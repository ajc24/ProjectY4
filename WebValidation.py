#   Student Name:   Anthony Cox
#   Student ID:     C00162988
#   Date:           18th February 2015
#   Purpose:        This file performs all validation on user entries from the UI on server side (to prevent security threats).
#                   Each method returns either an OK validation message or returns the full error message of what needs to be changed.

import ValidationProcessing

#===== Login and Registration Validation Methods ====================================================================================================================

# Validate the first set of registration details by the user
def validateFirstRegistrationDetails(schoolName, emailAddress, confirmedEmail, password, confirmedPassword):
    numberOfErrors = 0
    errorMessages = ""

    validationListA = validateSchoolNameEntry(schoolName, numberOfErrors, errorMessages)
    numberOfErrors = validationListA[0]
    errorMessages = validationListA[1]

    validationListB = validateEmailAddressEntry(emailAddress, numberOfErrors, errorMessages)
    numberOfErrors = validationListB[0]
    errorMessages = validationListB[1]

    validationListC = validateConfirmedEmailEntry(emailAddress, confirmedEmail, numberOfErrors, errorMessages)
    numberOfErrors = validationListC[0]
    errorMessages = validationListC[1]

    validationListD = validatePasswordEntry(password, numberOfErrors, errorMessages)
    numberOfErrors = validationListD[0]
    errorMessages = validationListD[1]

    validationListE = validateConfirmedPasswordEntry(password, confirmedPassword, numberOfErrors, errorMessages)
    numberOfErrors = validationListE[0]
    errorMessages = validationListE[1]

    if errorMessages == "":
        schoolEmailIsADuplicate = ValidationProcessing.checkIfSchoolEmailIsDuplicate(emailAddress)
        personEmailIsADuplicate = ValidationProcessing.checkIfPersonEmailIsDuplicate(emailAddress)
        if schoolEmailIsADuplicate == True or personEmailIsADuplicate == True:
            numberOfErrors += 1
            errorMessages += str(numberOfErrors) + ": The email you entered has already been registered with our application. Please try another.\n"

    if errorMessages == "":
        return "OK"
    else:
        return "The following problems were found with your entries:\n\n" + errorMessages

# Validate the second set of registration details by the user
def validateSecondRegistrationDetails(emailAddress, streetName1, streetName2, townOrCity, county, phoneNumber):
    numberOfErrors = 0
    errorMessages = ""

    validationListA = validateAddressEntries(streetName1, streetName2, townOrCity, county, numberOfErrors, errorMessages)
    numberOfErrors = validationListA[0]
    errorMessages = validationListA[1]

    validationListB = validatePhoneNumberEntry(phoneNumber, numberOfErrors, errorMessages)
    numberOfErrors = validationListB[0]
    errorMessages = validationListB[1]

    if errorMessages == "":
        isADuplicate = ValidationProcessing.checkIfSchoolEmailIsDuplicate(emailAddress)
        if isADuplicate == True:
            numberOfErrors += 1
            errorMessages += str(numberOfErrors) + ": This school/email address has already been registered with our application. Please return to login and retry registration again.\n"

    if errorMessages == "":
        return "OK"
    else:
        return "The following problems were found with your entries:\n\n" + errorMessages

#===== School Details Validation Methods ============================================================================================================================

# Validate the new school location entries are correct
def validateNewSchoolLocation(schoolId, locationName, streetName1, streetName2, townOrCity, county):
    numberOfErrors = 0
    errorMessages = ""

    validationListA = validateAddressEntries(streetName1, streetName2, townOrCity, county, numberOfErrors, errorMessages)
    numberOfErrors = int(validationListA[0])
    errorMessages = validationListA[1]

    validationListB = validateLocationName(locationName, numberOfErrors, errorMessages)
    numberOfErrors = int(validationListB[0])
    errorMessages = validationListB[1]

    isADuplicate = ValidationProcessing.checkIfLocationNameIsADuplicate(schoolId, locationName)
    if isADuplicate == True:
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": The location name you entered has already been linked to your school. Please try another.\n"

    if errorMessages == "":
        return "OK"
    else:
        return "The following problems were found with your entries:\n\n" + errorMessages

