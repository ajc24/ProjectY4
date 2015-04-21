#   Student Name:   Anthony Cox
#   Student ID:     C00162988
#   Date:           9th February 2015
#   Purpose:        This file works with any data sent from the browser and/or data that is required to be sent to the browser.
#                   It also acts as an access point to the DatabaseController for sending data to the database and also receiving
#                   data from the database.

import ClassesList
import DatabaseController
from flask import session

# Global Attributes
accountTypes = ["Administrator", "Teacher", "Student"]

#===== Login Details Processing =====================================================================================================================================

# Determine if the login details are correct, setting required session variables if they are correct
def verifyUserLoginDetails(emailAddress, password):
    schoolEmailCountRecord = DatabaseController.checkIfDuplicateSchoolEmail(emailAddress)
    schoolEmailCount = int(schoolEmailCountRecord[0][0])
    if schoolEmailCount > 0:
        schoolIdRecord = DatabaseController.getSchoolIdBasedOnEmailAddress(emailAddress)
        schoolId = int(schoolIdRecord[0][0])
        accountPasswordRecord = DatabaseController.getAccountPasswordBasedOnSchoolId(schoolId)
        accountPassword = accountPasswordRecord[0][0]
        if password == accountPassword:
            schoolNameRecord = DatabaseController.getSchoolNameBasedOnSchoolId(schoolId)
            schoolName = schoolNameRecord[0][0]
            session["loginId"] = schoolId
            session["loginName"] = schoolName
            session["loggedIn"] = True
            session["accountType"] = accountTypes[0]
            return True
        else:
            return False
    else:
        personEmailCountRecord = DatabaseController.countNumberOfDuplicatePersonEmailAddresses(emailAddress)
        personEmailCount = int(personEmailCountRecord[0][0])
        if personEmailCount > 0:
            personIdRecord = DatabaseController.getPersonIdBasedOnEmailAddress(emailAddress)
            personId = int(personIdRecord[0][0])
            accountPasswordRecord = DatabaseController.getAccountPasswordBasedOnPersonId(personId)
            if accountPasswordRecord.__len__() > 0:
                accountPassword = accountPasswordRecord[0][0]
                if password == accountPassword:
                    personNameRecord = DatabaseController.getPersonDetailsByPersonId(personId)
                    personName = "" + personNameRecord[0][0] + " " + personNameRecord[0][1]

                    accountTypeRecord = DatabaseController.getAccountTypeBasedOnPersonIdAndPassword(personId, accountPassword)
                    typeOfAccount = accountTypeRecord[0][0]
                    if typeOfAccount == "Teacher":
                        personIdRecord = DatabaseController.getTeacherIdFromPersonId(personId)
                        personId = int(personIdRecord[0][0])
                    elif typeOfAccount == "Student":
                        personIdRecord = DatabaseController.getStudentIdFromPersonId(personId)
                        personId = int(personIdRecord[0][0])
                    
                    session["loginId"] = personId
                    session["loginName"] = personName
                    session["loggedIn"] = True
                    session["accountType"] = accountTypeRecord[0][0]
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

#===== Account Details Processing ===================================================================================================================================

# Update the current schools account password
def updateAccountPassword(schoolOrPersonId, password, typeOfAccount):
    if typeOfAccount == "school":
        DatabaseController.updateSchoolAccountPassword(schoolOrPersonId, password)
    elif typeOfAccount == "teacher":
        DatabaseController.updatePersonAccountPassword(accountTypes[1], 0, schoolOrPersonId, password)
    elif typeOfAccount == "student":
        DatabaseController.updatePersonAccountPassword(accountTypes[2], 0, schoolOrPersonId, password)

# Search for all teacher accounts with the names provided for the school id provided
def getTeacherAccountsList(schoolId, firstName, surname):
    listOfTeacherAccounts = []
    listOfTeacherRecords = DatabaseController.getTeacherAccountsList(schoolId, firstName, surname)
    for eachRecord in listOfTeacherRecords:
        for index in range(0, eachRecord.__len__()):
            listOfTeacherAccounts.append(eachRecord[index])
        currentPersonId = int(eachRecord[0])
        accountPasswordRecord  = DatabaseController.getAccountPasswordBasedOnPersonIdAndType(currentPersonId, accountTypes[1])
        if accountPasswordRecord.__len__() > 0:
            listOfTeacherAccounts.append(accountPasswordRecord[0][0])
            listOfTeacherAccounts.append(True)
        else:
            listOfTeacherAccounts.append("")
            listOfTeacherAccounts.append(False)
    return listOfTeacherAccounts

# Search for all student accounts with the names provided for the school id provided
def getStudentAccountsList(schoolId, firstName, surname):
    listOfStudentAccounts = []
    listOfStudentRecords = DatabaseController.getStudentAccountsList(schoolId, firstName, surname)
    for eachRecord in listOfStudentRecords:
        for index in range(0, eachRecord.__len__()):
            listOfStudentAccounts.append(eachRecord[index])
        currentPersonId = int(eachRecord[0])
        accountPasswordRecord  = DatabaseController.getAccountPasswordBasedOnPersonIdAndType(currentPersonId, accountTypes[2])
        if accountPasswordRecord.__len__() > 0:
            listOfStudentAccounts.append(accountPasswordRecord[0][0])
            listOfStudentAccounts.append(True)
        else:
            listOfStudentAccounts.append("")
            listOfStudentAccounts.append(False)
    return listOfStudentAccounts

# Insert a new person account into the database
def insertNewPersonAccount(accountStyle, personId, password):
    if accountStyle == "teacher":
        DatabaseController.insertNewPersonAccountRecord(accountTypes[1], 0, personId, password)
    else:
        DatabaseController.insertNewPersonAccountRecord(accountTypes[2], 0, personId, password)

# Update an existing person account
def updateExistingPersonAccount(accountStyle, personId, password):
    if accountStyle == "teacher":
        DatabaseController.updatePersonAccountPassword(accountTypes[1], 0, personId, password)
    else:
        DatabaseController.updatePersonAccountPassword(accountTypes[2], 0, personId, password)

# Delete the chosen person account
def deletePersonAccount(personId, accountStyle):
    DatabaseController.deleteAccountRecordBasedOnIdAndType(personId, accountStyle)

