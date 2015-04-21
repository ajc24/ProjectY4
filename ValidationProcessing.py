#   Student Name:   Anthony Cox
#   Student ID:     C00162988
#   Date:           11th March 2015
#   Purpose:        This file performs further validation on user entries from the UI on server side. These validations
#                   are largely database-oriented - ie, checking if a new entry is a duplicate etc

import DatabaseController
import ClassesList

#===== School Details Validation ====================================================================================================================================

# Check if the proposed school email address has changed - returns false if it hasn't changed and true if it has changed
def checkIfSchoolEmailHasChanged(schoolId, emailAddress):
    countRecord = DatabaseController.checkIfExistingSchoolEmail(schoolId, emailAddress)
    countValue = int(countRecord[0][0])
    if countValue == 1:
        return False
    else:
        return True

# Check if the proposed school email address is a duplicate of another email address already in the system
def checkIfSchoolEmailIsDuplicate(emailAddress):
    countRecord = DatabaseController.checkIfDuplicateSchoolEmail(emailAddress)
    countValue = int(countRecord[0][0])
    if countValue == 0:
        return False
    else:
        return True

#===== Location Details Validation ==================================================================================================================================

# Check if the new school location name is a duplicate
def checkIfLocationNameIsADuplicate(schoolId, locationName):
    countRecord = DatabaseController.checkIfDuplicateLocationName(schoolId, locationName)
    countValue = int(countRecord[0][0])
    if countValue == 0:
        return False
    else:
        return True

# Check if the edited school location name is a duplicate
def checkIfEditedLocationNameIsADuplicate(schoolId, locationId, locationName):
    countRecord = DatabaseController.checkIfDuplicateEditedName(schoolId, locationId, locationName)
    countValue = int(countRecord[0][0])
    if countValue == 0:
        return False
    else:
        return True

#===== Account Details Validation ===================================================================================================================================

# Check if the current password matches to the account password stored for the current school
def checkIfCurrentSchoolPasswordIsCorrect(schoolId, currentPassword):
    accountPasswordRecord = DatabaseController.getAccountPasswordBasedOnSchoolId(schoolId)
    accountPassword = accountPasswordRecord[0][0]
    if currentPassword == accountPassword:
        return True
    else:
        return False

# Check if the current password matches to the account password stored for the person
def checkIfCurrentPersonPasswordIsCorrect(personId, accountType, currentPassword):
    accountPasswordRecord = DatabaseController.getAccountPasswordBasedOnPersonIdAndType(personId, accountType)
    accountPassword = accountPasswordRecord[0][0]
    if currentPassword == accountPassword:
        return True
    else:
        return False

#===== Lesson Details Validation ====================================================================================================================================

# Check if the proposed lesson entry is unique for the current school
def checkIfLessonEntryIsUnique(schoolId, lessonName):
    countRecord = DatabaseController.countNumberOfDuplicateLessons(schoolId, lessonName)
    countValue = int(countRecord[0][0])
    if countValue == 0:
        return True
    else:
        return False

# Check if the edited lesson name is different from its original lesson name
def checkIfLessonNameHasChanged(schoolLessonId, lessonName):
    originalNameRecord = DatabaseController.getLessonNameBySchoolLessonId(schoolLessonId)
    originalName = originalNameRecord[0][0]
    if originalName == lessonName:
        return False
    else:
        return True

#===== Person Details Validation (General) ==========================================================================================================================

# Check if the edited person details are different from the original person details stored
def checkIfPersonHasChanged(personId, firstName, surname, dateOfBirth, phoneNumber, emailAddress):
    originalRecord = DatabaseController.getPersonDetailsByPersonId(personId)
    originalPerson = ClassesList.Person(originalRecord[0][0], originalRecord[0][1], originalRecord[0][2], originalRecord[0][3], originalRecord[0][4])
    editedPerson = ClassesList.Person(firstName, surname, dateOfBirth, phoneNumber, emailAddress)
    if originalPerson.__eq__(editedPerson) == True:
        return False
    else:
        return True

# Check if the proposed email address is a duplicate of another persons email address already in the system (very general check)
def checkIfPersonEmailIsDuplicate(emailAddress):
    countRecord = DatabaseController.countNumberOfDuplicatePersonEmailAddresses(emailAddress)
    countValue = int(countRecord[0][0])
    if countValue == 0:
        return False
    else:
        return True

# Check that the commonly used person entry email address is unique (used to check if teachers or students addresses are unique)
def checkIfCommonPersonEmailIsDuplicate(firstName, surname, dateOfBirth, phoneNumber, emailAddress):
    idRecord = DatabaseController.getPersonId(firstName, surname, dateOfBirth, phoneNumber, emailAddress)
    if idRecord.__len__() == 0:
        isDuplicate = checkIfPersonEmailIsDuplicate(emailAddress)
        return isDuplicate
    return False

