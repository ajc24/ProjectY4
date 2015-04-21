#   Student Name:   Anthony Cox
#   Student ID:     C00162988
#   Date:           9th February 2015
#   Purpose:        This file manages all database actions and SQL statements. Data can be inserted, updated, selected and deleted from
#                   the database using the methods in this file.

from DatabaseConnector import DatabaseConnection

#===== School Table SQLs ============================================================================================================================================

# Retrieve the name of the school from the database based on its id
def getSchoolNameBasedOnSchoolId(schoolId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT name
                 FROM school
                 WHERE id = %s"""
        cursor.execute(SQL, (schoolId, ))
        nameRetrieved = cursor.fetchall()
    return nameRetrieved

# Retrieve the list of all school details from the database
def getSchoolDetails(schoolId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT school.id, name, school.addressId, streetName1, streetName2, townOrCity, county, phoneNumber, emailAddress
                 FROM school
                 INNER JOIN address ON address.id = school.addressId
                 WHERE school.id = %s"""
        cursor.execute(SQL, (schoolId, ))
        detailsRetrieved = cursor.fetchall()
    return detailsRetrieved

# Check if the email for the school is already stored - returns a count of 1 if it is stored already, 0 otherwise
def checkIfExistingSchoolEmail(schoolId, emailAddress):
    with DatabaseConnection() as cursor:
        SQL = """SELECT count(*)
                 FROM school
                 WHERE id = %s AND emailAddress = %s"""
        cursor.execute(SQL, (schoolId, emailAddress, ))
        countRetrieved = cursor.fetchall()
    return countRetrieved

# Check if the email address already exists in the database, regardless of school - returns a count of matching email addresses
def checkIfDuplicateSchoolEmail(emailAddress):
    with DatabaseConnection() as cursor:
        SQL = """SELECT count(*)
                 FROM school
                 WHERE emailAddress = %s"""
        cursor.execute(SQL, (emailAddress, ))
        countRetrieved = cursor.fetchall()
    return countRetrieved

# Update an existing school record with new details
def updateSchoolDetails(schoolId, schoolName, phoneNumber, emailAddress):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE school
                 SET name = %s, phoneNumber = %s, emailAddress = %s
                 WHERE id = %s"""
        cursor.execute(SQL, (schoolName, phoneNumber, emailAddress, schoolId, ))

# Update the address that the school provided is matched to
def updateSchoolAddressId(schoolId, addressId):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE school
                 SET addressId = %s
                 WHERE id = %s"""
        cursor.execute(SQL, (addressId, schoolId, ))

# Update the name of the school with the name provided
def updateSchoolName(schoolId, schoolName):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE school
                 SET name = %s
                 WHERE id = %s"""
        cursor.execute(SQL, (schoolName, schoolId, ))

# Count how many times an address is used in the school table
def countAddressUsageInSchools(addressId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT count(*)
                 FROM school
                 WHERE addressId = %s"""
        cursor.execute(SQL, (addressId, ))
        countRetrieved = cursor.fetchall()
    return countRetrieved

# Insert a new school record into the school table
def insertNewSchoolRecord(schoolName, addressId, phoneNumber, emailAddress):
    with DatabaseConnection() as cursor:
        SQL = """INSERT INTO school(name, addressId, phoneNumber, emailAddress)
                 VALUES(%s, %s, %s, %s)"""
        cursor.execute(SQL, (schoolName, addressId, phoneNumber, emailAddress, ))

# Retrieve the school id based on the provided email address
def getSchoolIdBasedOnEmailAddress(emailAddress):
    with DatabaseConnection() as cursor:
        SQL = """SELECT id
                 FROM school
                 WHERE emailAddress = %s"""
        cursor.execute(SQL, (emailAddress, ))
        idRetrieved = cursor.fetchall()
    return idRetrieved

#===== Account Table SQLs ===========================================================================================================================================

# Insert a new account record into the account table
def insertNewSchoolAccountRecord(accountType, schoolId, personId, password):
    with DatabaseConnection() as cursor:
        SQL = """INSERT INTO account(type, schoolId, personId, password, deletedFlag)
                 VALUES(%s, %s, %s, %s, 0)"""
        cursor.execute(SQL, (accountType, schoolId, personId, password, ))

# Retrieve an account password linked to the provided school id
def getAccountPasswordBasedOnSchoolId(schoolId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT password
                 FROM account
                 WHERE schoolId = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (schoolId, ))
        passwordRetrieved = cursor.fetchall()
    return passwordRetrieved

# Retrieve an account password linked to the provided person id
def getAccountPasswordBasedOnPersonId(personId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT password
                 FROM account
                 WHERE personId = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (personId, ))
        passwordRetrieved = cursor.fetchall()
    return passwordRetrieved

# Retrieve an account password linked to the provided person id
def getAccountPasswordBasedOnPersonIdAndType(personId, accountType):
    with DatabaseConnection() as cursor:
        SQL = """SELECT password
                 FROM account
                 WHERE personId = %s AND type = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (personId, accountType, ))
        passwordRetrieved = cursor.fetchall()
    return passwordRetrieved

# Update the school password based on the school id provided
def updateSchoolAccountPassword(schoolId, password):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE account
                 SET password = %s
                 WHERE schoolId = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (password, schoolId, ))

# Insert a new account record into the account table
def insertNewPersonAccountRecord(accountType, schoolId, personId, password):
    with DatabaseConnection() as cursor:
        SQL = """INSERT INTO account(type, schoolId, personId, password, deletedFlag)
                 VALUES(%s, %s, %s, %s, 0)"""
        cursor.execute(SQL, (accountType, schoolId, personId, password, ))

# Remove an account based on the person id
def deleteAccountRecord(personId):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE account
                 SET deletedFlag = 1
                 WHERE personId = %s"""
        cursor.execute(SQL, (personId, ))

# Retrieve the account type based on the provided person id and password
def getAccountTypeBasedOnPersonIdAndPassword(personId, password):
    with DatabaseConnection() as cursor:
        SQL = """SELECT type
                 FROM account
                 WHERE personId = %s AND password = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (personId, password, ))
        typeRetrieved = cursor.fetchall()
    return typeRetrieved

# Update the persons account with new password details
def updatePersonAccountPassword(accountType, schoolId, personId, password):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE account
                 SET password = %s
                 WHERE type = %s AND schoolId = %s AND personId = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (password, accountType, schoolId, personId, ))

# Remove an existing account based on its person id and account type
def deleteAccountRecordBasedOnIdAndType(personId, accountType):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE account
                 SET deletedFlag = 1
                 WHERE personId = %s AND type = %s"""
        cursor.execute(SQL, (personId, accountType, ))

#===== Address Table SQLs ===========================================================================================================================================

# Retrieve the address identified by the provided address id
def getAddressDetails(addressId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT id, streetName1, streetName2, townOrCity, county
                 FROM address
                 WHERE id = %s"""
        cursor.execute(SQL, (addressId, ))
        addressRetrieved = cursor.fetchall()
    return addressRetrieved

# Update an existing address record with new details
def updateAddressDetails(addressId, streetName1, streetName2, townOrCity, county):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE address SET streetName1 = %s, streetName2 = %s, townOrCity = %s, county = %s
                 WHERE id = %s"""
        cursor.execute(SQL, (streetName1, streetName2, townOrCity, county, addressId, ))

# Count the number of records that are stored in the address table
def countRecordsInAddressTable():
    with DatabaseConnection() as cursor:
        SQL = """SELECT count(*)
                 FROM address"""
        cursor.execute(SQL)
        countRetrieved = cursor.fetchall()
    return countRetrieved

# Insert a new address record into the address table
def insertNewAddressRecord(addressId, streetName1, streetName2, townOrCity, county):
    with DatabaseConnection() as cursor:
        SQL = """INSERT INTO address(id, streetName1, streetName2, townOrCity, county, deletedFlag)
                 VALUES(%s, %s, %s, %s, %s, 0)"""
        cursor.execute(SQL, (addressId, streetName1, streetName2, townOrCity, county, ))

# Count the number of address records which match the address attributes provided
def countNumberOfDuplicateAddresses(streetName1, streetName2, townOrCity, county):
    with DatabaseConnection() as cursor:
        SQL = """SELECT count(*)
                 FROM address
                 WHERE streetName1 = %s AND streetName2 = %s AND townOrCity = %s AND county = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (streetName1, streetName2, townOrCity, county, ))
        countRetrieved = cursor.fetchall()
    return countRetrieved

# Mark an existing address record as deleted
def deleteAddressRecord(addressId):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE address
                 SET deletedFlag = 1
                 WHERE id = %s"""
        cursor.execute(SQL, (addressId, ))

# Get the address id of the address matching the details provided
def getAddressId(streetName1, streetName2, townOrCity, county):
    with DatabaseConnection() as cursor:
        SQL = """SELECT id
                 FROM address
                 WHERE streetName1 = %s AND streetName2 = %s AND townOrCity = %s AND county = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (streetName1, streetName2, townOrCity, county, ))
        idRetrieved = cursor.fetchall()
    return idRetrieved

#===== Weekday Table SQLs ===========================================================================================================================================

# Get the list of weekdays from the database table
def getListOfWeekdays():
    with DatabaseConnection() as cursor:
        SQL = """SELECT id, name
                 FROM weekday"""
        cursor.execute(SQL)
        daysRetrieved = cursor.fetchall()
    return daysRetrieved

# Get the weekday name by weekday id
def getWeekdayNameById(weekdayId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT name
                 FROM weekday
                 WHERE id = %s"""
        cursor.execute(SQL, (weekdayId, ))
        dayRetrieved = cursor.fetchall()
    return dayRetrieved

#===== Opening Hours Table SQLs =====================================================================================================================================

# Retrieve the current opening hours for the school
def getSchoolOpeningHours(schoolId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT id, schoolId, weekdayId, timeId
                 FROM openinghours
                 WHERE schoolId = %s"""
        cursor.execute(SQL, (schoolId, ))
        hoursRetrieved = cursor.fetchall()
    return hoursRetrieved

# Retrieve the time id (whether the school is open or closed) for the weekday corresponding to the index position provided
def getOpeningHoursTimeId(schoolId, weekdayId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT timeId
                 FROM openinghours
                 WHERE schoolId = %s AND weekdayId = %s"""
        cursor.execute(SQL, (schoolId, weekdayId, ))
        idRetrieved = cursor.fetchall()
    return idRetrieved

# Get the unique id for the opening hours record for the school & weekday provided
def getOpeningHoursId(schoolId, weekdayId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT id
                 FROM openinghours
                 WHERE schoolId = %s AND weekdayId = %s"""
        cursor.execute(SQL, (schoolId, weekdayId, ))
        idRetrieved = cursor.fetchall()
    return idRetrieved

# Set the time id (whether the school is open or closed) for the weekday corresponding to the index position provided
def setOpeningHoursTimeId(openingHoursId, timeId):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE openinghours
                 SET timeId = %s
                 WHERE id = %s"""
        cursor.execute(SQL, (timeId, openingHoursId, ))

# Insert a new opening hours record into the opening hours table (school registration process)
def insertNewOpeningHoursRecord(schoolId, weekdayId):
    with DatabaseConnection() as cursor:
        SQL = """INSERT INTO openinghours(schoolId, weekdayId)
                 VALUES(%s, %s)"""
        cursor.execute(SQL, (schoolId, weekdayId, ))

#===== Time Table SQLs ==============================================================================================================================================

# Retrieve the time entry associated with the provided time id
def getTimeRecord(timeId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT id, startTime, endTime
                 FROM time
                 WHERE id = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (timeId, ))
        timeRetrieved = cursor.fetchall()
    return timeRetrieved

# Count the number of records stored in the time table
def countRecordsInTimeTable():
    with DatabaseConnection() as cursor:
        SQL = """SELECT count(*)
                 FROM time"""
        cursor.execute(SQL)
        countRetrieved = cursor.fetchall()
    return countRetrieved

# Insert a new record into the time table
def insertNewTimeRecord(timeId, startTime, endTime, deletedFlag):
    with DatabaseConnection() as cursor:
        SQL = """INSERT INTO time(id, startTime, endTime, deletedFlag)
                 VALUES(%s, %s, %s, %s)"""
        cursor.execute(SQL, (timeId, startTime, endTime, deletedFlag, ))

# Update an existing time record in the time table
def updateExistingTimeRecord(timeId, startTime, endTime):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE time
                 SET startTime = %s, endTime = %s
                 WHERE id = %s"""
        cursor.execute(SQL, (startTime, endTime, timeId, ))

# Set the deleted flag of the time table record to 1 (mark as deleted)
def deleteTimeRecord(timeId):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE time
                 SET deletedFlag = 1
                 WHERE id = %s"""
        cursor.execute(SQL, (timeId, ))

#===== Lesson Table SQLs ============================================================================================================================================

# Insert a new lesson record into the lesson table
def insertNewLessonRecord(lessonName):
    with DatabaseConnection() as cursor:
        SQL = """INSERT INTO lesson(name, deletedFlag)
                 VALUES(%s, 0)"""
        cursor.execute(SQL, (lessonName, ))

# Retrieve the lesson id associated with the specified lesson name
def getLessonId(lessonName):
    with DatabaseConnection() as cursor:
        SQL = """SELECT id
                 FROM lesson
                 WHERE name = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (lessonName, ))
        idRetrieved = cursor.fetchall()
    return idRetrieved

# Retrieve the lesson name based on lesson id provided
def getLessonName(lessonId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT name
                 FROM lesson
                 WHERE id = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (lessonId, ))
        nameRetrieved = cursor.fetchall()
    return nameRetrieved

# Count the number of lessons that match the specified name
def countNumberOfDuplicateLessonNames(lessonName):
    with DatabaseConnection() as cursor:
        SQL = """SELECT count(*)
                 FROM lesson
                 WHERE name = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (lessonName, ))
        countRetrieved = cursor.fetchall()
    return countRetrieved

# Remove an existing lesson, identified by its id, by setting the deletedFlag to a deleted state
def deleteLessonById(lessonId):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE lesson
                 SET deletedFlag = 1
                 WHERE id = %s"""
        cursor.execute(SQL, (lessonId, ))

#===== SchoolLesson Table SQLs ======================================================================================================================================

# Insert a new record into the School/Lesson table
def insertNewSchoolLessonRecord(schoolId, lessonId, abbreviatedName, colour):
    with DatabaseConnection() as cursor:
        SQL = """INSERT INTO schoollesson(schoolId, lessonId, abbreviatedName, colour, deletedFlag)
                 VALUES(%s, %s, %s, %s, 0)"""
        cursor.execute(SQL, (schoolId, lessonId, abbreviatedName, colour, ))

# Update an existing SchoolLesson record
def updateSchoolLessonRecord(schoolLessonId, schoolId, lessonId, abbreviatedName, colour):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE schoollesson
                 SET schoolId = %s, lessonId = %s, abbreviatedName = %s, colour = %s
                 WHERE id = %s"""
        cursor.execute(SQL, (schoolId, lessonId, abbreviatedName, colour, schoolLessonId, ))

# Determine if any school in the system is using the specified lesson
def countNumberOfTimesLessonIsUsed(lessonId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT count(*)
                 FROM schoollesson
                 WHERE lessonId = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (lessonId, ))
        countRetrieved = cursor.fetchall()
    return countRetrieved

# Remove an existing schoollesson record, identified by its id, to a deleted state (ie, set deletedFlag = 1)
def deleteSchoolLessonRecord(schoolLessonId):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE schoollesson
                 SET deletedFlag = 1
                 WHERE id = %s"""
        cursor.execute(SQL, (schoolLessonId, ))

# Retrieve the abbreviated name for the schoollessonId provided
def getLessonAbbreviatedNameBasedOnSchoolLessonId(schoolLessonId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT abbreviatedName
                 FROM schoollesson
                 WHERE id = %s"""
        cursor.execute(SQL, (schoolLessonId, ))
        nameRetrieved = cursor.fetchall()
    return nameRetrieved

#===== Location Table SQLs ==========================================================================================================================================

# Insert a brand new location record into the location table
def insertNewLocationRecord(locationName, schoolId, addressId, headLocation):
    with DatabaseConnection() as cursor:
        SQL = """INSERT INTO location(name, schoolId, addressId, headLocation, deletedFlag)
                 VALUES(%s, %s, %s, %s, 0)"""
        cursor.execute(SQL, (locationName, schoolId, addressId, headLocation, ))

# Check if the location name entered is already linked to this school
def checkIfDuplicateLocationName(schoolId, locationName):
    with DatabaseConnection() as cursor:
        SQL = """SELECT count(*)
                 FROM location
                 WHERE name = %s AND schoolId = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (locationName, schoolId, ))
        countRetrieved = cursor.fetchall()
    return countRetrieved

# Check if the edited location name entered is already linked to this school
def checkIfDuplicateEditedName(schoolId, locationId, locationName):
    with DatabaseConnection() as cursor:
        SQL = """SELECT count(*)
                 FROM location
                 WHERE name = %s AND schoolId = %s AND id != %s AND deletedFlag = 0"""
        cursor.execute(SQL, (locationName, schoolId, locationId, ))
        countRetrieved = cursor.fetchall()
    return countRetrieved

# Update the location name to the new location name provided
def updateLocationName(locationId, locationName):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE location
                 SET name = %s
                 WHERE id = %s"""
        cursor.execute(SQL, (locationName, locationId, ))

# Update the locations address id
def updateLocationAddressId(locationId, addressId):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE location
                 SET addressId = %s
                 WHERE id = %s"""
        cursor.execute(SQL, (addressId, locationId, ))

# Set a location record as being deleted - ie set the deletedFlag to 1
def removeLocationRecord(locationId):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE location
                 SET deletedFlag = 1
                 WHERE id = %s"""
        cursor.execute(SQL, (locationId, ))

# Retrieve the location id for the location name and school provided
def getLocationId(schoolId, locationName):
    with DatabaseConnection() as cursor:
        SQL = """SELECT id
                 FROM location
                 WHERE name = %s AND schoolId = %s"""
        cursor.execute(SQL, (locationName, schoolId, ))
        idRetrieved = cursor.fetchall()
    return idRetrieved

# Count how many times an address is used in the location table
def countAddressUsageInLocations(addressId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT count(*)
                 FROM location
                 WHERE addressId = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (addressId, ))
        countRetrieved = cursor.fetchall()
    return countRetrieved

# Retrieve the head location boolean for the provided location id
def getLocationHeadLocation(locationId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT headLocation
                 FROM location
                 WHERE id = %s"""
        cursor.execute(SQL, (locationId, ))
        headRetrieved = cursor.fetchall()
    return headRetrieved

#===== Person Table SQLs ============================================================================================================================================

# Retrieve the person id for the person details provided
def getPersonId(firstName, surname, dateOfBirth, phoneNumber, emailAddress):
    with DatabaseConnection() as cursor:
        SQL = """SELECT id
                 FROM person
                 WHERE firstName = %s AND surname = %s AND dateOfBirth = %s AND phoneNumber = %s AND emailAddress = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (firstName, surname, dateOfBirth, phoneNumber, emailAddress, ))
        idRetrieved = cursor.fetchall()
    return idRetrieved

# Insert a new person record into the person table
def insertNewPersonRecord(personId, firstName, surname, dateOfBirth, phoneNumber, emailAddress):
    with DatabaseConnection() as cursor:
        SQL = """INSERT INTO person(id, firstName, surname, dateOfBirth, phoneNumber, emailAddress, deletedFlag)
                 VALUES(%s, %s, %s, %s, %s, %s, 0)"""
        cursor.execute(SQL, (personId, firstName, surname, dateOfBirth, phoneNumber, emailAddress, ))

# Count the number of records stored in the person table
def countNumberOfPersonRecords():
    with DatabaseConnection() as cursor:
        SQL = """SELECT count(*)
                 FROM person"""
        cursor.execute(SQL)
        countRetrieved = cursor.fetchall()
    return countRetrieved

# Retrieve a persons details linked to the provided person id
def getPersonDetailsByPersonId(personId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT firstName, surname, dateOfBirth, phoneNumber, emailAddress
                 FROM person
                 WHERE id = %s"""
        cursor.execute(SQL, (personId, ))
        personRetrieved = cursor.fetchall()
    return personRetrieved

# Count the number of persons matching the attributes provided
def countNumberOfDuplicatePersons(firstName, surname, dateOfBirth, phoneNumber, emailAddress):
    with DatabaseConnection() as cursor:
        SQL = """SELECT count(*)
                 FROM person
                 WHERE firstName = %s AND surname = %s AND dateOfBirth = %s AND phoneNumber = %s AND emailAddress = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (firstName, surname, dateOfBirth, phoneNumber, emailAddress, ))
        countRetrieved = cursor.fetchall()
    return countRetrieved

# Mark the person associated with the person id as deleted
def deletePersonRecord(personId):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE person
                 SET deletedFlag = 1
                 WHERE id = %s"""
        cursor.execute(SQL, (personId, ))

# Count the number of email addresses linked to existing persons in the table
def countNumberOfDuplicatePersonEmailAddresses(emailAddress):
    with DatabaseConnection() as cursor:
        SQL = """SELECT count(*)
                 FROM person
                 WHERE emailAddress = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (emailAddress, ))
        countRetrieved = cursor.fetchall()
    return countRetrieved

# Retrieve the persons id based on their email address
def getPersonIdBasedOnEmailAddress(emailAddress):
    with DatabaseConnection() as cursor:
        SQL = """SELECT id
                 FROM person
                 WHERE emailAddress = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (emailAddress, ))
        personRetrieved = cursor.fetchall()
    return personRetrieved

# Get a persons first name and surname linked to the provided email address
def getPersonNameBasedOnEmailAddress(emailAddress):
    with DatabaseConnection() as cursor:
        SQL = """SELECT firstName, surname
                 FROM person
                 WHERE emailAddress = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (emailAddress, ))
        personRetrieved = cursor.fetchall()
    return personRetrieved

# Get a persons email address based on the persons id
def getPersonEmailAddressBasedOnId(personId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT emailAddress
                 FROM person
                 WHERE id = %s"""
        cursor.execute(SQL, (personId, ))
        emailAddressRetrieved = cursor.fetchall()
    return emailAddressRetrieved

#===== Student Table SQLs ===========================================================================================================================================

# Retrieve the student matched to the provided person id
def getStudentIdFromPersonId(personId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT id
                 FROM student
                 WHERE personId = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (personId, ))
        idRetrieved = cursor.fetchall()
    return idRetrieved

# Count how many times an address is used in the student table
def countAddressUsageInStudents(addressId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT count(*)
                 FROM student
                 WHERE addressId = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (addressId, ))
        countRetrieved = cursor.fetchall()
    return countRetrieved

# Count the number of records stored in the student table
def countNumberOfStudentRecords():
    with DatabaseConnection() as cursor:
        SQL = """SELECT count(*)
                 FROM student"""
        cursor.execute(SQL)
        countRetrieved = cursor.fetchall()
    return countRetrieved

# Insert a new student record into the student table
def insertNewStudentRecord(studentId, personId, addressId):
    with DatabaseConnection() as cursor:
        SQL = """INSERT INTO student(id, personId, addressId, deletedFlag)
                 VALUES(%s, %s, %s, 0)"""
        cursor.execute(SQL, (studentId, personId, addressId, ))

# Update the students address id (link to a new address)
def updateStudentAddressId(studentId, addressId):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE student
                 SET addressId = %s
                 WHERE id = %s"""
        cursor.execute(SQL, (addressId, studentId, ))

# Update the students person id (link to a new person)
def updateStudentPersonId(studentId, personId):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE student
                 SET personId = %s
                 WHERE id = %s"""
        cursor.execute(SQL, (personId, studentId, ))

# Count how many times a person is used in the students table
def countPersonUsageInStudents(personId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT count(*)
                 FROM student
                 WHERE personId = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (personId, ))
        countRetrieved = cursor.fetchall()
    return countRetrieved

# Mark a student as deleted - set deletedFlag = 1
def deleteStudentRecord(studentId):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE student
                 SET deletedFlag = 1
                 WHERE id = %s"""
        cursor.execute(SQL, (studentId, ))

#===== SchoolStudent Table SQLs =====================================================================================================================================

# Retrieve a count of whether the student provided matched to the current school
def countMatchingSchoolStudentRecords(schoolId, studentId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT count(*)
                 FROM schoolstudent
                 WHERE schoolId = %s AND studentId = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (schoolId, studentId, ))
        countRetrieved = cursor.fetchall()
    return countRetrieved

# Insert a new school student record into the schoolStudent table
def insertNewSchoolStudentRecord(schoolId, studentId):
    with DatabaseConnection() as cursor:
        SQL = """INSERT INTO schoolstudent(schoolId, studentId, deletedFlag)
                 VALUES(%s, %s, 0)"""
        cursor.execute(SQL, (schoolId, studentId, ))

# Mark a schoolstudent record as deleted - set deletedFlag = 1
def deleteSchoolStudentRecord(schoolId, studentId):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE schoolstudent
                 SET deletedFlag = 1
                 WHERE schoolId = %s AND studentId = %s"""
        cursor.execute(SQL, (schoolId, studentId, ))

# Count how many times a student is used in the schoolstudents table
def countStudentUsageInSchoolStudents(studentId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT count(*)
                 FROM schoolstudent
                 WHERE studentId = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (studentId, ))
        countRetrieved = cursor.fetchall()
    return countRetrieved

# Get all schools associated with the student id provided
def getStudentSchoolsList(studentId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT schoolId
                 FROM schoolstudent
                 WHERE studentId = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (studentId, ))
        schoolsRetrieved = cursor.fetchall()
    return schoolsRetrieved

#===== Teacher Table SQLs ===========================================================================================================================================

# Retrieve the teacher matched to the provided person id
def getTeacherIdFromPersonId(personId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT id
                 FROM teacher
                 WHERE personId = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (personId, ))
        idRetrieved = cursor.fetchall()
    return idRetrieved

# Count the number of records stored in the teacher table
def countNumberOfTeacherRecords():
    with DatabaseConnection() as cursor:
        SQL = """SELECT count(*)
                 FROM teacher"""
        cursor.execute(SQL)
        countRetrieved = cursor.fetchall()
    return countRetrieved

# Insert a new teacher record into the teacher table
def insertNewTeacherRecord(teacherId, personId, addressId):
    with DatabaseConnection() as cursor:
        SQL = """INSERT INTO teacher(id, personId, addressId, deletedFlag)
                 VALUES(%s, %s, %s, 0)"""
        cursor.execute(SQL, (teacherId, personId, addressId, ))

# Update the teachers person id (link to a new person)
def updateTeacherPersonId(teacherId, personId):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE teacher
                 SET personId = %s
                 WHERE id = %s"""
        cursor.execute(SQL, (personId, teacherId, ))

# Count how many times a person is used in the teachers table
def countPersonUsageInTeachers(personId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT count(*)
                 FROM teacher
                 WHERE personId = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (personId, ))
        countRetrieved = cursor.fetchall()
    return countRetrieved

# Update the teachers address id (link to a new address)
def updateTeacherAddressId(teacherId, addressId):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE teacher
                 SET addressId = %s
                 WHERE id = %s"""
        cursor.execute(SQL, (addressId, teacherId, ))

# Mark a teacher as deleted - set deletedFlag = 1
def deleteTeacherRecord(teacherId):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE teacher
                 SET deletedFlag = 1
                 WHERE id = %s"""
        cursor.execute(SQL, (teacherId, ))

# Count how many times the provided address id is used in the teachers table
def countAddressUsageInTeachers(addressId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT count(*)
                 FROM teacher
                 WHERE addressId = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (addressId, ))
        countRetrieved = cursor.fetchall()
    return countRetrieved

#===== SchoolTeacher Table SQLs =====================================================================================================================================

# Retrieve a count of whether the teacher provided matched to the current school
def countMatchingSchoolTeacherRecords(schoolId, teacherId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT count(*)
                 FROM schoolteacher
                 WHERE schoolId = %s AND teacherId = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (schoolId, teacherId, ))
        countRetrieved = cursor.fetchall()
    return countRetrieved

# Insert a new school teacher record into the schoolTeacher table
def insertNewSchoolTeacherRecord(schoolId, teacherId):
    with DatabaseConnection() as cursor:
        SQL = """INSERT INTO schoolteacher(schoolId, teacherId, deletedFlag)
                 VALUES(%s, %s, 0)"""
        cursor.execute(SQL, (schoolId, teacherId, ))

# Mark a schoolteacher record as deleted - set deletedFlag = 1
def deleteSchoolTeacherRecord(schoolId, teacherId):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE schoolteacher
                 SET deletedFlag = 1
                 WHERE schoolId = %s AND teacherId = %s"""
        cursor.execute(SQL, (schoolId, teacherId, ))

# Count how many times a teacher is used in the schoolteachers table
def countTeacherUsageInSchoolTeachers(teacherId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT count(*)
                 FROM schoolteacher
                 WHERE teacherId = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (teacherId, ))
        countRetrieved = cursor.fetchall()
    return countRetrieved

# Get all schools associated with the teacher id provided
def getTeacherSchoolsList(personId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT schoolId
                 FROM schoolteacher
                 WHERE teacherId = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (personId, ))
        schoolsRetrieved = cursor.fetchall()
    return schoolsRetrieved

#===== Classroom Table SQLs =========================================================================================================================================

# Retrieve the classroom id associated with the room name provided
def getClassroomIdFromRoomName(roomName):
    with DatabaseConnection() as cursor:
        SQL = """SELECT id
                 FROM classroom
                 WHERE roomName = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (roomName, ))
        idRetrieved = cursor.fetchall()
    return idRetrieved

# Insert a new classroom record into the classroom table
def insertNewClassroomRecord(roomName):
    with DatabaseConnection() as cursor:
        SQL = """INSERT INTO classroom(roomName, deletedFlag)
                 VALUES(%s, 0)"""
        cursor.execute(SQL, (roomName, ))

# Count the number of duplicate room names in the table (check for duplicates)
def countDuplicateClassroomNames(roomName):
    with DatabaseConnection() as cursor:
        SQL = """SELECT count(*)
                 FROM classroom
                 WHERE roomName = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (roomName, ))
        countRetrieved = cursor.fetchall()
    return countRetrieved
    
# Get a classroom id based on its room name (provided)
def getClassroomIdBasedOnName(roomName):
    with DatabaseConnection() as cursor:
        SQL = """SELECT id
                 FROM classroom
                 WHERE roomName = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (roomName, ))
        idRetrieved = cursor.fetchall()
    return idRetrieved