#===== School Details Processing ====================================================================================================================================

# Retrieve the school name of the school based on the provided school id
def getNameOfSchool(schoolId):
    schoolName = DatabaseController.getSchoolName(schoolId)
    return schoolName[0][0]

# Insert a new school record into the application database and initialise all other parameters required (opening hours & location)
def insertNewSchoolRecord(schoolName, emailAddress, streetName1, streetName2, townOrCity, county, phoneNumber, password):
    headLocation = 1
    personId = 0
    weekdayId = 1
    duplicateRecord = DatabaseController.countNumberOfDuplicateAddresses(streetName1, streetName2, townOrCity, county)
    duplicateValue = int(duplicateRecord[0][0])
    if duplicateValue == 0:
        insertNewAddressRecord(streetName1, streetName2, townOrCity, county)
    addressIdRecord = DatabaseController.getAddressId(streetName1, streetName2, townOrCity, county)
    addressId = int(addressIdRecord[0][0])

    DatabaseController.insertNewSchoolRecord(schoolName, addressId, phoneNumber, emailAddress)
    schoolIdRecord = DatabaseController.getSchoolIdBasedOnEmailAddress(emailAddress)
    schoolId = int(schoolIdRecord[0][0])
    DatabaseController.insertNewSchoolAccountRecord(accountTypes[0], schoolId, personId, password)

    while weekdayId <= 7:
        DatabaseController.insertNewOpeningHoursRecord(schoolId, weekdayId)
        weekdayId += 1
    insertNewLocationRecord(schoolId, schoolName, streetName1, streetName2, townOrCity, county, headLocation)
    

# Retrieve the full list of details for the current school
def getSchoolDetails(schoolId):
    schoolDetailsList = DatabaseController.getSchoolDetails(schoolId)
    return ClassesList.School(int(schoolDetailsList[0][0]), schoolDetailsList[0][1], int(schoolDetailsList[0][2]), schoolDetailsList[0][3], schoolDetailsList[0][4],
                                schoolDetailsList[0][5], schoolDetailsList[0][6], schoolDetailsList[0][7], schoolDetailsList[0][8])

# Update the school details for the current school
def updateSchoolDetails(schoolId, oldSchoolName, editedSchoolName, addressId, streetName1, streetName2, townOrCity, county, phoneNumber, emailAddress):
    if oldSchoolName != editedSchoolName:
        locationIdRecord = DatabaseController.getLocationId(schoolId, oldSchoolName)
        locationId = locationIdRecord[0][0]
        DatabaseController.updateLocationName(locationId, editedSchoolName)
        DatabaseController.updateSchoolDetails(schoolId, editedSchoolName, phoneNumber, emailAddress)
        session["loginName"] = editedSchoolName

    hasChanged = checkIfAddressHasChanged(addressId, streetName1, streetName2, townOrCity, county)
    if hasChanged == True:
        duplicateRecord = DatabaseController.countNumberOfDuplicateAddresses(streetName1, streetName2, townOrCity, county)
        duplicateValue = int(duplicateRecord[0][0])
        if duplicateValue == 0:
            insertNewAddressRecord(streetName1, streetName2, townOrCity, county)
        addressIdRecord = DatabaseController.getAddressId(streetName1, streetName2, townOrCity, county)
        addressIdValue = int(addressIdRecord[0][0])
        DatabaseController.updateSchoolAddressId(schoolId, addressIdValue)
        checkIfAddressIsUsed(addressId)

# Insert a new location record for this school and link them together
def insertNewLocationRecord(schoolId, locationName, streetName1, streetName2, townOrCity, county, headLocation):
    duplicateRecord = DatabaseController.countNumberOfDuplicateAddresses(streetName1, streetName2, townOrCity, county)
    duplicateValue = int(duplicateRecord[0][0])
    if duplicateValue == 0:
        insertNewAddressRecord(streetName1, streetName2, townOrCity, county)
    addressIdRecord = DatabaseController.getAddressId(streetName1, streetName2, townOrCity, county)
    addressId = int(addressIdRecord[0][0])
    DatabaseController.insertNewLocationRecord(locationName, schoolId, addressId, headLocation)

# Insert a new address record into the address table - returns the unique ID associated with the new record
def insertNewAddressRecord(streetName1, streetName2, townOrCity, county):
    maxRecord = DatabaseController.countRecordsInAddressTable()
    maxValue = int(maxRecord[0][0])
    addressId = maxValue + 1
    DatabaseController.insertNewAddressRecord(addressId, streetName1, streetName2, townOrCity, county)

# Get a list of locations linked to this school
def getListOfSchoolLocations(schoolId):
    listOfLocations = []
    locationRecords = DatabaseController.getListOfSchoolLocations(schoolId)
    for eachRecord in locationRecords:
        currentLocation = ClassesList.Location(int(eachRecord[0]), eachRecord[1], int(eachRecord[2]), eachRecord[3], eachRecord[4], eachRecord[5], eachRecord[6])
        listOfLocations.append(currentLocation)
    return listOfLocations

# Update the details for the current location
def updateLocationDetails(schoolId, locationId, addressId, locationName, streetName1, streetName2, townOrCity, county):
    schoolLocationId = getLocationIdOfSchoolName(schoolId)
    if schoolLocationId == int(locationId):
        DatabaseController.updateSchoolName(schoolId, locationName)
        session["loginName"] = locationName
    DatabaseController.updateLocationName(locationId, locationName)

    hasChanged = checkIfAddressHasChanged(addressId, streetName1, streetName2, townOrCity, county)
    if hasChanged == True:
        duplicateRecord = DatabaseController.countNumberOfDuplicateAddresses(streetName1, streetName2, townOrCity, county)
        duplicateValue = int(duplicateRecord[0][0])
        if duplicateValue == 0:
            insertNewAddressRecord(streetName1, streetName2, townOrCity, county)
        addressIdRecord = DatabaseController.getAddressId(streetName1, streetName2, townOrCity, county)
        addressIdValue = int(addressIdRecord[0][0])
        DatabaseController.updateSchoolAddressId(schoolId, addressIdValue)
        DatabaseController.updateLocationAddressId(locationId, addressIdValue)
        checkIfAddressIsUsed(addressId)