# Check if the persons email address has been edited
def checkIfPersonEmailHasChanged(personId, emailAddress):
    oldEmailAddressRecord = DatabaseController.getPersonEmailAddressBasedOnId(personId)
    oldEmailAddress = oldEmailAddressRecord[0][0]
    if emailAddress == oldEmailAddress:
        return False
    else:
        return True

#===== Student Details Validation ===================================================================================================================================

# Check that the new student entry is unique (ie has not been entered before into the system)
def checkIfStudentIsUnique(schoolId, firstName, surname, dateOfBirth, phoneNumber, emailAddress):
    idRecord = DatabaseController.getPersonId(firstName, surname, dateOfBirth, phoneNumber, emailAddress)
    if idRecord.__len__() == 0:
        return True
    else:
        personId = int(idRecord[0][0])
        studentRecord = DatabaseController.getStudentIdFromPersonId(personId)
        if studentRecord.__len__() == 0:
            return True
        studentId = int(studentRecord[0][0])
        countRecord = DatabaseController.countMatchingSchoolStudentRecords(schoolId, studentId)
        countValue = int(countRecord[0][0])
        if countValue == 0:
            return True
        else:
            return False

#===== Teacher Details Validation ===================================================================================================================================

# Check that the new teacher entry is unique (ie has not been entered before into the system)
def checkIfTeacherIsUnique(schoolId, firstName, surname, dateOfBirth, phoneNumber, emailAddress):
    idRecord = DatabaseController.getPersonId(firstName, surname, dateOfBirth, phoneNumber, emailAddress)
    if idRecord.__len__() == 0:
        return True
    else:
        personId = int(idRecord[0][0])
        teacherRecord = DatabaseController.getTeacherIdFromPersonId(personId)
        if teacherRecord.__len__() == 0:
            return True
        teacherId = int(teacherRecord[0][0])
        countRecord = DatabaseController.countMatchingSchoolTeacherRecords(schoolId, teacherId)
        countValue = int(countRecord[0][0])
        if countValue == 0:
            return True
        else:
            return False

#===== Classroom Details Validation =================================================================================================================================

# Check that the new/edited classroom entry is unique
def checkIfClassroomIsUnique(locationId, roomName):
    classroomIdRecord = DatabaseController.getClassroomIdFromRoomName(roomName)
    if classroomIdRecord.__len__() == 0:
        return True
    classroomId = int(classroomIdRecord[0][0])
    existingCountRecord = DatabaseController.countDuplicateClassroomLocationRecords(locationId, classroomId)
    existingCount = int(existingCountRecord[0][0])
    if existingCount == 0:
        return True
    else:
        return False

#===== Timetable Details Validation =================================================================================================================================

# Verify that the proposed lesson time is unique for this student
def verifyIfLessonTimeIsUnique(schoolId, studentId, weekdayId, schoolLessonId, lessonStartTime, lessonEndTime, startHour, endHour, startMin, timetableStartHour):
    allLessonsRecord = DatabaseController.getStudentLessonsWithinTimeSlot(schoolId, studentId, weekdayId, startHour, endHour)
    errorString = ""
    for eachLesson in allLessonsRecord:
        nextStartHour = int(eachLesson[0])
        nextStartMin = int(eachLesson[1])
        nextLessonLength = int(eachLesson[2])

        nextStartTime = ((nextStartHour - timetableStartHour) * 60) + nextStartMin
        nextEndTime = nextStartTime + nextLessonLength

        lessonClash = checkIfLessonsAreCollidingInTimeFrame(lessonStartTime, lessonEndTime, nextStartTime, nextEndTime)
        
        # If lessons collide - process the error message
        if lessonClash == True:
            currentErrorMessage = ""
            weekdayNameRecord = DatabaseController.getWeekdayNameById(weekdayId)
            weekdayName = weekdayNameRecord[0][0]
            lessonNameRecord = DatabaseController.getLessonAbbreviatedNameBasedOnSchoolLessonId(schoolLessonId)
            lessonName = lessonNameRecord[0][0]

            currentErrorMessage = "Cannot schedule lesson '" + lessonName + "' on " + weekdayName + " at "
            if startHour < 10:
                currentErrorMessage += "0" + str(startHour) + ":"
            else:
                currentErrorMessage += str(startHour) + ":"
            if startMin < 10:
                currentErrorMessage += "0" + str(startMin) + ".\n"
            else:
                currentErrorMessage += str(startMin) + ".\n"
            currentErrorMessage += "This lessons duration clashes with another lesson scheduled to this student by another school.\n\n" 
            errorString += currentErrorMessage
    return errorString