# Mark a classroom as deleted - set the deleted flag to 1
def deleteClassroomRecord(classroomId):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE classroom
                 SET deletedFlag = 1
                 WHERE id = %s"""
        cursor.execute(SQL, (classroomId, ))

#===== ClassroomLocation Table SQLs =================================================================================================================================

# Retrieve a count of records matching to the location id and classroom id provided
def countDuplicateClassroomLocationRecords(locationId, classroomId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT count(*)
                 FROM classroomlocation
                 WHERE locationId = %s AND classroomId = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (locationId, classroomId, ))
        countRetrieved = cursor.fetchall()
    return countRetrieved

# Insert a new classroomLocation record into the classroomLocation table
def insertNewClassroomLocationRecord(locationId, classroomId):
    with DatabaseConnection() as cursor:
        SQL = """INSERT INTO classroomlocation(locationId, classroomId, deletedFlag)
                 VALUES(%s, %s, 0)"""
        cursor.execute(SQL, (locationId, classroomId, ))

# Update the location id of a classroom stored in the classroomLocation table
def updateClassroomLocationId(oldLocationId, newLocationId, classroomId):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE classroomlocation
                 SET locationId = %s
                 WHERE locationId = %s AND classroomId = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (newLocationId, oldLocationId, classroomId, ))

# Update a classrooms location id and classroom id
def updateClassroomLocationAndRoomId(oldLocationId, newLocationId, oldClassroomId, newClassroomId):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE classroomlocation
                 SET locationId = %s, classroomId = %s
                 WHERE locationId = %s AND classroomId = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (newLocationId, newClassroomId, oldLocationId, oldClassroomId, ))

# Count how many times the provided classroom id is used in the classroomlocation table
def countClassroomIdUsage(classroomId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT count(*)
                 FROM classroomlocation
                 WHERE classroomId = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (classroomId, ))
        countRetrieved = cursor.fetchall()
    return countRetrieved

# Retrieve all details stored in this table that are linked to the provided location id
def getLocationClassroomRecords(locationId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT id, classroomId
                 FROM classroomlocation
                 WHERE locationId = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (locationId, ))
        recordsRetrieved = cursor.fetchall()
    return recordsRetrieved

# Mark a classroomlocation record as deleted - set the deletedFlag = 1
def deleteClassroomLocationRecordById(recordId):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE classroomlocation
                 SET deletedFlag = 1
                 WHERE id = %s"""
        cursor.execute(SQL, (recordId, ))