# Check if the submitted address has changed
def checkIfAddressHasChanged(addressId, streetName1, streetName2, townOrCity, county):
    storedAddress = DatabaseController.getAddressDetails(addressId)
    oldAddress = ClassesList.Address(addressId, storedAddress[0][1], storedAddress[0][2], storedAddress[0][3], storedAddress[0][4])
    editedAddress = ClassesList.Address(addressId, streetName1, streetName2, townOrCity, county)
    if oldAddress.__eq__(editedAddress) == True:
        return False
    else:
        return True

# Check if the provided address id is still used by any entity in the system
def checkIfAddressIsUsed(addressId):
    countRecordA = DatabaseController.countAddressUsageInSchools(addressId)
    countRecordB = DatabaseController.countAddressUsageInLocations(addressId)
    countRecordC = DatabaseController.countAddressUsageInStudents(addressId)
    countRecordD = DatabaseController.countAddressUsageInTeachers(addressId)
    countValueA = int(countRecordA[0][0])
    countValueB = int(countRecordB[0][0])
    countValueC = int(countRecordC[0][0])
    countValueD = int(countRecordD[0][0])
    countTotal = countValueA + countValueB + countValueC + countValueD
    if countTotal == 0:
        DatabaseController.deleteAddressRecord(addressId)

# Remove a selected record from the database
def removeLocationRecord(locationId, addressId):
    headLocationRecord = DatabaseController.getLocationHeadLocation(locationId)
    headLocation = int(headLocationRecord[0][0])
    if headLocation == int(locationId):
        return False
    else:
        DatabaseController.removeLocationRecord(locationId)
        checkIfAddressIsUsed(addressId)
        locationClassroomRecords = DatabaseController.getLocationClassroomRecords(locationId)
        for eachClassroom in locationClassroomRecords:
            recordId = int(eachClassroom[0])
            classroomId = int(eachClassroom[1])
            DatabaseController.deleteClassroomLocationRecordById(recordId)
            manageClassroomUsage(classroomId)
        DatabaseController.deleteTimetableRecordsBasedOnLocationId(locationId)
        return True

# Get the location id of the location name that matches the schools name
def getLocationIdOfSchoolName(schoolId):
    schoolRecord = DatabaseController.getSchoolNameBasedOnSchoolId(schoolId)
    oldSchoolName = schoolRecord[0][0]
    locationIdRecord = DatabaseController.getLocationId(schoolId, oldSchoolName)
    return int(locationIdRecord[0][0])

#===== School Opening Hours Processing ==============================================================================================================================
            
# Retrieve the full list of weekdays, a list of opening hours for the school and a list of opening times and return them for rendering in the browser
def getSchoolOpeningHours(schoolId):
    listOfWeekdays = []
    listOfOpeningHours = []
    listOfTimes = []
    weekdayRecords = DatabaseController.getListOfWeekdays()
    for eachRecord in weekdayRecords:
        currentWeekdayRecord = ClassesList.Weekday(int(eachRecord[0]), eachRecord[1])
        listOfWeekdays.append(currentWeekdayRecord)
    openingHoursRecords = DatabaseController.getSchoolOpeningHours(schoolId)
    for eachRecord in openingHoursRecords:
        currentOpeningHoursRecord = ClassesList.OpeningHours(int(eachRecord[0]), int(eachRecord[1]), int(eachRecord[2]), int(eachRecord[3]))
        listOfOpeningHours.append(currentOpeningHoursRecord)
        if currentOpeningHoursRecord.timeId > 0:
            timeRecord = DatabaseController.getTimeRecord(currentOpeningHoursRecord.timeId)
            startTime = str(timeRecord[0][1])
            endTime = str(timeRecord[0][2])
            if endTime == "1 day, 0:00:00":
                endTime = "24:00:00"
            currentTimeRecord = ClassesList.Time(int(timeRecord[0][0]), startTime, endTime)
            listOfTimes.append(currentTimeRecord)
    return [listOfWeekdays, listOfOpeningHours, listOfTimes]

# Update the schools opening hours for every day in the week
def updateSchoolOpeningHours(schoolId, weekdayId, openOrClosed, openingTime, closingTime):
    timeRecord = DatabaseController.getOpeningHoursTimeId(schoolId, weekdayId)
    idRecord = DatabaseController.getOpeningHoursId(schoolId, weekdayId)
    timeValue = int(timeRecord[0][0])
    idValue = int(idRecord[0][0])
    if openOrClosed == "open":
        if timeValue == 0:
            countRecord = DatabaseController.countRecordsInTimeTable()
            countValue = int(countRecord[0][0])
            newTimeId = countValue + 1
            DatabaseController.insertNewTimeRecord(newTimeId, openingTime, closingTime, 0)
            DatabaseController.setOpeningHoursTimeId(idValue, newTimeId)
        else:
            DatabaseController.updateExistingTimeRecord(timeValue, openingTime, closingTime)
    else:
        if timeValue > 0:
            DatabaseController.deleteTimeRecord(timeValue)
            DatabaseController.setOpeningHoursTimeId(idValue, 0)
            DatabaseController.deleteTimetableRecordsByDay(schoolId, weekdayId)

#===== Lesson Details Processing ====================================================================================================================================

# Insert a new lesson record into the database
def insertNewLessonRecord(schoolId, lessonName, abbreviatedName, lessonColour):
    duplicateRecord = DatabaseController.countNumberOfDuplicateLessonNames(lessonName)
    duplicateValue = int(duplicateRecord[0][0])
    if duplicateValue == 0:
        DatabaseController.insertNewLessonRecord(lessonName)
    lessonRecord = DatabaseController.getLessonId(lessonName)
    lessonId = int(lessonRecord[0][0])
    DatabaseController.insertNewSchoolLessonRecord(schoolId, lessonId, abbreviatedName, lessonColour)

# Retrieve a list of the lessons associated with the school id provided
def getSchoolLessonsList(schoolId):
    listOfLessonNames = []
    listOfLessonNameRecords = DatabaseController.getListOfLessonNames(schoolId)
    for eachLesson in listOfLessonNameRecords:
        currentLessonName = ClassesList.LessonName(eachLesson[0])
        listOfLessonNames.append(currentLessonName)
    return listOfLessonNames