# Verify that the teacher is available at the time slot allocated for the current lesson
def verifyIfTeacherIsFreeAtThisTime(teacherId, weekdayId, studentId, lessonStartTime, lessonEndTime, startHour, endHour, startMin, timetableStartHour):
    allTeacherLessons = DatabaseController.getTeacherLessonsWithinTimeSlot(teacherId, weekdayId, studentId, startHour, endHour)
    errorString = ""
    for eachLesson in allTeacherLessons:
        nextStartHour = int(eachLesson[0])
        nextStartMin = int(eachLesson[1])
        nextLessonLength = int(eachLesson[2])

        nextStartTime = ((nextStartHour - timetableStartHour) * 60) + nextStartMin
        nextEndTime = nextStartTime + nextLessonLength

        lessonClash = checkIfLessonsAreCollidingInTimeFrame(lessonStartTime, lessonEndTime, nextStartTime, nextEndTime)

        # If lessons collide - process the error message
        if lessonClash == True:
            currentErrorMessage = ""
            weekdayNameRecord = DatabaseController.getWeekdayNameById(weekdayId)
            weekdayName = weekdayNameRecord[0][0]
            teacherNameRecord = DatabaseController.getPersonNameBasedOnTeacherId(teacherId)
            teacherFirstName = teacherNameRecord[0][0]
            teacherSurname = teacherNameRecord[0][1]

            currentErrorMessage = "Cannot schedule " + teacherFirstName[0:1] + ". " + teacherSurname + " on " + weekdayName + " at "
            if startHour < 10:
                currentErrorMessage += "0" + str(startHour) + ":"
            else:
                currentErrorMessage += str(startHour) + ":"
            if startMin < 10:
                currentErrorMessage += "0" + str(startMin) + ".\n"
            else:
                currentErrorMessage += str(startMin) + ".\n"
            currentErrorMessage += "This teacher has already been scheduled elsewhere during this lessons time frame.\n\n"
            errorString += currentErrorMessage
    return errorString

# Verify that the classroom is available at the time slot allocated for the current lesson
def verifyIfClassroomIsFreeAtThisTime(schoolId, weekdayId, studentId, locationId, classroomId, lessonStartTime, lessonEndTime, startHour,
                                      endHour, startMin, timetableStartHour):
    classroomLocationIdRecord = DatabaseController.getClassroomLocationIdBasedOnLocationIdAndClassroomId(locationId, classroomId)
    classroomLocationId = int(classroomLocationIdRecord[0][0])
    allClassroomLessons = DatabaseController.getClassroomLessonsWithinTimeSlot(classroomLocationId, weekdayId, studentId, startHour, endHour)
    errorString = ""
    for eachLesson in allClassroomLessons:
        nextStartHour = int(eachLesson[0])
        nextStartMin = int(eachLesson[1])
        nextLessonLength = int(eachLesson[2])

        nextStartTime = ((nextStartHour - timetableStartHour) * 60) + nextStartMin
        nextEndTime = nextStartTime + nextLessonLength

        lessonClash = checkIfLessonsAreCollidingInTimeFrame(lessonStartTime, lessonEndTime, nextStartTime, nextEndTime)

        # If lessons collide - process the error message
        if lessonClash == True:
            currentErrorMessage = ""
            weekdayNameRecord = DatabaseController.getWeekdayNameById(weekdayId)
            weekdayName = weekdayNameRecord[0][0]
            classroomNameRecord = DatabaseController.getClassroomNameBasedOnIdAndLocation(locationId, classroomId)
            classroomName = classroomNameRecord[0][0]
    
            currentErrorMessage = "The lesson scheduled on " + weekdayName + " at "
            if startHour < 10:
                currentErrorMessage += "0" + str(startHour) + ":"
            else:
                currentErrorMessage += str(startHour) + ":"
            if startMin < 10:
                currentErrorMessage += "0" + str(startMin) + " "
            else:
                currentErrorMessage += str(startMin) + " "
            currentErrorMessage += "cannot be scheduled.\n"
            currentErrorMessage += "The classroom " + classroomName + " is unavailable during this lessons time frame.\n\n"
            errorString += currentErrorMessage
    return errorString
                                                                               

# Check if lesson times are colliding between two time frames provided
def checkIfLessonsAreCollidingInTimeFrame(lessonStartTime, lessonEndTime, nextStartTime, nextEndTime):
    collisionsFound = False

    if lessonStartTime == nextStartTime or lessonEndTime == nextEndTime:
        collisionsFound = True
    elif lessonStartTime < nextStartTime:
        if lessonEndTime > nextEndTime:
            collisionsFound = True
        elif lessonEndTime > nextStartTime:
            collisionsFound = True
    elif nextStartTime < lessonStartTime:
        if nextEndTime > lessonEndTime:
            collisionsFound = True
        elif nextEndTime > lessonStartTime:
            collisionsFound = True

    return collisionsFound