# Mark a classroomlocation record as deleted - set the deletedFlag = 1
def deleteClassroomLocationRecord(locationId, classroomId):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE classroomlocation
                 SET deletedFlag = 1
                 WHERE locationId = %s AND classroomId = %s"""
        cursor.execute(SQL, (locationId, classroomId, ))

# Retrieve the id matched to the location id and classroom id provided
def getClassroomLocationIdBasedOnLocationIdAndClassroomId(locationId, classroomId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT id
                 FROM classroomlocation
                 WHERE locationId = %s AND classroomId = %s"""
        cursor.execute(SQL, (locationId, classroomId, ))
        idRetrieved = cursor.fetchall()
    return idRetrieved

# Retrieve the classroom id based on the classroomLocation id provided
def getClassroomIdFromClassroomLocationId(classroomLocationId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT classroomId
                 FROM classroomlocation
                 WHERE id = %s"""
        cursor.execute(SQL, (classroomLocationId, ))
        idRetrieved = cursor.fetchall()
    return idRetrieved

#===== Timetable Table SQLs =========================================================================================================================================

# Retrieve the timetable for the school and student provided
def getStudentTimetable(schoolId, studentId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT id, weekdayId, startHour, startMin, lessonLength, schoolId, studentId, schoolLessonId, teacherId, locationId, classroomLocationId
                 FROM timetable
                 WHERE schoolId = %s AND studentId = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (schoolId, studentId, ))
        timetableRetrieved = cursor.fetchall()
    return timetableRetrieved

# Retrieve the timetable for the classroom provided
def getClassroomLocationTimetable(classroomLocationId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT id, weekdayId, startHour, startMin, lessonLength, schoolId, studentId, schoolLessonId, teacherId, locationId,
                 (SELECT roomName
                 FROM classroom
                 INNER JOIN classroomlocation ON classroomlocation.classroomId = classroom.id
                 WHERE classroomlocation.id = %s)
                 FROM timetable
                 WHERE classroomLocationId = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (classroomLocationId, classroomLocationId, ))
        timetableRetrieved = cursor.fetchall()
    return timetableRetrieved

# Retrieve the individual school timetable for the teacher provided
def getTeacherSchoolTimetable(schoolId, teacherId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT id, weekdayId, startHour, startMin, lessonLength, schoolId, studentId, schoolLessonId, teacherId, locationId, classroomLocationId
                 FROM timetable
                 WHERE schoolId = %s AND teacherId = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (schoolId, teacherId, ))
        timetableRetrieved = cursor.fetchall()
    return timetableRetrieved

# Retrieve the individual school timetable for the student provided
def getStudentSchoolTimetable(schoolId, studentId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT id, weekdayId, startHour, startMin, lessonLength, schoolId, studentId, schoolLessonId, teacherId, locationId, classroomLocationId
                 FROM timetable
                 WHERE schoolId = %s AND studentId = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (schoolId, studentId, ))
        timetableRetrieved = cursor.fetchall()
    return timetableRetrieved

# Retrieve the students timetable across all schools
def getStudentAllTimetable(studentId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT id, weekdayId, startHour, startMin, lessonLength, schoolId, studentId, schoolLessonId, teacherId, locationId, classroomLocationId
                 FROM timetable
                 WHERE studentId = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (studentId, ))
        timetableRetrieved = cursor.fetchall()
    return timetableRetrieved

# Retrieve the teachers timetable across all schools
def getTeacherAllTimetable(teacherId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT id, weekdayId, startHour, startMin, lessonLength, schoolId, studentId, schoolLessonId, teacherId, locationId, classroomLocationId
                 FROM timetable
                 WHERE teacherId = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (teacherId, ))
        timetableRetrieved = cursor.fetchall()
    return timetableRetrieved

# Update an existing timetable id record
def updateExistingTimetableRecord(recordId, weekdayId, startHour, startMin, lessonLength, endHour, schoolLessonId, teacherId, locationId, classroomLocationId):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE timetable
                 SET weekdayId = %s, startHour = %s, startMin = %s, lessonLength = %s, endHour = %s, schoolLessonId = %s,
                 teacherId = %s, locationId = %s, classroomLocationId = %s
                 WHERE id = %s"""
        cursor.execute(SQL, (weekdayId, startHour, startMin, lessonLength, endHour, schoolLessonId, teacherId, locationId, classroomLocationId, recordId, ))

# Count the number of records stored in the timetable table
def countNumberOfTimetableRecords():
    with DatabaseConnection() as cursor:
        SQL = """SELECT count(*)
                 FROM timetable"""
        cursor.execute(SQL)
        countRetrieved = cursor.fetchall()
    return countRetrieved

# Insert a new timetable record into the table
def insertNewTimetableRecord(recordId, weekdayId, startHour, startMin, lessonLength, endHour, schoolLessonId,
                             schoolId, studentId, teacherId, locationId, classroomLocationId):
    with DatabaseConnection() as cursor:
        SQL = """INSERT INTO timetable(id, weekdayId, startHour, startMin, lessonLength, endHour, schoolLessonId, schoolId, studentId, teacherId, locationId,
                                       classroomLocationId, deletedFlag)
                 VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 0)"""
        cursor.execute(SQL, (recordId, weekdayId, startHour, startMin, lessonLength, endHour, schoolLessonId,
                             schoolId, studentId, teacherId, locationId, classroomLocationId, ))

# Mark a timetable record as deleted - set the deletedFlag = 1
def deleteTimetableRecord(recordId):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE timetable
                 SET deletedFlag = 1
                 WHERE id = %s"""
        cursor.execute(SQL, (recordId, ))

# Mark all records outside of the schools opening hours as deleted - set the deletedFlag = 1
def deleteTimetableRecordsBeforeSchoolStart(schoolId, startHour):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE timetable
                 SET deletedFlag = 1
                 WHERE schoolId = %s AND startHour < %s AND deletedFlag = 0"""
        cursor.execute(SQL, (schoolId, startHour, ))

# Mark all records outside of the schools closing hours as deleted - set the deletedFlag = 1
def deleteTimetableRecordsAfterSchoolEnd(schoolId, endHour):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE timetable
                 SET deletedFlag = 1
                 WHERE schoolId = %s AND endHour >= %s AND deletedFlag = 0"""
        cursor.execute(SQL, (schoolId, endHour, ))

# Mark all records linked to the provided schoolLessonId as deleted - set the deletedFlag = 1
def deleteTimetableRecordsBasedOnSchoolLessonId(schoolLessonId):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE timetable
                 SET deletedFlag = 1
                 WHERE schoolLessonId = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (schoolLessonId, ))

# Mark all records linked to the provided schoolId and teacherId as deleted - set the deletedFlag = 1
def deleteTimetableRecordsBasedOnSchoolIdAndTeacherId(schoolId, teacherId):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE timetable
                 SET deletedFlag = 1
                 WHERE schoolId = %s AND teacherId = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (schoolId, teacherId, ))

# Mark all records linked to the provided classroomLocationId - set the deletedFlag = 1
def deleteTimetableRecordsBasedOnClassroomLocationId(classroomLocationId):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE timetable
                 SET deletedFlag = 1
                 WHERE classroomLocationId = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (classroomLocationId, ))

# Mark all records linked to the provided locationId as deleted - set the deletedFlag = 1
def deleteTimetableRecordsBasedOnLocationId(locationId):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE timetable
                 SET deletedFlag = 1
                 WHERE locationId = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (locationId, ))

# Mark all records linked to the provided schoolId and studentId as deleted - set the deletedFlag = 1
def deleteTimetableRecordsBasedOnSchoolIdAndStudentId(schoolId, studentId):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE timetable
                 SET deletedFlag = 1
                 WHERE schoolId = %s AND studentId = %s AND deletedFlag = 0"""
        cursor.execute(SQL, (schoolId, studentId, ))

# Retrieve all lessons for the provided student that take place within the scheduled time frame (not including lessons linked to the the school provided)
def getStudentLessonsWithinTimeSlot(schoolId, studentId, weekdayId, startHour, endHour):
    with DatabaseConnection() as cursor:
        SQL = """SELECT startHour, startMin, lessonLength
                 FROM timetable
                 WHERE schoolId != %s AND weekdayId = %s AND studentId = %s AND ((startHour >= %s AND startHour <= %s) OR (startHour <= %s AND endHour >= %s))
                 AND deletedFlag = 0"""
        cursor.execute(SQL, (schoolId, weekdayId, studentId, startHour, endHour, startHour, startHour, ))
        lessonsRetrieved = cursor.fetchall()
    return lessonsRetrieved

# Retrieve all lessons for the provided teacher that take place within the time slot provided
def getTeacherLessonsWithinTimeSlot(teacherId, weekdayId, studentId, startHour, endHour):
    with DatabaseConnection() as cursor:
        SQL = """SELECT startHour, startMin, lessonLength
                 FROM timetable
                 WHERE weekdayId = %s AND teacherId = %s AND studentId != %s AND ((startHour >= %s AND startHour <= %s) OR (startHour <= %s AND endHour >= %s))
                 AND deletedFlag = 0"""
        cursor.execute(SQL, (weekdayId, teacherId, studentId, startHour, endHour, startHour, startHour, ))
        lessonsRetrieved = cursor.fetchall()
    return lessonsRetrieved

# Retrieve all lessons for the provided classroom that take place within the time slot provided
def getClassroomLessonsWithinTimeSlot(classroomLocationId, weekdayId, studentId, startHour, endHour):
    with DatabaseConnection() as cursor:
        SQL = """SELECT startHour, startMin, lessonLength
                 FROM timetable
                 WHERE weekdayId = %s AND classroomLocationId = %s AND studentId != %s AND
                 ((startHour >= %s AND startHour <= %s) OR (startHour <= %s AND endHour >= %s)) AND deletedFlag = 0"""
        cursor.execute(SQL, (weekdayId, classroomLocationId, studentId, startHour, endHour, startHour, startHour ))
        lessonsRetrieved = cursor.fetchall()
    return lessonsRetrieved

# Delete all of the timetable records for a school day
def deleteTimetableRecordsByDay(schoolId, weekdayId):
    with DatabaseConnection() as cursor:
        SQL = """UPDATE timetable
                 SET deletedFlag = 1
                 WHERE schoolId = %s AND weekdayId = %s"""
        cursor.execute(SQL, (schoolId, weekdayId, ))
    
#===== Multiple Table SQLs ==========================================================================================================================================

# Retrieve the names of all lessons associated with the provided school
def getListOfLessonNames(schoolId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT name
                 FROM lesson
                 INNER JOIN schoollesson ON schoollesson.lessonId = lesson.id
                 WHERE schoolId = %s AND schoollesson.deletedFlag = 0 AND lesson.deletedFlag = 0
                 ORDER BY name"""
        cursor.execute(SQL, (schoolId, ))
        lessonsRetrieved = cursor.fetchall()
    return lessonsRetrieved

# Retrieve the complete list of lesson details for the school id and lesson name provided
def getListOfLessonDetails(schoolId, lessonName):
    with DatabaseConnection() as cursor:
        SQL = """SELECT schoollesson.id, lesson.id, name, abbreviatedName, colour
                 FROM lesson
                 INNER JOIN schoollesson ON schoollesson.lessonId = lesson.id
                 WHERE schoolId = %s AND name = %s AND schoollesson.deletedFlag = 0"""
        cursor.execute(SQL, (schoolId, lessonName, ))
        lessonRetrieved = cursor.fetchall()
    return lessonRetrieved

# Count the number of existing lessons which match the current lesson entry - returns count = 0 if no duplicates found, count > 0 otherwise
def countNumberOfDuplicateLessons(schoolId, lessonName):
    with DatabaseConnection() as cursor:
        SQL = """SELECT count(*)
                 FROM schoollesson
                 INNER JOIN lesson ON schoollesson.lessonId = lesson.id
                 WHERE lesson.name = %s AND schoollesson.schoolId = %s
                 AND lesson.deletedFlag = 0 AND schoollesson.deletedFlag = 0"""
        cursor.execute(SQL, (lessonName, schoolId, ))
        countRetrieved = cursor.fetchall()
    return countRetrieved

# Retrieve the lesson name linked to the schoolLessonId provided
def getLessonNameBySchoolLessonId(schoolLessonId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT lesson.name
                 FROM lesson
                 INNER JOIN schoollesson ON schoollesson.lessonId = lesson.id
                 WHERE schoollesson.id = %s"""
        cursor.execute(SQL, (schoolLessonId, ))
        nameRetrieved = cursor.fetchall()
    return nameRetrieved

# Retrieve all school locations associated with the provided school id
def getListOfSchoolLocations(schoolId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT location.id, location.name, address.id, address.streetName1, address.streetName2, address.townOrCity, address.county
                 FROM location
                 INNER JOIN address ON location.addressId = address.id
                 WHERE schoolId = %s AND location.deletedFlag = 0 AND address.deletedFlag = 0"""
        cursor.execute(SQL, (schoolId, ))
        locationsRetrieved = cursor.fetchall()
    return locationsRetrieved

# Retrieve the list of all students (and their details) matching the school, first name and surname provided
def getListOfStudentDetails(schoolId, firstName, surname):
    with DatabaseConnection() as cursor:
        SQL = """SELECT person.id, address.id, student.id, firstName, surname, dateOfBirth, phoneNumber, emailAddress, streetName1, streetName2, townOrCity, county
                 FROM person
                 INNER JOIN student ON person.id = student.personId
                 INNER JOIN address ON student.addressId = address.id
                 INNER JOIN schoolstudent ON schoolstudent.studentId = student.id
                 WHERE schoolId = %s AND firstName = %s AND surname = %s AND schoolstudent.deletedFlag = 0"""
        cursor.execute(SQL, (schoolId, firstName, surname, ))
        studentsRetrieved = cursor.fetchall()
    return studentsRetrieved

# Retrieve the list of student names associated with the current school
def getListOfStudentNames(schoolId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT firstName, surname, dateOfBirth
                 FROM person
                 INNER JOIN student ON person.id = student.personId
                 INNER JOIN schoolstudent ON schoolstudent.studentId = student.id
                 WHERE schoolId = %s AND schoolstudent.deletedFlag = 0
                 ORDER BY firstName ASC"""
        cursor.execute(SQL, (schoolId, ))
        namesRetrieved = cursor.fetchall()
    return namesRetrieved

# Retrieve the list of teacher names associated with the current school
def getListOfTeacherNames(schoolId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT firstName, surname, dateOfBirth
                 FROM person
                 INNER JOIN teacher ON person.id = teacher.personId
                 INNER JOIN schoolteacher ON schoolteacher.teacherId = teacher.id
                 WHERE schoolId = %s AND schoolteacher.deletedFlag = 0
                 ORDER BY firstName ASC"""
        cursor.execute(SQL, (schoolId, ))
        namesRetrieved = cursor.fetchall()
    return namesRetrieved

# Retrieve the list of all teachers (and their details) matching the school, first name and surname provided
def getListOfTeacherDetails(schoolId, firstName, surname):
    with DatabaseConnection() as cursor:
        SQL = """SELECT person.id, address.id, teacher.id, firstName, surname, dateOfBirth, phoneNumber, emailAddress, streetName1, streetName2, townOrCity, county
                 FROM person
                 INNER JOIN teacher ON person.id = teacher.personId
                 INNER JOIN address ON teacher.addressId = address.id
                 INNER JOIN schoolteacher ON schoolteacher.teacherId = teacher.id
                 WHERE schoolId = %s AND firstName = %s AND surname = %s AND schoolteacher.deletedFlag = 0"""
        cursor.execute(SQL, (schoolId, firstName, surname, ))
        teachersRetrieved = cursor.fetchall()
    return teachersRetrieved

# Retrieve the list of all classrooms matched to the provided location id
def getListOfClassrooms(locationId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT location.id, classroom.id, roomName
                 FROM location
                 INNER JOIN classroomlocation ON classroomlocation.locationId = location.id
                 INNER JOIN classroom ON classroomlocation.classroomId = classroom.id
                 WHERE classroomlocation.locationId = %s AND classroomlocation.deletedFlag = 0"""
        cursor.execute(SQL, (locationId, ))
        classroomsRetrieved = cursor.fetchall()
    return classroomsRetrieved

# Retrieve the existing details for a classroom based on its id and location id
def getClassroomNameBasedOnIdAndLocation(locationId, classroomId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT roomName
                 FROM classroom
                 INNER JOIN classroomlocation ON classroomlocation.classroomId = classroom.id
                 WHERE classroomlocation.classroomId = %s AND locationId = %s AND classroomlocation.deletedFlag = 0"""
        cursor.execute(SQL, (classroomId, locationId, ))
        detailsRetrieved = cursor.fetchall()
    return detailsRetrieved

# Retrieve the room name for a classroom based on classroomLocationId
def getClassroomNameBasedOnClassroomLocationId(classroomLocationId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT roomName
                 FROM classroom
                 INNER JOIN classroomlocation ON classroomlocation.classroomId = classroom.id
                 WHERE classroomlocation.id = %s AND classroomlocation.deletedFlag = 0"""
        cursor.execute(SQL, (classroomLocationId, ))
        nameRetrieved = cursor.fetchall()
    return nameRetrieved

# Retrieve the list of all student names and ids for the provided school
def getSchoolStudentsNamesAndIds(schoolId, firstName, surname):
    with DatabaseConnection() as cursor:
        SQL = """SELECT student.id, firstName, surname
                 FROM student
                 INNER JOIN person ON student.personId = person.id
                 INNER JOIN schoolstudent ON schoolstudent.studentId = student.id
                 WHERE schoolId = %s AND firstName = %s AND surname = %s AND schoolstudent.deletedFlag = 0 AND student.deletedFlag = 0"""
        cursor.execute(SQL, (schoolId, firstName, surname))
        studentsRetrieved = cursor.fetchall()
    return studentsRetrieved

# Retrieve the list of all details associated with all lessons for the school id provided
def getListOfFullLessonDetails(schoolId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT schoollesson.id, name, abbreviatedName, colour
                 FROM lesson
                 INNER JOIN schoollesson ON schoollesson.lessonId = lesson.id
                 WHERE schoolId = %s AND schoollesson.deletedFlag = 0"""
        cursor.execute(SQL, (schoolId, ))
        lessonsRetrieved = cursor.fetchall()
    return lessonsRetrieved

# Retrieve the list of teacher id's and full names that are linked to the school id provided
def getListOfTeacherIdsAndNames(schoolId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT teacher.id, firstName, surname
                 FROM teacher
                 INNER JOIN person ON teacher.personId = person.id
                 INNER JOIN schoolteacher ON schoolteacher.teacherId = teacher.id
                 WHERE schoolId = %s AND schoolteacher.deletedFlag = 0"""
        cursor.execute(SQL, (schoolId, ))
        teachersRetrieved = cursor.fetchall()
    return teachersRetrieved

# Retrieve the list of classroom id's, names and locations that are linked to the school id provided
def getListOfClassroomIdsNamesAndLocations(schoolId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT location.id, name, classroom.id, roomName
                 FROM location
                 INNER JOIN classroomlocation ON classroomlocation.locationId = location.id
                 INNER JOIN classroom ON classroomlocation.classroomId = classroom.id
                 WHERE schoolId = %s AND location.deletedFlag = 0 AND classroom.deletedFlag = 0"""
        cursor.execute(SQL, (schoolId, ))
        classroomsRetrieved = cursor.fetchall()
    return classroomsRetrieved

# Retrieve the list of teacher accounts for the school id provided and matching the name provided
def getTeacherAccountsList(schoolId, firstName, surname):
    with DatabaseConnection() as cursor:
        SQL = """SELECT person.id, firstName, surname, emailAddress
                 FROM person
                 INNER JOIN teacher ON teacher.personId = person.id
                 INNER JOIN schoolteacher ON schoolteacher.teacherId = teacher.id
                 WHERE schoolteacher.schoolId = %s AND firstName = %s AND surname = %s AND schoolteacher.deletedFlag = 0 AND person.deletedFlag = 0"""
        cursor.execute(SQL, (schoolId, firstName, surname, ))
        accountsRetrieved = cursor.fetchall()
    return accountsRetrieved

# Retrieve the list of student accounts for the school id provided and matching the name provided
def getStudentAccountsList(schoolId, firstName, surname):
    with DatabaseConnection() as cursor:
        SQL = """SELECT person.id, firstName, surname, emailAddress
                 FROM person
                 INNER JOIN student ON student.personId = person.id
                 INNER JOIN schoolstudent ON schoolstudent.studentId = student.id
                 WHERE schoolstudent.schoolId = %s AND firstName = %s AND surname = %s AND schoolstudent.deletedFlag = 0 AND person.deletedFlag = 0"""
        cursor.execute(SQL, (schoolId, firstName, surname, ))
        accountsRetrieved = cursor.fetchall()
    return accountsRetrieved

# Retrieve a teachers name based on their teacher id
def getPersonNameBasedOnTeacherId(teacherId):
    with DatabaseConnection() as cursor:
        SQL = """SELECT firstName, surname
                 FROM person
                 INNER JOIN teacher ON person.id = teacher.personId
                 WHERE teacher.id = %s"""
        cursor.execute(SQL, (teacherId, ))
        nameRetrieved = cursor.fetchall()
    return nameRetrieved