# Retrieve the details associated with the selected school
def getSchoolLessonDetails(schoolId, lessonName):
    listOfLessonDetails = []
    lessonRecord = DatabaseController.getListOfLessonDetails(schoolId, lessonName)
    for theLesson in lessonRecord:
        for index in range(0, theLesson.__len__()):
            listOfLessonDetails.append(theLesson[index])
    return listOfLessonDetails
            
# Update an existing lesson record when provided with each of its attributes
def updateLessonRecord(schoolLessonId, schoolId, lessonId, lessonName, abbreviatedName, colour):
    duplicateRecord = DatabaseController.countNumberOfDuplicateLessonNames(lessonName)
    duplicateValue = int(duplicateRecord[0][0])
    if duplicateValue == 0:
        DatabaseController.insertNewLessonRecord(lessonName)
    lessonIdRecord = DatabaseController.getLessonId(lessonName)
    lessonIdValue = int(lessonIdRecord[0][0])
    DatabaseController.updateSchoolLessonRecord(schoolLessonId, schoolId, lessonIdValue, abbreviatedName, colour)
    manageLessonUsage(lessonId)

# Set a lesson record as removed, ie set the deleted flag of the entry in the schoollesson table to 1. Also delete all timetabled lessons matching to this
def deleteLessonRecord(schoolLessonId, lessonId):
    DatabaseController.deleteSchoolLessonRecord(schoolLessonId)
    DatabaseController.deleteTimetableRecordsBasedOnSchoolLessonId(schoolLessonId)
    manageLessonUsage(lessonId)

# Count how many times a lesson is used - if not used, mark it as deleted
def manageLessonUsage(lessonId):
    lessonUsageCounterRecord = DatabaseController.countNumberOfTimesLessonIsUsed(lessonId)
    lessonUsageCounterValue = int(lessonUsageCounterRecord[0][0])
    if lessonUsageCounterValue == 0:
        DatabaseController.deleteLessonById(lessonId)

#===== Student Details Processing ===================================================================================================================================

# Insert the new student record and link it to the current school
def insertNewStudentRecord(schoolId, firstName, surname, dateOfBirth, phoneNumber, emailAddress, streetName1, streetName2, townOrCity, county):
    personId = 0
    addressId = 0
    studentId = 0   
    personIdRecord = DatabaseController.getPersonId(firstName, surname, dateOfBirth, phoneNumber, emailAddress)
    if personIdRecord.__len__() == 0:
        countRecord = DatabaseController.countNumberOfPersonRecords()
        personId = int(countRecord[0][0]) + 1
        DatabaseController.insertNewPersonRecord(personId, firstName, surname, dateOfBirth, phoneNumber, emailAddress)
    else:
        personId = int(personIdRecord[0][0])

    addressIdRecord = DatabaseController.getAddressId(streetName1, streetName2, townOrCity, county)
    if addressIdRecord.__len__() == 0:
        countRecord = DatabaseController.countRecordsInAddressTable()
        addressId = int(countRecord[0][0]) + 1
        DatabaseController.insertNewAddressRecord(addressId, streetName1, streetName2, townOrCity, county)
    else:
        addressId = int(addressIdRecord[0][0])

    studentIdRecord = DatabaseController.getStudentIdFromPersonId(personId)
    if studentIdRecord.__len__() == 0:
        countRecord = DatabaseController.countNumberOfStudentRecords()
        studentId = int(countRecord[0][0]) + 1
        DatabaseController.insertNewStudentRecord(studentId, personId, addressId)
    else:
        studentId = int(studentIdRecord[0][0])
    DatabaseController.insertNewSchoolStudentRecord(schoolId, studentId)

# Get the entire list of students associated with the provided school
def getSchoolStudentsList(schoolId, firstName, surname):
    listOfStudentNamesAndDetails = []
    listOfStudentDetailsAndRecords = DatabaseController.getListOfStudentDetails(schoolId, firstName, surname)
    for eachStudent in listOfStudentDetailsAndRecords:
        for index in range(0, eachStudent.__len__()):
            listOfStudentNamesAndDetails.append(eachStudent[index])
    return listOfStudentNamesAndDetails

# Get the entire list of student names associated with the provided school
def getSchoolStudentsNamesList(schoolId):
    listOfStudentNames = []
    listOfStudentRecords = DatabaseController.getListOfStudentNames(schoolId)
    for eachStudent in listOfStudentRecords:
        currentStudentDetails = ClassesList.PersonName(eachStudent[0], eachStudent[1], eachStudent[2])
        listOfStudentNames.append(currentStudentDetails)
    return listOfStudentNames

# Update an existing student record when provided with each of its attributes
def updateStudentRecord(schoolId, personId, studentId, addressId, firstName, surname, dateOfBirth, phoneNumber, emailAddress, streetName1, streetName2,
                        townOrCity, county):
    duplicateRecord = DatabaseController.countNumberOfDuplicatePersons(firstName, surname, dateOfBirth, phoneNumber, emailAddress)
    duplicateValue = int(duplicateRecord[0][0])
    if duplicateValue == 0:
        countRecord = DatabaseController.countNumberOfPersonRecords()
        newPersonId = int(countRecord[0][0]) + 1
        DatabaseController.insertNewPersonRecord(newPersonId, firstName, surname, dateOfBirth, phoneNumber, emailAddress)
    personIdRecord = DatabaseController.getPersonId(firstName, surname, dateOfBirth, phoneNumber, emailAddress)
    personIdValue = int(personIdRecord[0][0])
    if personIdValue != int(personId):
        DatabaseController.updateStudentPersonId(studentId, personIdValue)
        checkIfPersonIsUsed(personId)

    hasChanged = checkIfAddressHasChanged(addressId, streetName1, streetName2, townOrCity, county)
    if hasChanged == True:
        duplicateRecord = DatabaseController.countNumberOfDuplicateAddresses(streetName1, streetName2, townOrCity, county)
        duplicateValue = int(duplicateRecord[0][0])
        if duplicateValue == 0:
            insertNewAddressRecord(streetName1, streetName2, townOrCity, county)    
        newAddressIdRecord = DatabaseController.getAddressId(streetName1, streetName2, townOrCity, county)
        newAddressId = newAddressIdRecord[0][0]
        DatabaseController.updateStudentAddressId(studentId, newAddressId)
        checkIfAddressIsUsed(addressId)