# Validate that the edited location entry is correct
def validateEditedSchoolLocation(schoolId, locationId, addressId, locationName, streetName1, streetName2, townOrCity, county):
    numberOfErrors = 0
    errorMessages = ""

    validationListA = validateAddressEntries(streetName1, streetName2, townOrCity, county, numberOfErrors, errorMessages)
    numberOfErrors = int(validationListA[0])
    errorMessages = validationListA[1]

    validationListB = validateLocationName(locationName, numberOfErrors, errorMessages)
    numberOfErrors = int(validationListB[0])
    errorMessages = validationListB[1]

    isADuplicate = ValidationProcessing.checkIfEditedLocationNameIsADuplicate(schoolId, locationId, locationName)
    if isADuplicate == True:
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": The location name you entered has already been linked to your school. Please try another.\n"

    if errorMessages == "":
        return "OK"
    else:
        return "The following problems were found with your entries:\n\n" + errorMessages

# Validate that the school details entries are correct
def validateSchoolDetails(schoolId, schoolName, addressId, streetName1, streetName2, townOrCity, county, phoneNumber, emailAddress, confirmedEmail):
    numberOfErrors = 0
    errorMessages = ""

    validationListA = validateSchoolNameEntry(schoolName, numberOfErrors, errorMessages)
    numberOfErrors = validationListA[0]
    errorMessages = validationListA[1]
        
    validationListB = validateAddressEntries(streetName1, streetName2, townOrCity, county, numberOfErrors, errorMessages)
    numberOfErrors = validationListB[0]
    errorMessages = validationListB[1]

    validationListC = validatePhoneNumberEntry(phoneNumber, numberOfErrors, errorMessages)
    numberOfErrors = validationListC[0]
    errorMessages = validationListC[1]
    		
    validationListD = validateEmailAddressEntry(emailAddress, numberOfErrors, errorMessages)
    numberOfErrors = validationListD[0]
    errorMessages = validationListD[1]

    validationListE = validateConfirmedEmailEntry(emailAddress, confirmedEmail, numberOfErrors, errorMessages)
    numberOfErrors = validationListE[0]
    errorMessages = validationListE[1]
		
    if errorMessages == "":
        schoolEmailIsADuplicate = False
        personEmailIsADuplicate = False
        emailHasChanged = ValidationProcessing.checkIfSchoolEmailHasChanged(schoolId, emailAddress)
        if emailHasChanged == True:
            schoolEmailIsADuplicate = ValidationProcessing.checkIfSchoolEmailIsDuplicate(emailAddress)
            personEmailIsADuplicate = ValidationProcessing.checkIfPersonEmailIsDuplicate(emailAddress)

        if emailHasChanged == True and (schoolEmailIsADuplicate == True or personEmailIsADuplicate == True):
            numberOfErrors += 1
            errorMessages += str(numberOfErrors) + ": The email you entered is not a unique email address. Please try another.\n"

    if errorMessages == "":
        return "OK"
    else:
        return "The following problems were found with your entries:\n\n" + errorMessages

# Validate that the schools opening hours have been set correctly
def validateOpeningHours(listOfOpeningHoursSettings):
    numberOfErrors = 0
    errorMessages = ""
    for index in range(0, listOfOpeningHoursSettings.__len__()):
        if listOfOpeningHoursSettings[index].openOrClosed == "open":
            currentDay = determineDayByIndexPosition(index)
            startHour = int(listOfOpeningHoursSettings[index].openingTime[0:listOfOpeningHoursSettings[index].openingTime.index(":")])
            closingHour = int(listOfOpeningHoursSettings[index].closingTime[0:listOfOpeningHoursSettings[index].closingTime.index(":")])
            if closingHour <= startHour:
                numberOfErrors += 1
                errorMessages += str(numberOfErrors) + ": You have set the times incorrectly for " + currentDay + ".\n"
    if errorMessages == "":
        return "OK"
    else:
        return "The following problems were found with your entries:\n\n" + errorMessages

#===== Account Details Validation Methods ===========================================================================================================================

