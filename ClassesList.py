#   Student Name:   Anthony Cox
#   Student ID:     C00162988
#   Date:           11th February 2015
#   Purpose:        This file contains a complete list of classes used by the system. The attributes for each of these object
#                   classes match the fields used in the MySQL database

# A School object class has attributes for all of the school details
class School:
    def __init__(self, schoolId, schoolName, addressId, streetName1, streetName2, townOrCity, county, phoneNumber, emailAddress):
        self.schoolId = schoolId
        self.schoolName = schoolName
        self.addressId = addressId
        self.streetName1 = streetName1
        self.streetName2 = streetName2
        self.townOrCity = townOrCity
        self.county = county
        self.phoneNumber = phoneNumber
        self.emailAddress = emailAddress

# An Address object class has attributes for all of the address details
class Address:
    def __init__(self, addressId, streetName1, streetName2, townOrCity, county):
        self.addressId = addressId
        self.streetName1 = streetName1
        self.streetName2 = streetName2
        self.townOrCity = townOrCity
        self.county = county

    def __eq__(self, otherObject):
        return self.__dict__ == otherObject.__dict__

# A Weekday object class has attributes for all of the weekday details
class Weekday:
    def __init__(self, weekdayId, weekdayName):
        self.weekdayId = weekdayId
        self.weekdayName = weekdayName

# An OpeningHours object class has attributes for all of the opening hours details
class OpeningHours:
    def __init__(self, openingHoursId, schoolId, weekdayId, timeId):
        self.openingHoursId = openingHoursId
        self.schoolId = schoolId
        self.weekdayId = weekdayId
        self.timeId = timeId

# A Time object class has attributes for all of the time details
class Time:
    def __init__(self, timeId, startTime, endTime):
        self.timeId = timeId
        self.startTime = startTime
        self.endTime = endTime

# A LessonName object class has an attribute only for the lesson name
class LessonName:
    def __init__(self, lessonName):
        self.lessonName = lessonName

# A FullLesson object class has attributes for all lesson details
class FullLesson:
    def __init__(self, schoollessonId, lessonName, abbreviatedName, colour):
        self.schoollessonId = schoollessonId
        self.lessonName = lessonName
        self.abbreviatedName = abbreviatedName
        self.colour = colour
    
# An OpeningHoursSettings object class has attributes for the settings the user has set in the UI
class OpeningHoursSettings:
    def __init__(self, openOrClosed, openingTime, closingTime):
        self.openOrClosed = openOrClosed
        self.openingTime = openingTime
        self.closingTime = closingTime

# A Location object class has attributes for all of the location details
class Location:
    def __init__(self, locationId, locationName, addressId, streetName1, streetName2, townOrCity, county):
        self.locationId = locationId
        self.locationName = locationName
        self.addressId = addressId
        self.streetName1 = streetName1
        self.streetName2 = streetName2
        self.townOrCity = townOrCity
        self.county = county

# A Person object class has attributes for all of the person details
class Person:
    def __init__(self, firstName, surname, dateOfBirth, phoneNumber, emailAddress):
        self.firstName = firstName
        self.surname = surname
        self.dateOfBirth = dateOfBirth
        self.phoneNumber = phoneNumber
        self.emailAddress = emailAddress

    def __eq__(self, otherObject):
        return self.__dict__ == otherObject.__dict__

# A PersonName object class only holds a students/teachers first name, surname and date of birth attributes
class PersonName:
    def __init__(self, firstName, surname, dateOfBirth):
        self.firstName = firstName
        self.surname = surname
        self.dateOfBirth = dateOfBirth

# A TeacherIdAndName object class has attributes for the teachers ID, first name and surname
class TeacherIdAndName:
    def __init__(self, teacherId, firstName, surname):
        self.teacherId = teacherId
        self.firstName = firstName
        self.surname = surname

# A TimetabledClassroom object class has attributes for the classrooms location id, location name, classroom id and classroom name
class TimetabledClassroom:
    def __init__(self, locationId, locationName, classroomId, classroomName):
        self.locationId = locationId
        self.locationName = locationName
        self.classroomId = classroomId
        self.classroomName = classroomName

# A TimetabledLesson object class has attributes for the lessons that are scheduled on the timetable
class TimetabledLesson:
    def __init__(self, timetableId, weekdayId, startHour, startMin, lessonLength, schoolId, studentId, schoolLessonId, teacherId, locationId, classroomId):
        self.timetableId = timetableId
        self.weekdayId = weekdayId
        self.startHour = startHour
        self.startMin = startMin
        self.lessonLength = lessonLength
        self.schoolId = schoolId
        self.studentId = studentId
        self.schoolLessonId = schoolLessonId
        self.teacherId = teacherId
        self.locationId = locationId
        self.classroomId = classroomId