# Check if the provided person id is still used by any entity in the system
def checkIfPersonIsUsed(personId):
    countRecordA = DatabaseController.countPersonUsageInStudents(personId)
    countRecordB = DatabaseController.countPersonUsageInTeachers(personId)
    countValueA = int(countRecordA[0][0])
    countValueB = int(countRecordB[0][0])
    countTotal = countValueA + countValueB
    if countTotal == 0:
        DatabaseController.deletePersonRecord(personId)
        DatabaseController.deleteAccountRecord(personId)

# Delete the student from the current school and check the students, persons and address usage across the system (deleting those if required)
def deleteStudentRecord(schoolId, personId, studentId, addressId):
    DatabaseController.deleteSchoolStudentRecord(schoolId, studentId)
    countRecord = DatabaseController.countStudentUsageInSchoolStudents(studentId)
    countValue = int(countRecord[0][0])
    if countValue == 0:
        DatabaseController.deleteStudentRecord(studentId)
        checkIfPersonIsUsed(personId)
        checkIfAddressIsUsed(addressId)
    DatabaseController.deleteTimetableRecordsBasedOnSchoolIdAndStudentId(schoolId, studentId)

#===== Teacher Details Processing ===================================================================================================================================

# Insert the new teacher record and link it to the current school
def insertNewTeacherRecord(schoolId, firstName, surname, dateOfBirth, phoneNumber, emailAddress, streetName1, streetName2, townOrCity, county):
    personId = 0
    addressId = 0
    teacherId = 0   
    personIdRecord = DatabaseController.getPersonId(firstName, surname, dateOfBirth, phoneNumber, emailAddress)
    if personIdRecord.__len__() == 0:
        countRecord = DatabaseController.countNumberOfPersonRecords()
        personId = int(countRecord[0][0]) + 1
        DatabaseController.insertNewPersonRecord(personId, firstName, surname, dateOfBirth, phoneNumber, emailAddress)
    else:
        personId = int(personIdRecord[0][0])

    addressIdRecord = DatabaseController.getAddressId(streetName1, streetName2, townOrCity, county)
    if addressIdRecord.__len__() == 0:
        countRecord = DatabaseController.countRecordsInAddressTable()
        addressId = int(countRecord[0][0]) + 1
        DatabaseController.insertNewAddressRecord(addressId, streetName1, streetName2, townOrCity, county)
    else:
        addressId = int(addressIdRecord[0][0])

    teacherIdRecord = DatabaseController.getTeacherIdFromPersonId(personId)
    if teacherIdRecord.__len__() == 0:
        countRecord = DatabaseController.countNumberOfTeacherRecords()
        teacherId = int(countRecord[0][0]) + 1
        DatabaseController.insertNewTeacherRecord(teacherId, personId, addressId)
    else:
        teacherId = int(teacherIdRecord[0][0])
    DatabaseController.insertNewSchoolTeacherRecord(schoolId, teacherId)

# Get the entire list of teacher names associated with the provided school
def getSchoolTeachersNamesList(schoolId):
    listOfTeacherNames = []
    listOfTeacherRecords = DatabaseController.getListOfTeacherNames(schoolId)
    for eachTeacher in listOfTeacherRecords:
        currentTeacherDetails = ClassesList.PersonName(eachTeacher[0], eachTeacher[1], eachTeacher[2])
        listOfTeacherNames.append(currentTeacherDetails)
    return listOfTeacherNames

# Get the entire list of teachers associated with the provided school
def getSchoolTeachersList(schoolId, firstName, surname):
    listOfTeacherNamesAndDetails = []
    listOfTeacherDetailsAndRecords = DatabaseController.getListOfTeacherDetails(schoolId, firstName, surname)
    for eachTeacher in listOfTeacherDetailsAndRecords:
        for index in range(0, eachTeacher.__len__()):
            listOfTeacherNamesAndDetails.append(eachTeacher[index])
    return listOfTeacherNamesAndDetails

# Update an existing teacher record when provided with each of its attributes
def updateTeacherRecord(schoolId, personId, teacherId, addressId, firstName, surname, dateOfBirth, phoneNumber, emailAddress, streetName1, streetName2,
                        townOrCity, county):
    duplicateRecord = DatabaseController.countNumberOfDuplicatePersons(firstName, surname, dateOfBirth, phoneNumber, emailAddress)
    duplicateValue = int(duplicateRecord[0][0])
    if duplicateValue == 0:
        countRecord = DatabaseController.countNumberOfPersonRecords()
        newPersonId = int(countRecord[0][0]) + 1
        DatabaseController.insertNewPersonRecord(newPersonId, firstName, surname, dateOfBirth, phoneNumber, emailAddress)
    personIdRecord = DatabaseController.getPersonId(firstName, surname, dateOfBirth, phoneNumber, emailAddress)
    personIdValue = int(personIdRecord[0][0])
    if personIdValue != int(personId):
        DatabaseController.updateTeacherPersonId(teacherId, personIdValue)
        checkIfPersonIsUsed(personId)

    hasChanged = checkIfAddressHasChanged(addressId, streetName1, streetName2, townOrCity, county)
    if hasChanged == True:
        duplicateRecord = DatabaseController.countNumberOfDuplicateAddresses(streetName1, streetName2, townOrCity, county)
        duplicateValue = int(duplicateRecord[0][0])
        if duplicateValue == 0:
            insertNewAddressRecord(streetName1, streetName2, townOrCity, county)
        newAddressIdRecord = DatabaseController.getAddressId(streetName1, streetName2, townOrCity, county)
        newAddressId = int(newAddressIdRecord[0][0])
        DatabaseController.updateTeacherAddressId(teacherId, newAddressId)
        checkIfAddressIsUsed(addressId)

# Delete the teacher from the current school and check the teachers, persons and address usage across the system (deleting those if required)
def deleteTeacherRecord(schoolId, personId, teacherId, addressId):
    DatabaseController.deleteSchoolTeacherRecord(schoolId, teacherId)
    DatabaseController.deleteTimetableRecordsBasedOnSchoolIdAndTeacherId(schoolId, teacherId)
    countRecord = DatabaseController.countTeacherUsageInSchoolTeachers(teacherId)
    countValue = int(countRecord[0][0])
    if countValue == 0:
        DatabaseController.deleteTeacherRecord(teacherId)
        checkIfPersonIsUsed(personId)
        checkIfAddressIsUsed(addressId)