# Validate that the proposed new school account details are correct
def validateSchoolAccountDetails(schoolId, currentPassword, newPassword, confirmedPassword):
    numberOfErrors = 0
    errorMessages = ""

    currentPasswordIsCorrect = ValidationProcessing.checkIfCurrentSchoolPasswordIsCorrect(schoolId, currentPassword)
    if currentPasswordIsCorrect == False:
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": The current password entered is not the password linked to this account.\n"

    if errorMessages == "":
        validationListA = validatePasswordEntry(newPassword, numberOfErrors, errorMessages)
        numberOfErrors = validationListA[0]
        errorMessages = validationListA[1]

        validationListB = validateConfirmedPasswordEntry(newPassword, confirmedPassword, numberOfErrors, errorMessages)
        numberOfErrors = validationListB[0]
        errorMessages = validationListB[1]
        errorMessages = errorMessages.replace("password", "new password")

    if errorMessages == "":
        return "OK"
    else:
        return "The following problems were found with your entries:\n\n" + errorMessages

# Validate that the proposed new person account details are correct
def validatePersonAccountDetails(personId, accountStyle, currentPassword, newPassword, confirmedPassword):
    numberOfErrors = 0
    errorMessages = ""

    currentPasswordIsCorrect = ValidationProcessing.checkIfCurrentPersonPasswordIsCorrect(personId, accountStyle, currentPassword)
    if currentPasswordIsCorrect == False:
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": The current password entered is not the password linked to this account.\n"

    if errorMessages == "":
        validationListA = validatePasswordEntry(newPassword, numberOfErrors, errorMessages)
        numberOfErrors = validationListA[0]
        errorMessages = validationListA[1]

        validationListB = validateConfirmedPasswordEntry(newPassword, confirmedPassword, numberOfErrors, errorMessages)
        numberOfErrors = validationListB[0]
        errorMessages = validationListB[1]
        errorMessages = errorMessages.replace("password", "new password")

    if errorMessages == "":
        return "OK"
    else:
        return "The following problems were found with your entries:\n\n" + errorMessages

# Validate that the new/reset person account details are correct
def validateExistingPersonAccountDetails(password, confirmedPassword):
    numberOfErrors = 0
    errorMessages = ""

    validationListA = validatePasswordEntry(password, numberOfErrors, errorMessages)
    numberOfErrors = validationListA[0]
    errorMessages = validationListA[1]

    validationListB = validateConfirmedPasswordEntry(password, confirmedPassword, numberOfErrors, errorMessages)
    numberOfErrors = validationListB[0]
    errorMessages = validationListB[1]

    if errorMessages == "":
        return "OK"
    else:
        return "The following problems were found with your entries:\n\n" + errorMessages

#===== Lesson Details Validation Methods ============================================================================================================================

# Validate that the new lesson details are correct
def validateNewLessonDetails(schoolId, lessonName, abbreviatedName, lessonColour):
    numberOfErrors = 0
    errorMessages = ""

    validationListA = validateLessonDetails(schoolId, lessonName, abbreviatedName, lessonColour, numberOfErrors, errorMessages)
    numberOfErrors = validationListA[0]
    errorMessages = validationListA[1]

    if errorMessages == "":
        isUnique = ValidationProcessing.checkIfLessonEntryIsUnique(schoolId, lessonName)
        if isUnique == False:
            numberOfErrors += 1
            errorMessages += str(numberOfErrors) + ": The lesson name you entered is not unique. Please try another.\n"

    if errorMessages == "":
        return "OK"
    else:
        return "The following problems were found with your entries:\n\n" + errorMessages

# Validate that the edited lesson details are correct
def validateEditedLessonDetails(schoolLessonId, schoolId, lessonName, abbreviatedName, lessonColour):
    numberOfErrors = 0
    errorMessages = ""

    validationListA = validateLessonDetails(schoolId, lessonName, abbreviatedName, lessonColour, numberOfErrors, errorMessages)
    numberOfErrors = validationListA[0]
    errorMessages = validationListA[1]
    if errorMessages == "":
        hasChanged = ValidationProcessing.checkIfLessonNameHasChanged(schoolLessonId, lessonName)
        if hasChanged == True:
            isUnique = ValidationProcessing.checkIfLessonEntryIsUnique(schoolId, lessonName)
            if isUnique == False:
                numberOfErrors += 1
                errorMessages += str(numberOfErrors) + ": The lesson name you entered is not unique. Please try another.\n"

    if errorMessages == "":
        return "OK"
    else:
        return "The following problems were found with your entries:\n\n" + errorMessages
    
#===== Student Details Validation Methods ===========================================================================================================================

