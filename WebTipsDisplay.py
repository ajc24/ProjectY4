#   Student Name:   Anthony Cox
#   Student ID:     C00162988
#   Date:           23rd March 2015
#   Purpose:        This file decides on all of the tutorial type displays that are to be displayed in
#                   the footer of the UI.

import random

tutorialDisplays = {
    # Login Page tutorial displays
    1: "Create~Our application allows you~to create new lessons, new~students and teachers, new~classrooms and, of course,~new timetables.", 
    2: "Edit~All of your information can~be edited at any time and~with immediate updates.~Everything has been geared~towards ease of use.",
    3: "View~View any of your timetables~at any time and in a~printable format. Likewise~all staff and students in~your school can be viewed.",
    4: "Manage~Take control of your~music school. Expand by~adding extra school locations.~Manage every students~timetable with our editor.",

    # Registration Page 1 tutorial displays
    5: "Registration~Registering your school with~us allows you to access our~system and use our key~features. We hope you~enjoy using our application.",
    6: "School Name~Enter your schools name~in the text box provided.~This name will then be~linked to your newly~registered account.",
    7: "Email Address~Use a unique email~address for your new account.~Only unique email addresses~are accepted. Don't forget~to confirm this address.",
    8: "Submit~When you are finished,~submit your school details.~We can then move you~onto the final part of~your new account registration.",

    # Registration Page 2 tutorial displays
    9: "Street Names~Enter your schools street~name(s) in these fields.~Note that only one street~name field needs to have an~entry in order to continue.",
    10: "Town or City~Use this field to enter the~town or city in which your~school is based. This field~can be changed at any~time after registration.",
    11: "Phone Number~This field is used to enter~your school phone number.~This entry accepts brackets as~well as any other special~characters you may require.",
    12: "Finish~Once you have entered all~of the information requested,~you can submit these details~to us to complete your~new account registration.",
    
    # Home Page tutorial displays
    13: "Hints & Tips~Helpful tips will display here.~These tips include:~1: General screen tips.~2: User input tips.~3: Editing tips.",
    14: "Accounts~Change your password.~Manage all user accounts.~Edit user account types.~Add and remove users.~Update user passwords.",
    15: "School~View your school details.~Edit any school details.~Change your opening hours.~Add new school locations.~Remove existing locations.",
    16: "Lessons~Add new lessons.~View any existing lessons.~Edit any lesson details.~Change lesson displays.~Remove any lessons.",
    17: "Students~Add new students.~View any existing students.~Edit personal student details.~Edit the students address.~Remove any students.",
    18: "Ensembles~Create new ensemble groups.~Add students to a group.~Remove students from groups.~Edit any ensemble details.~Feature coming soon!",
    19: "Teachers~Add new teachers.~View any existing teachers.~Edit personal teacher details.~Edit the teachers address.~Remove any teachers.",
    20: "Classrooms~Add new school classrooms.~All locations can be updated.~View any classroom.~Edit any classroom details.~Remove any classroom.",
    21: "Timetables~Edit any student timetable.~View any timetable.~Schedule new lessons.~Change scheduled lessons.~Remove scheduled lessons.",

    # Location (Add New) tutorial displays
    22: "Location Name~Enter the name for your~new location. A location name~cannot be empty and it~cannot be more than 50~characters in length.",
    23: "Street Names~Enter your locations street~name(s) in these fields.~Note that only one street~name field needs to have an~entry in order to continue.",
    24: "Town or City~Use this field to enter the~town or city in which your~location is based. This field~can be changed at any~time after setting it.",
    25: "County~Input the county in which~your new location is based.~A county name cannot be~empty and it cannot be~longer than 20 characters.",

    # School Details tutorial displays
    26: "School Name~Edit your existing~school name. This name~will then be changed and~linked to your current~school account.",
    27: "Street Names~Edit your schools street~name(s) in these fields.~Note that only one street~name field needs to have an~entry in order to continue.",
    28: "Town or City~Use this field to edit the~town or city in which your~school is based. Any changes~made will be immediately~linked to your school.",
    29: "County~Change the county in which~your school is based.~A county name cannot be~empty and it cannot be~longer than 20 characters.",
    30: "Phone Number~This field is used to edit~your schools phone number.~This entry accepts brackets as~well as any other special~characters you may require.",
    31: "Email Address~Edit the email address~linked to your school.~Only unique email addresses~are accepted. Don't forget~to confirm any changes.",

    # Opening Hours tutorial displays
    32: "Opening Hours~Manage your schools~opening hours. Don't worry,~your timetables will~automatically adjust to suit~any changes that you make.",
    33: "Open/Closed~Choose whether your school~is open or closed for~any day in the week. Note~that only days set as 'Open'~can have their hours changed.",
    34: "Opening Time~Select from a range of~hours to set your schools~opening time for each day.~Note that a day must be~at least one hour in length.",
    35: "Closing Time~You can choose your schools~closing time in the same~way as before. This time~must be set at least one~hour after the opening time.",

    # Location (Edit Existing) tutorial displays
    36: "Manage~This screen allows you~to both edit any location~details and also to remove~any existing location from~your school.",
    37: "Select~Click on a location~from the list provided in~order to access editing~options and location~removal options.",
    38: "View/Edit~Choosing this option will~allow you to change any~of the locations details.~The changes will be saved~after you submit them.",
    39: "Remove~Selecting the option to~remove a location will~permanently delete it. Note~that your main school~location cannot be removed.",

    # Lesson (Add New) tutorial displays
    40: "Lesson Name~Enter the name for your~new lesson. A lesson name~cannot be empty and it~cannot be more than 50~characters in length.",
    41: "Abbreviated~The abbreviated lesson~name is the name that will~appear on the schools~timetable when this lesson~is scheduled.",
    42: "Colour~Your selected colour acts~as the background colour~for this lesson when~it is scheduled on any~of your timetables.",
    43: "Submit~When you have finished~entering your new lessons~details, submit them to~permanently store them~in the system.",

    # Lesson (Edit Existing) tutorial displays
    44: "Search~Begin by entering a~lesson name into the search~box and clicking on the~Search button. All matching~lessons will be displayed.",
    45: "Click~Once your lessons are~displayed, simply click on~the lesson name in the table.~You can now access options~to edit or remove this lesson.",
    46: "View/Edit~Choosing this option will~allow you to change any~of the lessons details.~The changes will be saved~after you submit them.",
    47: "Remove~Selecting the option to~remove a lesson will~permanently delete it. All~matching scheduled lessons~will also be removed.",

    # Student (Add New) tutorial displays
    48: "First Name~Enter the first name for your~new student. A students first~name cannot be empty and~it cannot be more than 25~characters in length.",
    49: "Surname~Enter the surname for your~new student. The surname~cannot be empty and it~cannot be more than 25~characters in length.",
    50: "Date of Birth~Enter the students date~of birth in the format~DD/MM/YY. This is the only~accepted format for this~entry so type carefully!",
    51: "Street Names~Edit the students street~name(s) in these fields.~Note that only one street~name field needs to have an~entry in order to continue.",
    52: "Town or City~Use this field to enter the~town or city in which your~student is based. This field~can be changed at any~time after student creation.",
    53: "County~Enter the county in which~your student resides.~A county name cannot be~empty and it cannot be~longer than 20 characters.",
    54: "Phone Number~This field is used to enter~your students phone number.~This entry accepts brackets as~well as any other special~characters you may require.",
    55: "Email Address~Enter the email address~used by your student.~Only unique email addresses~are accepted. Don't forget~to confirm any changes.",

    # Student (Edit Existing) tutorial displays
    56: "Search~Begin by entering a~students name into the search~box and clicking on the~Search button. All matching~students will be displayed.",
    57: "Click~Once your students are~displayed, simply click on~the students name.~You can now access options~to edit or remove this student.",
    58: "View/Edit~Choosing this option will~allow you to change any~of the student details.~The changes will be saved~after you submit them.",
    59: "Remove~Selecting the option to~remove a student will~permanently delete them. All~subsequent timetables for this~student will also be removed.",

    # Teacher (Add New) tutorial displays
    60: "First Name~Enter the first name for your~new teacher. A teachers first~name cannot be empty and~it cannot be more than 25~characters in length.",
    61: "Surname~Enter the surname for your~new teacher. The surname~cannot be empty and it~cannot be more than 25~characters in length.",
    62: "Date of Birth~Enter the teachers date~of birth in the format~DD/MM/YY. This is the only~accepted format for this~entry so type carefully!",
    63: "Street Names~Edit the teacher street~name(s) in these fields.~Note that only one street~name field needs to have an~entry in order to continue.",
    64: "Town or City~Use this field to enter the~town or city in which your~teacher is based. This field~can be changed at any~time after student creation.",
    65: "County~Enter the county in which~your teacher resides.~A county name cannot be~empty and it cannot be~longer than 20 characters.",
    66: "Phone Number~This field is used to enter~your teachers phone number.~This entry accepts brackets as~well as any other special~characters you may require.",
    67: "Email Address~Enter the email address~used by your teacher.~Only unique email addresses~are accepted. Don't forget~to confirm any changes.",

    # Teacher (Edit Existing) tutorial displays
    68: "Search~Begin by entering a~teachers name into the search~box and clicking on the~Search button. All matching~teachers will be displayed.",
    69: "Click~Once your teachers are~displayed, simply click on~the teachers name.~You can now access options~to edit or remove this teacher.",
    70: "View/Edit~Choosing this option will~allow you to change any~of the teacher details.~The changes will be saved~after you submit them.",
    71: "Remove~Selecting the option to~remove a teacher will~permanently delete them. All~lessons scheduled to this~teacher will also be removed.",

    # Accounts - Edit School Account tutorial displays
    72: "Current~Enter your current~account password. Your~account password cannot~be changed without first~entering this password.",
    73: "New~Once you have entered~your current password,~you can then enter a~new password which is to be~linked to your account.",
    74: "Confirm~Don't forget to confirm~your new password. You~cannot submit your new~password request without~confirming it.",
    75: "Submit~Once you have finished~entering your details,~you must submit them~in order to make the changes~to your account.",

    # Accounts - Manage Teacher Account tutorial displays
    76: "Search~Begin by entering a~teachers name into the search~box and clicking on the~Search button. All matching~teachers will be displayed.",
    77: "Create~Click on the teachers~name to access account~options. If the teacher has~not had an account set up for~them, you can create one.",
    78: "Reset~If you wish to reset the~teachers account, click on~their name and select the~Reset Account option. You~can now reset their account.",
    79: "Remove~Clicking on the teachers~name also provides an~option to remove the teachers~account. Removed accounts~can no longer log in.",

    # Accounts - Manage Student Account tutorial displays
    80: "Search~Begin by entering a~students name into the search~box and clicking on the~Search button. All matching~students will be displayed.",
    81: "Create~Click on the students~name to access account~options. If the student has~not had an account set up for~them, you can create one.",
    82: "Reset~If you wish to reset the~students account, click on~their name and select the~Reset Account option. You~can now reset their account.",
    83: "Remove~Clicking on the students~name also provides an~option to remove the students~account. Removed accounts~can no longer log in.",

    # Classroom (Add New) tutorial displays
    84: "Add~This screen allows you~to add a new classroom~to any location linked~to your school. New rooms can~be used in your timetables.",
    85: "Location~Select an existing~location associated with~your school from the~list of linked school~locations provided.",
    86: "Room Name~Enter a room name to~be linked to this location.~Room names can be a~maximum of 10 characters~in length.",
    87: "Submit~When you have selected~your location and entered~a room name, submit your~entries to permanently~store them in the system.",

    # Classroom (View/Edit/Remove) tutorial displays
    88: "Select~Select an existing~location associated with~your school from the~list of linked school~locations provided.",
    89: "Click~Once you have chosen~a location, the list of~rooms associated with~that room are listed.~Click any one of them.",
    90: "View/Edit~Choosing this option will~allow you to change any~of the rooms details.~The changes will be saved~after you submit them.",
    91: "Remove~Selecting the option to~remove a room will~permanently delete it. All~lessons scheduled to this~room will also be removed.",

    # Timetable (Manage Student Timetable) tutorial displays
    92: "Search~Begin by entering a~students name into the search~box and clicking on the~Search button. All matching~students will be displayed.",
    93: "Click~Once your students are~displayed, simply click on~the students name.~You can now access options~to manage their timetable.",
    94: "Add~Add new lessons to~this students timetable.~The editor automatically~saves all changes that~you make.",
    95: "Edit~Drag and drop lessons~to reschedule them.~Alternatively, you can~remove existing lessons~from the timetable.",

    # Timetable (View Classroom Timetable) tutorial displays
    96: "Select~Select an existing~location associated with~your school from the~list of linked school~locations provided.",
    97: "Click~Once you have chosen~a location, the list of~rooms associated with~that room are listed.~Click any one of them.",
    98: "View~After clicking on a~classroom, its timetable~will be displayed.~You cannot edit this~timetable in any way.",
    99: "Print~The timetable will be~deliberately output in a~printable format (no colour).~If you wish, it can~then be printed.",

    # Timetable (View Teacher Timetable) tutorial displays
    100: "Search~Begin by entering a~teachers name into the search~box and clicking on the~Search button. All matching~teachers will be displayed.",
    101: "Click~Once your teachers are~displayed, simply click on~the teachers name.~You can now view this~teachers timetable.",
    102: "View~After clicking on a~teacher, his/her timetable~will then be displayed.~You cannot edit this~timetable in any way.",
    103: "Print~The timetable will be~deliberately output in a~printable format (no colour).~If you wish, it can~then be printed.",

    # Timetable (View Student Timetable) tutorial displays
    104: "Search~Begin by entering a~students name into the search~box and clicking on the~Search button. All matching~students will be displayed.",
    105: "Click~Once your students are~displayed, simply click on~the students name.~You can now view this~students timetable.",
    106: "View~After clicking on a~student, his/her timetable~will then be displayed.~You cannot edit this~timetable in any way.",
    107: "Print~The timetable will be~deliberately output in a~printable format (no colour).~If you wish, it can~then be printed.",
}               

# Determine all of the headings and subsequent content that will be displayed in the footer section of the UI (random selection)
def determineFooterTutorialDisplayByRandom(startRange, endRange):
    numberOfSelections = 0
    maxNumberOfSelections = 4
    listOfRandomNumbers = []
    listOfDisplays = []

    while numberOfSelections < maxNumberOfSelections:
        currentRandom = random.randint(startRange, endRange)
        while currentRandom in listOfRandomNumbers:
            currentRandom = random.randint(startRange, endRange)
        listOfRandomNumbers.append(currentRandom)
        listOfDisplays.append(tutorialDisplays[currentRandom])
        numberOfSelections += 1

    return listOfDisplays

# Get the list of tutorial displays based on a specified range of numbers
def determineFooterTutorialDisplayByRange(startRange, endRange):
    listOfDisplays = []
    currentIndex = startRange
    
    while currentIndex <= endRange:
        listOfDisplays.append(tutorialDisplays[currentIndex])
        currentIndex += 1

    return listOfDisplays
    
    