#===== Classrooms Processing ========================================================================================================================================

# Insert a new classroom record and link it to the current location
def insertNewClassroomRecord(locationId, roomName):
    classroomIdRecord = DatabaseController.getClassroomIdFromRoomName(roomName)
    if classroomIdRecord.__len__() == 0:
        DatabaseController.insertNewClassroomRecord(roomName)
        classroomIdRecord = DatabaseController.getClassroomIdFromRoomName(roomName)
    classroomId = int(classroomIdRecord[0][0])
    DatabaseController.insertNewClassroomLocationRecord(locationId, classroomId)

# Retrieve the full list of classrooms for the provided location
def getLocationClassroomsList(locationId):
    listOfClassrooms = []
    listOfClassroomRecords = DatabaseController.getListOfClassrooms(locationId)
    for eachRoom in listOfClassroomRecords:
        for index in range(0, eachRoom.__len__()):
            listOfClassrooms.append(eachRoom[index])
    return listOfClassrooms

# Update an edited classroom record
def updateEditedClassroomRecord(oldLocationId, newLocationId, classroomId, roomName):
    existingClassroomRecord = DatabaseController.getClassroomNameBasedOnIdAndLocation(oldLocationId, classroomId)
    if existingClassroomRecord[0][0] == roomName:
        DatabaseController.updateClassroomLocationId(oldLocationId, newLocationId, classroomId)
    else:
        duplicateCountRecord = DatabaseController.countDuplicateClassroomNames(roomName)
        duplicateCount = int(duplicateCountRecord[0][0])
        if duplicateCount == 0:
            DatabaseController.insertNewClassroomRecord(roomName)
        newClassroomIdRecord = DatabaseController.getClassroomIdBasedOnName(roomName)
        newClassroomId = int(newClassroomIdRecord[0][0])
        DatabaseController.updateClassroomLocationAndRoomId(oldLocationId, newLocationId, classroomId, newClassroomId)
        manageClassroomUsage(classroomId)

# Check if an existing classroom is used any more
def manageClassroomUsage(classroomId):
    usageCountRecord = DatabaseController.countClassroomIdUsage(classroomId)
    usageCount = int(usageCountRecord[0][0])
    if usageCount == 0:
        DatabaseController.deleteClassroomRecord(classroomId)

# Delete the selected classroom from the system
def deleteClassroomRecord(locationId, classroomId):
    DatabaseController.deleteClassroomLocationRecord(locationId, classroomId)
    classroomLocationIdRecord = DatabaseController.getClassroomLocationIdBasedOnLocationIdAndClassroomId(locationId, classroomId)
    classroomLocationId = int(classroomLocationIdRecord[0][0])
    DatabaseController.deleteTimetableRecordsBasedOnClassroomLocationId(classroomLocationId)
    manageClassroomUsage(classroomId)

#===== Timetable Details Processing =================================================================================================================================

# Retrieve a list of students and student ids for selection
def getListOfStudentNamesAndIds(schoolId, firstName, surname):
    listOfNamesAndIds = DatabaseController.getSchoolStudentsNamesAndIds(schoolId, firstName, surname)
    return listOfNamesAndIds

# Retrieve a list of lessons associated with the school id provided - this method returns all details
def getSchoolFullLessonDetailsList(schoolId):
    listOfLessonDetails = []
    listOfLessonDetailsRecords = DatabaseController.getListOfFullLessonDetails(schoolId)
    for eachLesson in listOfLessonDetailsRecords:
        currentLesson = ClassesList.FullLesson(int(eachLesson[0]), eachLesson[1], eachLesson[2], eachLesson[3])
        listOfLessonDetails.append(currentLesson)
    return listOfLessonDetails

# Retrieve the list of teachers (and their id's) associated with the provided school
def getSchoolTeacherIdAndNamesList(schoolId):
    listOfTeacherIdsAndNames = []
    listOfTeacherRecords = DatabaseController.getListOfTeacherIdsAndNames(schoolId)
    for eachTeacher in listOfTeacherRecords:
        currentTeacher = ClassesList.TeacherIdAndName(int(eachTeacher[0]), eachTeacher[1], eachTeacher[2])
        listOfTeacherIdsAndNames.append(currentTeacher)
    return listOfTeacherIdsAndNames

# Retrieve the list of classrooms and their locations associated with the provided school
def getSchoolClassroomNamesAndLocations(schoolId):
    listOfClassroomsAndLocations = []
    listOfClassroomRecords = DatabaseController.getListOfClassroomIdsNamesAndLocations(schoolId)
    for eachRoom in listOfClassroomRecords:
        currentRoom = ClassesList.TimetabledClassroom(int(eachRoom[0]), eachRoom[1], int(eachRoom[2]), eachRoom[3])
        listOfClassroomsAndLocations.append(currentRoom)
    return listOfClassroomsAndLocations