# Validate that the new student entries are correct
def validateNewStudentDetails(schoolId, firstName, surname, dateOfBirth, phoneNumber, emailAddress, confirmedEmail, streetName1, streetName2, townOrCity, county):
    numberOfErrors = 0
    errorMessages = ""

    validationListA = validatePersonDetails(firstName, surname, dateOfBirth, phoneNumber, emailAddress, numberOfErrors, errorMessages)
    numberOfErrors = validationListA[0]
    errorMessages = validationListA[1]

    validationListB = validateConfirmedEmailEntry(emailAddress, confirmedEmail, numberOfErrors, errorMessages)
    numberOfErrors = validationListB[0]
    errorMessages = validationListB[1]

    validationListC = validateAddressEntries(streetName1, streetName2, townOrCity, county, numberOfErrors, errorMessages)
    numberOfErrors = validationListC[0]
    errorMessages = validationListC[1]

    if errorMessages == "":
        studentIsUnique = ValidationProcessing.checkIfStudentIsUnique(schoolId, firstName, surname, dateOfBirth, phoneNumber, emailAddress)
        if studentIsUnique == False:
            numberOfErrors += 1
            errorMessages += str(numberOfErrors) + ": This student has already been registered in your school. You cannot add this student again.\n"

        studentEmailMatchesSchool = ValidationProcessing.checkIfSchoolEmailIsDuplicate(emailAddress)
        studentEmailMatchesPerson = ValidationProcessing.checkIfCommonPersonEmailIsDuplicate(firstName, surname, dateOfBirth, phoneNumber, emailAddress)
        if studentEmailMatchesSchool == True or studentEmailMatchesPerson == True:
            numberOfErrors += 1
            errorMessages += str(numberOfErrors) + ": This email has been previously registered with the system. Please try a different/unique email.\n"

    if errorMessages == "":
        return "OK"
    else:
        return "The following problems were found with your entries:\n\n" + errorMessages

# Validate that the edited student entries are correct
def validateEditedStudentDetails(schoolId, personId, firstName, surname, dateOfBirth, phoneNumber, emailAddress, streetName1, streetName2, townOrCity, county):
    numberOfErrors = 0
    errorMessages = ""

    validationListA = validatePersonDetails(firstName, surname, dateOfBirth, phoneNumber, emailAddress, numberOfErrors, errorMessages)
    numberOfErrors = validationListA[0]
    errorMessages = validationListA[1]

    validationListB = validateAddressEntries(streetName1, streetName2, townOrCity, county, numberOfErrors, errorMessages)
    numberOfErrors = validationListB[0]
    errorMessages = validationListB[1]

    if errorMessages == "":
        personChanged = ValidationProcessing.checkIfPersonHasChanged(personId, firstName, surname, dateOfBirth, phoneNumber, emailAddress)
        if personChanged == True:
            isUnique = ValidationProcessing.checkIfStudentIsUnique(schoolId, firstName, surname, dateOfBirth, phoneNumber, emailAddress)
            if isUnique == False:
                numberOfErrors += 1
                errorMessages += str(numberOfErrors) + ": This student has already been registered in your school.\n"

            emailChanged = ValidationProcessing.checkIfPersonEmailHasChanged(personId, emailAddress)
            if emailChanged == True:
                studentEmailMatchesSchool = ValidationProcessing.checkIfSchoolEmailIsDuplicate(emailAddress)
                studentEmailMatchesPerson = ValidationProcessing.checkIfCommonPersonEmailIsDuplicate(firstName, surname, dateOfBirth, phoneNumber, emailAddress)

                if studentEmailMatchesSchool == True or studentEmailMatchesPerson == True:
                    numberOfErrors += 1
                    errorMessages += str(numberOfErrors) + ": This email has been previously registered with the system. Please try a different/unique email.\n"

    if errorMessages == "":
        return "OK"
    else:
        return "The following problems were found with your entries:\n\n" + errorMessages

#===== Teacher Details Validation Methods ===========================================================================================================================

# Validate that the new teacher entries are correct
def validateNewTeacherDetails(schoolId, firstName, surname, dateOfBirth, phoneNumber, emailAddress, confirmedEmail, streetName1, streetName2, townOrCity, county):
    numberOfErrors = 0
    errorMessages = ""

    validationListA = validatePersonDetails(firstName, surname, dateOfBirth, phoneNumber, emailAddress, numberOfErrors, errorMessages)
    numberOfErrors = validationListA[0]
    errorMessages = validationListA[1]

    validationListB = validateConfirmedEmailEntry(emailAddress, confirmedEmail, numberOfErrors, errorMessages)
    numberOfErrors = validationListB[0]
    errorMessages = validationListB[1]

    validationListC = validateAddressEntries(streetName1, streetName2, townOrCity, county, numberOfErrors, errorMessages)
    numberOfErrors = validationListC[0]
    errorMessages = validationListC[1]

    if errorMessages == "":
        teacherIsUnique = ValidationProcessing.checkIfTeacherIsUnique(schoolId, firstName, surname, dateOfBirth, phoneNumber, emailAddress)
        if teacherIsUnique == False:
            numberOfErrors += 1
            errorMessages += str(numberOfErrors) + ": This teacher has already been registered in your school.\n"

        teacherEmailMatchesSchool = ValidationProcessing.checkIfSchoolEmailIsDuplicate(emailAddress)
        teacherEmailMatchesPerson = ValidationProcessing.checkIfCommonPersonEmailIsDuplicate(firstName, surname, dateOfBirth, phoneNumber, emailAddress)
        if teacherEmailMatchesSchool == True or teacherEmailMatchesPerson == True:
            numberOfErrors += 1
            errorMessages += str(numberOfErrors) + ": This email has been previously registered with the system. Please try a different/unique email.\n"

    if errorMessages == "":
        return "OK"
    else:
        return "The following problems were found with your entries:\n\n" + errorMessages

# Validate that the edited teacher entries are correct
def validateEditedTeacherDetails(schoolId, personId, firstName, surname, dateOfBirth, phoneNumber, emailAddress, streetName1, streetName2, townOrCity, county):
    numberOfErrors = 0
    errorMessages = ""

    validationListA = validatePersonDetails(firstName, surname, dateOfBirth, phoneNumber, emailAddress, numberOfErrors, errorMessages)
    numberOfErrors = validationListA[0]
    errorMessages = validationListA[1]

    validationListB = validateAddressEntries(streetName1, streetName2, townOrCity, county, numberOfErrors, errorMessages)
    numberOfErrors = validationListB[0]
    errorMessages = validationListB[1]

    if errorMessages == "":
        personChanged = ValidationProcessing.checkIfPersonHasChanged(personId, firstName, surname, dateOfBirth, phoneNumber, emailAddress)
        if personChanged == True:
            isUnique = ValidationProcessing.checkIfTeacherIsUnique(schoolId, firstName, surname, dateOfBirth, phoneNumber, emailAddress)
            if isUnique == False:
                numberOfErrors += 1
                errorMessages += str(numberOfErrors) + ": This teacher has already been registered in your school.\n"

            emailChanged = ValidationProcessing.checkIfPersonEmailHasChanged(personId, emailAddress)
            if emailChanged == True:
                teacherEmailMatchesSchool = ValidationProcessing.checkIfSchoolEmailIsDuplicate(emailAddress)
                teacherEmailMatchesPerson = ValidationProcessing.checkIfCommonPersonEmailIsDuplicate(firstName, surname, dateOfBirth, phoneNumber, emailAddress)
                if teacherEmailMatchesSchool == True or teacherEmailMatchesPerson == True:
                    numberOfErrors += 1
                    errorMessages += str(numberOfErrors) + ": This email has been previously registered with the system. Please try a different/unique email.\n"

    if errorMessages == "":
        return "OK"
    else:
        return "The following problems were found with your entries:\n\n" + errorMessages

#===== Classroom Details Validation Methods =========================================================================================================================

# Validate that the new classroom entry details are correct
def validateClassroomDetails(locationId, roomName):
    numberOfErrors = 0
    errorMessages = ""

    if locationId == "not set":
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": You have not selected a location. Please choose one before submitting.\n"

    if roomName == "":
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": You have not entered a room name.\n"

    if roomName.__len__() > 10:
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": The room name you entered is too long (max 10 characters).\n"

    if errorMessages == "":
        isUnique = ValidationProcessing.checkIfClassroomIsUnique(locationId, roomName)
        if isUnique == False:
            numberOfErrors += 1
            errorMessages += str(numberOfErrors) + ": This classroom has already been added to this location.\n"

    if errorMessages == "":
        return "OK"
    else:
        return "The following problems were found with your entries:\n\n" + errorMessages