# Update the timetable with the current state of scheduled lessons
def updateTimetable(listOfTimetableData):
    if listOfTimetableData.__len__() > 0:
        schoolId = int(listOfTimetableData[4])
        studentId = int(listOfTimetableData[5])
        listOfStoredRecords = DatabaseController.getStudentTimetable(schoolId, studentId)
        currentStateIndex = 0
        storedStateIndex = 0
        while currentStateIndex < listOfTimetableData.__len__():
            weekdayId = int(listOfTimetableData[currentStateIndex])
            startHour = int(listOfTimetableData[currentStateIndex + 1])
            startMin = int(listOfTimetableData[currentStateIndex + 2])
            lessonLength = int(listOfTimetableData[currentStateIndex + 3])
            schoolLessonId = int(listOfTimetableData[currentStateIndex + 6])
            teacherId = int(listOfTimetableData[currentStateIndex + 7])
            locationId = int(listOfTimetableData[currentStateIndex + 8])
            classroomId = int(listOfTimetableData[currentStateIndex + 9])

            # Determine the endHour for the lesson and the classroomLocationId
            endMinutes = startMin + lessonLength
            additionalHours = 0
            while endMinutes > 60:
                additionalHours += 1
                endMinutes -= 60
            endHour = int(startHour + additionalHours)
            classroomLocationIdRecord = DatabaseController.getClassroomLocationIdBasedOnLocationIdAndClassroomId(locationId, classroomId)
            classroomLocationId = int(classroomLocationIdRecord[0][0])
            
            # Overwrite an existing timetable entry or insert a brand new one if required
            if storedStateIndex < listOfStoredRecords.__len__():
                existingRecordId = int(listOfStoredRecords[storedStateIndex][0])
                DatabaseController.updateExistingTimetableRecord(existingRecordId, weekdayId, startHour, startMin, lessonLength, endHour, schoolLessonId,
                                                                 teacherId, locationId, classroomLocationId)
                storedStateIndex += 1
            else:
                maxCountRecord = DatabaseController.countNumberOfTimetableRecords()
                maxCount = int(maxCountRecord[0][0])
                newRecordId = maxCount + 1
                DatabaseController.insertNewTimetableRecord(newRecordId, weekdayId, startHour, startMin, lessonLength, endHour, schoolLessonId, schoolId, studentId,
                                                            teacherId, locationId, classroomLocationId)
            currentStateIndex += 10

        # If there are any remaining existing lessons after all updates are complete - remove them
        while storedStateIndex < listOfStoredRecords.__len__():
            existingRecordId = int(listOfStoredRecords[storedStateIndex][0])
            DatabaseController.deleteTimetableRecord(existingRecordId)
            storedStateIndex += 1
    else:
        # No lessons currently on the timetable - delete all of the records stored in the database
        schoolId = session.get("loginId")
        studentId = session.get("studentId")
        listOfStoredRecords = DatabaseController.getStudentTimetable(schoolId, studentId)
        for eachRecord in listOfStoredRecords:
            existingRecordId = int(eachRecord[0])
            DatabaseController.deleteTimetableRecord(existingRecordId)

# Retrieve the list of all timetabled lessons for this student in this school
def getStudentTimetable(schoolId, studentId):
    listOfTimetabledLessons = []
    listOfStoredRecords = DatabaseController.getStudentTimetable(schoolId, studentId)
    for eachRecord in listOfStoredRecords:
        classroomLocationId = int(eachRecord[10])
        classroomIdRecord = DatabaseController.getClassroomIdFromClassroomLocationId(classroomLocationId)
        classroomId = int(classroomIdRecord[0][0])
        currentLesson = ClassesList.TimetabledLesson(int(eachRecord[0]), int(eachRecord[1]), int(eachRecord[2]), int(eachRecord[3]), int(eachRecord[4]),
                                                     int(eachRecord[5]), int(eachRecord[6]), int(eachRecord[7]), int(eachRecord[8]), int(eachRecord[9]),
                                                     classroomId)
        listOfTimetabledLessons.append(currentLesson)
    return listOfTimetabledLessons

# Delete all timetabled records that are now outside of the schools opening hours
def deleteTimetableRecordsOutsideSchoolHours(schoolId, startHour, endHour):
    DatabaseController.deleteTimetableRecordsBeforeSchoolStart(schoolId, startHour)
    DatabaseController.deleteTimetableRecordsAfterSchoolEnd(schoolId, endHour)

# Retrieve the classroom location id for timetabling
def getClassroomLocationIdForTimetable(locationId, classroomId):
    classroomLocationIdRecord = DatabaseController.getClassroomLocationIdBasedOnLocationIdAndClassroomId(locationId, classroomId)
    return int(classroomLocationIdRecord[0][0])

# Retrieve a schools opening hours and open days for timetabling
def getSchoolOpenDaysAndTimesDetails(schoolId):
    schoolHoursList = getSchoolOpeningHours(schoolId)
    openingDaysAndTimes = schoolHoursList[1]
    openingTimes = schoolHoursList[2]

    dayHoursAndIndexes = determineTimetabledHoursAndIndexes(openingDaysAndTimes, openingTimes)
    listOfOpenDayIndexes = dayHoursAndIndexes[0]
    earliestStartTime = dayHoursAndIndexes[1]
    latestEndTime = dayHoursAndIndexes[2]

    return [listOfOpenDayIndexes, earliestStartTime, latestEndTime, openingDaysAndTimes, openingTimes]

# Retrieve a persons general opening hours and open days based on their respective schools hours and days
def getGeneralOpenDaysAndTimesDetails(personId, personType):
    openingDaysAndTimes = []
    openingTimes = []

    listOfSchools = []
    if personType == "Teacher":
        listOfSchools = DatabaseController.getTeacherSchoolsList(personId)
    elif personType == "Student":
        listOfSchools = DatabaseController.getStudentSchoolsList(personId)

    allSchoolDetailsList = []
    for eachSchool in listOfSchools:
        allSchoolDetailsList.append(getSchoolOpeningHours(eachSchool[0]))

    index = 0
    while index < allSchoolDetailsList.__len__():
        if index == 0:
            openingDaysAndTimes = allSchoolDetailsList[index][1]
            openingTimes = allSchoolDetailsList[index][2]
        else:
            openingDaysAndTimesAtIndex = allSchoolDetailsList[index][1]
            openingTimesAtIndex = allSchoolDetailsList[index][2]
            for innerIndex in range(0, 7):
                storedTimeId = openingDaysAndTimes[innerIndex].timeId
                currentTimeId = openingDaysAndTimesAtIndex[innerIndex].timeId

                # Only perform checks if there is a time id to compare against
                if currentTimeId > 0:
                    if storedTimeId == 0:
                        # No previous record stored for this weekday - add it to the openingTimes list
                        openingDaysAndTimes[innerIndex].timeId = openingDaysAndTimesAtIndex[innerIndex].timeId
                        timeIndex = 0
                        foundTime = False
                        while timeIndex < openingTimesAtIndex.__len__() and foundTime == False:
                            if openingTimesAtIndex[timeIndex].timeId == currentTimeId:
                                openingTimes.append(openingTimesAtIndex[timeIndex])
                                foundTime = True
                            timeIndex += 1
                    else:
                        # Get the time object matched to both the stored day and the current day to be compared 
                        timeIndex = 0
                        foundTime = False
                        while timeIndex < openingTimes.__len__() and foundTime == False:
                            if storedTimeId == openingTimes[timeIndex].timeId:
                                storedTimeObject = openingTimes[timeIndex]
                                foundTime = True
                            timeIndex += 1

                        timeIndex = 0
                        foundTime = False
                        while timeIndex < openingTimesAtIndex.__len__() and foundTime == False:
                            if currentTimeId == openingTimesAtIndex[timeIndex].timeId:
                                currentTimeObject = openingTimesAtIndex[timeIndex]
                                foundTime = True
                            timeIndex += 1

                        # Compare the times of each object - set the earliest start time and latest end time if required
                        storedStartTime = int(storedTimeObject.startTime[0:storedTimeObject.startTime.index(":")])
                        storedEndTime = int(storedTimeObject.endTime[0:storedTimeObject.endTime.index(":")])
                        currentStartTime = int(currentTimeObject.startTime[0:currentTimeObject.startTime.index(":")])
                        currentEndTime = int(currentTimeObject.endTime[0:storedTimeObject.endTime.index(":")])

                        if storedStartTime > currentStartTime:
                            storedTimeObject.startTime = currentTimeObject.startTime
                        if storedEndTime < currentEndTime:
                            storedTimeObject.endTime = currentTimeObject.endTime
        index += 1

    # Now determine the earliest start time, the latest end time and the list of open day indexes
    dayHoursAndIndexes = determineTimetabledHoursAndIndexes(openingDaysAndTimes, openingTimes)
    listOfOpenDayIndexes = dayHoursAndIndexes[0]
    earliestStartTime = dayHoursAndIndexes[1]
    latestEndTime = dayHoursAndIndexes[2]

    return [listOfOpenDayIndexes, earliestStartTime, latestEndTime, openingDaysAndTimes, openingTimes]