#===== Timetable Details Validation Methods =========================================================================================================================

# Validate that the entries from the "Schedule A Lesson" feature of the timetable editor are correct
def validateScheduleLessonDetails(lessonValue, teacherValue, classroomValue):
    numberOfErrors = 0
    errorMessages = ""

    if lessonValue == "":
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": You have not entered/selected a valid lesson name.\n"

    if teacherValue == "":
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": You have not entered/selected a valid teacher name.\n"

    if classroomValue == "":
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": You have not entered/selected a valid classroom name.\n"

    if errorMessages == "":
        return "OK"
    else:
        return "The following problems were found with your entries:\n\n" + errorMessages

# Validate that none of the lessons collide with this students/classrooms/teachers other lessons
def validateLessonCollisions(timetableStartHour, listOfTimetableData):
    errorMessages = ""
    index = 0
    while index < listOfTimetableData.__len__():
        weekdayId = int(listOfTimetableData[index])
        startHour = int(listOfTimetableData[index + 1])
        startMin = int(listOfTimetableData[index + 2])
        lessonLength = int(listOfTimetableData[index + 3])
        schoolId = int(listOfTimetableData[index + 4])
        studentId = int(listOfTimetableData[index + 5])
        schoolLessonId = int(listOfTimetableData[index + 6])
        teacherId = int(listOfTimetableData[index + 7])
        locationId = int(listOfTimetableData[index + 8])
        classroomId = int(listOfTimetableData[index + 9])

        # Determine the lessons start time and end time (in minutes)
        lessonStartTime = ((startHour - timetableStartHour) * 60) + startMin
        lessonEndTime = lessonStartTime + lessonLength
       
        # Determine the lesson end hour figure for database processing
        endHour = startHour
        endMin = startMin + lessonLength
        while endMin > 60:
            endHour += 1
            endMin -= 60

        # Check if the lesson collides with any other lessons scheduled by other schools
        errorMessages += ValidationProcessing.verifyIfLessonTimeIsUnique(schoolId, studentId, weekdayId, schoolLessonId, lessonStartTime, lessonEndTime,
                                                                         startHour, endHour, startMin, timetableStartHour)
        
        # Check if the teacher is available at this requested time
        errorMessages += ValidationProcessing.verifyIfTeacherIsFreeAtThisTime(teacherId, weekdayId, studentId, lessonStartTime, lessonEndTime, startHour,
                                                                              endHour, startMin, timetableStartHour)
        
        # Check if this classroom is available at this time
        errorMessages += ValidationProcessing.verifyIfClassroomIsFreeAtThisTime(schoolId, weekdayId, studentId, locationId, classroomId, lessonStartTime,
                                                                                lessonEndTime, startHour, endHour, startMin, timetableStartHour)
        index += 10

    if errorMessages == "":
        return "OK"
    else:
        return "The following problems were found with your timetable proposal:\n\n" + errorMessages

#===== General Validation Methods (Used Across Multiple Validations) ================================================================================================

# Location name checks - common across multiple screens
def validateLocationName(locationName, numberOfErrors, errorMessages):
    if locationName == "":
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": You have not entered a name for your new location.\n"

    if locationName.__len__() > 50:
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": The location name you entered is too long (max 50 characters).\n"
    return [numberOfErrors, errorMessages]

# Address entry checks - common across multiple screens
def validateAddressEntries(streetName1, streetName2, townOrCity, county, numberOfErrors, errorMessages):
    if streetName1 == "" and streetName2 == "":
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": You have not entered a valid street name in either street name field.\n"

    if townOrCity == "":
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": You have not entered a town or city name.\n"

    if county == "":
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": You have not entered a county name.\n"

    if streetName1.__len__() > 25:
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": The 1st street name you entered is too long (max 50 characters).\n"

    if streetName2.__len__() > 25:
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": The 2nd street name you entered is too long (max 50 characters).\n"

    if townOrCity.__len__() > 25:
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": The town/city you entered is too long (max 50 characters).\n"

    if county.__len__() > 20:
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": The county you entered is too long (max 20 characters).\n"
    return [numberOfErrors, errorMessages]

# Determine the current day based on the current index position
def determineDayByIndexPosition(indexPos):
    if indexPos == 0:
        return "Monday"
    elif indexPos == 1:
        return "Tuesday"
    elif indexPos == 2:
        return "Wednesday"
    elif indexPos == 3:
        return "Thursday"
    elif indexPos == 4:
        return "Friday"
    elif indexPos == 5:
        return "Saturday"
    else:
        return "Sunday"

# Validate that the lesson details entries are correct - common across multiple screens
def validateLessonDetails(schoolId, lessonName, abbreviatedName, lessonColour, numberOfErrors, errorMessages):
    if lessonName == "":
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": You have not entered a name for the lesson.\n"

    if abbreviatedName == "":
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": You have not entered an abbreviated name for the lesson.\n"

    if lessonName.__len__() > 50:
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": The lesson name you have entered is too long (max 50 characters).\n"

    if abbreviatedName.__len__() > 10:
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": You abbreviated name you have entered is too long (max 10 characters).\n"

    if lessonColour == "not set":
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": You have not selected a colour.\n"
    return [numberOfErrors, errorMessages]

# Validate that the new person details are correct - common across multiple screens
def validatePersonDetails(firstName, surname, dateOfBirth, phoneNumber, emailAddress, numberOfErrors, errorMessages):
    if firstName == "":
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": You have not entered a first name.\n"

    if firstName.__len__() > 25:
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": The first name you entered is too long (max 25 characters).\n"
        
    if surname == "":
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": You have not entered a surname.\n"

    if surname.__len__() > 25:
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": The surname you entered is too long (max 25 characters).\n"

    try:
        indexOfFirstSlash = dateOfBirth.index("/")
    except ValueError:
        indexOfFirstSlash = -1

    try:
        indexOfSecondSlash = dateOfBirth.rindex("/")
    except ValueError:
        indexOfSecondSlash = -1

    if indexOfFirstSlash == -1 or indexOfSecondSlash == -1:
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": The date of birth is not in the correct DD/MM/YY format.\n"

    if indexOfFirstSlash > -1 and indexOfSecondSlash > -1:
        if indexOfFirstSlash == indexOfSecondSlash:
            numberOfErrors += 1
            errorMessages += str(numberOfErrors) + ": You have not entered two '/' characters in the date of birth field. The format should be DD/MM/YY.\n"

    if errorMessages == "":
        daySet = dateOfBirth[0:dateOfBirth.index("/")]
        monthSet = dateOfBirth[dateOfBirth.index("/") + 1:dateOfBirth.rindex("/")]
        yearSet = dateOfBirth[dateOfBirth.rindex("/") + 1:]

        try:
            daySet = int(daySet)
            monthSet = int(monthSet)
            yearSet = int(yearSet)
        except ValueError:
            numberOfErrors += 1
            errorMessages += str(numberOfErrors) + ": You have not entered a valid date in the format DD/MM/YY for the date of birth.\n"

    if errorMessages == "":
        if monthSet >= 1 and monthSet <= 12:
            if monthSet == 4 or monthSet == 6 or monthSet == 9 or monthSet == 11:
                if daySet < 1 or daySet > 30:
                    numberOfErrors += 1
                    errorMessages += str(numberOfErrors) + ": You have not entered a valid day in the range of 1 to 30 in the date of birth entry.\n"

            if monthSet == 1 or monthSet == 3 or monthSet == 5 or monthSet == 7 or monthSet == 8 or monthSet == 10 or monthSet == 12:
                if daySet < 1 or daySet > 31:
                    numberOfErrors += 1
                    errorMessages += str(numberOfErrors) + ": You have not entered a valid day in the range of 1 to 31 in the date of birth entry.\n"

            if monthSet == 2:
                if yearSet % 4 == 0:
                    if daySet < 1 or daySet > 29:
                        numberOfErrors += 1
                        errorMessages += str(numberOfErrors) + ": You have not entered a valid day in the range of 1 to 29 in the date of birth entry.\n"
                else:
                    if daySet < 1 or daySet > 28:
                        numberOfErrors += 1
                        errorMessages += str(numberOfErrors) + ": You have not entered a valid day in the range of 1 to 28 in the date of birth entry.\n" 
        else:
            numberOfErrors += 1
            errorMessages += str(numberOfErrors) + ": You have not entered a valid month in the range of 1 to 12 in the date of birth entry.\n"
    
    validationListA = validatePhoneNumberEntry(phoneNumber, numberOfErrors, errorMessages)
    numberOfErrors = validationListA[0]
    errorMessages = validationListA[1]

    validationListB = validateEmailAddressEntry(emailAddress, numberOfErrors, errorMessages)
    numberOfErrors = validationListB[0]
    errorMessages = validationListB[1]

    return [numberOfErrors, errorMessages]