# Determine a list of day indexes, the days earliest start time and the days latest end time
def determineTimetabledHoursAndIndexes(openingDaysAndTimes, openingTimes):
    listOfIndexes = []
    earliestStartTime = -1
    latestEndTime = -1
    for eachDay in openingDaysAndTimes:
        if eachDay.timeId > 0:
            if int(eachDay.weekdayId) not in listOfIndexes:
                listOfIndexes.append(int(eachDay.weekdayId))
            currentTimeId = int(eachDay.timeId)
            index = 0
            foundTime = False
            while index < openingTimes.__len__() and foundTime == False:
                if int(openingTimes[index].timeId) == currentTimeId:
                    dayStartString = str(openingTimes[index].startTime)
                    dayEndString = str(openingTimes[index].endTime)
                    dayStart = int(dayStartString[0:dayStartString.index(":")])
                    dayEnd = int(dayEndString[0:dayEndString.index(":")])
                    if earliestStartTime == -1 and latestEndTime == -1:
                        earliestStartTime = dayStart
                        latestEndTime = dayEnd
                    if dayStart < earliestStartTime:
                        earliestStartTime = dayStart
                    if dayEnd > latestEndTime:
                        latestEndTime = dayEnd
                    foundTime = True
                index += 1
    listOfIndexes.sort()
    return [listOfIndexes, earliestStartTime, latestEndTime]

# Retrieve a classroom timetable
def getClassroomTimetable(classroomLocationId):
    listOfTimetabledLessons = []
    listOfStoredRecords = DatabaseController.getClassroomLocationTimetable(classroomLocationId)
    for eachRecord in listOfStoredRecords:
        schoolLessonId = int(eachRecord[7])
        abbreviatedNameRecord = DatabaseController.getLessonAbbreviatedNameBasedOnSchoolLessonId(schoolLessonId)
        abbreviatedName = abbreviatedNameRecord[0][0]
        currentLesson = ClassesList.TimetabledLesson(int(eachRecord[0]), int(eachRecord[1]), int(eachRecord[2]), int(eachRecord[3]), int(eachRecord[4]),
                                                     int(eachRecord[5]), int(eachRecord[6]), abbreviatedName, int(eachRecord[8]), int(eachRecord[9]),
                                                     eachRecord[10])
        listOfTimetabledLessons.append(currentLesson)
    return listOfTimetabledLessons

# Retrieve a teachers individual school timetable
def getTeacherSchoolTimetable(schoolId, teacherId):
    listOfStoredRecords = DatabaseController.getTeacherSchoolTimetable(schoolId, teacherId)
    listOfTimetabledLessons = buildSchoolTimetableData(listOfStoredRecords)
    return listOfTimetabledLessons

# Retrieve a teachers timetable across all schools
def getTeacherAllTimetable(teacherId):
    listOfStoredRecords = DatabaseController.getTeacherAllTimetable(teacherId)
    listOfTimetabledLessons = buildSchoolTimetableData(listOfStoredRecords)
    return listOfTimetabledLessons

# Retrieve a students individual school timetable
def getStudentSchoolTimetable(schoolId, studentId):
    listOfStoredRecords = DatabaseController.getStudentSchoolTimetable(schoolId, studentId)
    listOfTimetabledLessons = buildSchoolTimetableData(listOfStoredRecords)
    return listOfTimetabledLessons

# Retrieve a students timetable across all schools
def getStudentAllTimetable(studentId):
    listOfStoredRecords = DatabaseController.getStudentAllTimetable(studentId)
    listOfTimetabledLessons = buildSchoolTimetableData(listOfStoredRecords)
    return listOfTimetabledLessons

# Build the list of data for the student/teacher school timetables
def buildSchoolTimetableData(listOfRecords):
    listOfLessons = []
    for eachRecord in listOfRecords:
        classroomLocationId = int(eachRecord[10])
        classroomNameRecord = DatabaseController.getClassroomNameBasedOnClassroomLocationId(classroomLocationId)
        classroomName = classroomNameRecord[0][0]

        schoolLessonId = int(eachRecord[7])
        abbreviatedNameRecord = DatabaseController.getLessonAbbreviatedNameBasedOnSchoolLessonId(schoolLessonId)
        abbreviatedName = abbreviatedNameRecord[0][0]
        
        currentLesson = ClassesList.TimetabledLesson(int(eachRecord[0]), int(eachRecord[1]), int(eachRecord[2]), int(eachRecord[3]), int(eachRecord[4]),
                                                     int(eachRecord[5]), int(eachRecord[6]), abbreviatedName, int(eachRecord[8]), int(eachRecord[9]),
                                                     classroomName)
        listOfLessons.append(currentLesson)
    return listOfLessons
    