# Validate that the email entry and format is correct - common across multiple screens
def validateEmailAddressEntry(emailAddress, numberOfErrors, errorMessages):
    if emailAddress == "":
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": You have not entered an email address.\n"

    if emailAddress.__len__() > 50:
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": The email address you entered is too long (max 50 characters).\n"

    try:
        indexOfAt = emailAddress.index("@")
    except ValueError:
        indexOfAt = -1

    try:
        indexOfDot = emailAddress.rindex(".")
    except ValueError:
        indexOfDot = -1

    if indexOfAt == -1:
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": The email address must contain an '@' character.\n"

    if indexOfDot == -1:
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": The email address must contain at least one '.' character.\n"
        
    if indexOfAt > indexOfDot:
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": The email address must contain a '.' character after the '@' character.\n"
    return [numberOfErrors, errorMessages]

# Validate that the phone number entry is correct - common across multiple screens
def validatePhoneNumberEntry(phoneNumber, numberOfErrors, errorMessages):
    if phoneNumber == "":
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": You have not entered a phone number for your school.\n"
    
    if phoneNumber.__len__() > 20:
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": The phone number you entered is too long (max 20 characters).\n"
    return [numberOfErrors, errorMessages]

# Validate that the confirmed email address entry is correct - common across multiple screens
def validateConfirmedEmailEntry(emailAddress, confirmedEmail, numberOfErrors, errorMessages):
    if confirmedEmail == "":
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": You have not confirmed the email address.\n"
	
    if confirmedEmail.__len__() > 50:
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": The confirmed email address you entered is too long (max 50 characters).\n"

    if emailAddress != confirmedEmail:
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": The email address and confirmed email address do not match.\n"
    return [numberOfErrors, errorMessages]

# Validate that the school name entry is correct - common across multiple screens
def validateSchoolNameEntry(schoolName, numberOfErrors, errorMessages):
    if schoolName == "":
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": You have not entered a name for your school.\n"

    if schoolName.__len__() > 50:
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": The school name you entered is too long (max 50 characters).\n"
    return [numberOfErrors, errorMessages]

# Validate that the password entered is correct - common across multiple screens
def validatePasswordEntry(password, numberOfErrors, errorMessages):
    if password == "":
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": You have not entered a password.\n"

    if password.__len__() < 3:
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": The password you entered is too short. It must be at least 3 characters in length.\n"

    if password.__len__() > 50:
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": The password you entered is too long (max 50 characters).\n"

    foundUpper = False
    foundLower = False
    foundNumber = False
    index = 0
    while index < password.__len__() and (foundUpper == False or foundLower == False or foundNumber == False):
        if password[index].isupper() and foundUpper == False:
            foundUpper = True
        elif password[index].islower() and foundLower == False:
            foundLower = True
        elif password[index].isnumeric() and foundNumber == False:
            foundNumber = True
        index += 1

    if foundUpper == False:
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": The password you entered does not contain an uppercase character.\n"

    if foundLower == False:
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": The password you entered does not contain a lowercase character.\n"

    if foundNumber == False:
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": The password you entered does not contain a number.\n"

    return [numberOfErrors, errorMessages]

# Validate that the confirmed password entry is correct - common across multiple screens
def validateConfirmedPasswordEntry(password, confirmedPassword, numberOfErrors, errorMessages):
    if confirmedPassword == "":
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": You have not confirmed your password.\n"

    if confirmedPassword.__len__() > 50:
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": The confirmed password you entered is too long (max 50 characters).\n"

    if password != confirmedPassword:
        numberOfErrors += 1
        errorMessages += str(numberOfErrors) + ": The password and confirmed password do not match.\n"
    return [numberOfErrors, errorMessages]
