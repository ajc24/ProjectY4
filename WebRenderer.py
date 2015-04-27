#   Student Name:   Anthony Cox
#   Student ID:     C00162988
#   Date:           9th February 2015
#   Purpose:        The main application file. This file renders all of the pages in the browser.
#                   Any data that requires processing between rendered pages is forwarded from here to the DataProcessing file.

import WebValidation
import WebTipsDisplay
import DataProcessing
import ClassesList
from flask import Flask, render_template, request, url_for, session, json

app = Flask(__name__)

#===== Login and First Time Registration Screens ====================================================================================================================

@app.route("/")
def display_login_page():
    resetAllSessionVariables()
    footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(1, 4)
    return render_template("loginScreen.html",
                           logged_in = session.get("loggedIn"),
                           register_new_school_url = url_for("display_register_new_school_first_page"),
                           footer_one = footerDisplays[0],
                           footer_two = footerDisplays[1],
                           footer_three = footerDisplays[2],
                           footer_four = footerDisplays[3], )

@app.route("/registerNewSchoolPage1")
def display_register_new_school_first_page():
    resetAllSessionVariables()
    footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(5, 8)
    return render_template("registerNewSchoolPage1.html",
                           logged_in = session.get("loggedIn"),
                           login_screen_url = url_for("display_login_page"),
                           footer_one = footerDisplays[0],
                           footer_two = footerDisplays[1],
                           footer_three = footerDisplays[2],
                           footer_four = footerDisplays[3], )

@app.route("/registerNewSchoolPage2")
def display_register_new_school_second_page():
    if session.get("schoolName") == "Not set" or session.get("schoolName") is None:
        session["loggedIn"] = False
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(1, 4)
        return render_template("errorRegistration.html",
                               logged_in = session.get("loggedIn"),
                               login_screen_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3], )
    else:
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(9, 12)
        return render_template("registerNewSchoolPage2.html",
                               logged_in = session.get("loggedIn"),
                               login_screen_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3], )

@app.route("/registrationComplete")
def display_registration_complete_page():
    footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(1, 4)
    if session.get("registered") == False or session.get("registered") is None:
        session["loggedIn"] = False
        return render_template("errorRegistrationComplete.html",
                               logged_in = session.get("loggedIn"),
                               login_screen_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3], )
    else:
        session["registered"] = False
        return render_template("registerNewSchoolSuccessful.html",
                               logged_in = session.get("loggedIn"),
                               login_screen_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3], )

#===== Home Page and Menu Selection Screens =========================================================================================================================

@app.route("/homePage")
def display_home_page():
    if session.get("loggedIn") == False or session.get("loggedIn") is None:
        session["loggedIn"] = False
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(1, 4)
        return render_template("errorNotLoggedIn.html",
                               logged_in = session.get("loggedIn"),
                               login_screen_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3], )
    else:
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRandom(13, 21)
        return render_template("homePage.html",
                               page_title = "Music Manager Home Page",
                               school_name = session.get("loginName"),
                               logged_in = session.get("loggedIn"),
                               account_type = session.get("accountType"),
                               login_id = session.get("loginId"),
                               home_page_url = url_for("display_home_page"),
                               manage_your_account_url = url_for("display_change_account_password"),
                               manage_teacher_accounts_url = url_for("display_manage_teacher_accounts_page"),
                               manage_student_accounts_url = url_for("display_manage_student_accounts_page"),
                               add_new_location_url = url_for("add_new_location"),
                               edit_school_details_url = url_for("manage_school_details"),
                               edit_opening_hours_url = url_for("manage_school_opening_hours"),
                               manage_locations_url = url_for("view_edit_locations"),
                               add_new_lesson_url = url_for("add_new_lesson"),
                               view_edit_lessons_url = url_for("view_edit_lessons"),
                               add_new_student_url = url_for("add_new_student"),
                               view_edit_students_url = url_for("view_edit_students"),
                               add_new_teacher_url = url_for("add_new_teacher"),
                               view_edit_teachers_url = url_for("view_edit_teachers"),
                               add_new_ensemble_group_url = url_for("add_new_ensemble"),
                               manage_ensemble_groups_url = url_for("view_edit_ensemble_groups"),
                               add_new_classroom_url = url_for("add_new_classroom"),
                               view_edit_classrooms_url = url_for("view_edit_classrooms"),
                               manage_a_student_timetable_url = url_for("manage_timetables"),
                               view_a_classroom_timetable_url = url_for("select_classroom_timetable"),
                               view_a_teacher_timetable_url = url_for("select_teacher_timetable"),
                               view_a_student_timetable_url = url_for("select_student_timetable"),
                               about_this_project_url = url_for("display_about_this_project_page"),
                               log_out_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3], )

@app.route("/aboutThisProject")
def display_about_this_project_page():
    if session.get("loggedIn") == False or session.get("loggedIn") is None:
        session["loggedIn"] = False
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(1, 4)
        return render_template("errorNotLoggedIn.html",
                               logged_in = session.get("loggedIn"),
                               login_screen_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3], )
    else:
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRandom(13, 21)
        return render_template("aboutThisProject.html",
                               page_title = "About This Project",
                               school_name = session.get("loginName"),
                               logged_in = session.get("loggedIn"),
                               account_type = session.get("accountType"),
                               login_id = session.get("loginId"),
                               home_page_url = url_for("display_home_page"),
                               manage_your_account_url = url_for("display_change_account_password"),
                               manage_teacher_accounts_url = url_for("display_manage_teacher_accounts_page"),
                               manage_student_accounts_url = url_for("display_manage_student_accounts_page"),
                               add_new_location_url = url_for("add_new_location"),
                               edit_school_details_url = url_for("manage_school_details"),
                               edit_opening_hours_url = url_for("manage_school_opening_hours"),
                               manage_locations_url = url_for("view_edit_locations"),
                               add_new_lesson_url = url_for("add_new_lesson"),
                               view_edit_lessons_url = url_for("view_edit_lessons"),
                               add_new_student_url = url_for("add_new_student"),
                               view_edit_students_url = url_for("view_edit_students"),
                               add_new_teacher_url = url_for("add_new_teacher"),
                               view_edit_teachers_url = url_for("view_edit_teachers"),
                               add_new_ensemble_group_url = url_for("add_new_ensemble"),
                               manage_ensemble_groups_url = url_for("view_edit_ensemble_groups"),
                               add_new_classroom_url = url_for("add_new_classroom"),
                               view_edit_classrooms_url = url_for("view_edit_classrooms"),
                               manage_a_student_timetable_url = url_for("manage_timetables"),
                               view_a_classroom_timetable_url = url_for("select_classroom_timetable"),
                               view_a_teacher_timetable_url = url_for("select_teacher_timetable"),
                               view_a_student_timetable_url = url_for("select_student_timetable"),
                               about_this_project_url = url_for("display_about_this_project_page"),
                               log_out_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3], )

#===== School Management Screens ====================================================================================================================================

@app.route("/addNewLocation")
def add_new_location():
    if session.get("loggedIn") == False or session.get("loggedIn") is None or session.get("accountType") != "Administrator":
        session["loggedIn"] = False
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(1, 4)
        return render_template("errorNotLoggedIn.html",
                               logged_in = session.get("loggedIn"),
                               login_screen_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3], )
    else:
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(22, 25)
        return render_template("locationAddNew.html",
                               page_title = "Add New School Location",
                               home_page_url = url_for("display_home_page"),
                               school_name = session.get("loginName"),
                               logged_in = session.get("loggedIn"),
                               account_type = session.get("accountType"),
                               login_id = session.get("loginId"),
                               manage_your_account_url = url_for("display_change_account_password"),
                               manage_teacher_accounts_url = url_for("display_manage_teacher_accounts_page"),
                               manage_student_accounts_url = url_for("display_manage_student_accounts_page"),
                               add_new_location_url = url_for("add_new_location"),
                               edit_school_details_url = url_for("manage_school_details"),
                               edit_opening_hours_url = url_for("manage_school_opening_hours"),
                               manage_locations_url = url_for("view_edit_locations"),
                               add_new_lesson_url = url_for("add_new_lesson"),
                               view_edit_lessons_url = url_for("view_edit_lessons"),
                               add_new_student_url = url_for("add_new_student"),
                               view_edit_students_url = url_for("view_edit_students"),
                               add_new_teacher_url = url_for("add_new_teacher"),
                               view_edit_teachers_url = url_for("view_edit_teachers"),
                               add_new_ensemble_group_url = url_for("add_new_ensemble"),
                               manage_ensemble_groups_url = url_for("view_edit_ensemble_groups"),
                               add_new_classroom_url = url_for("add_new_classroom"),
                               view_edit_classrooms_url = url_for("view_edit_classrooms"),
                               manage_a_student_timetable_url = url_for("manage_timetables"),
                               view_a_classroom_timetable_url = url_for("select_classroom_timetable"),
                               view_a_teacher_timetable_url = url_for("select_teacher_timetable"),
                               view_a_student_timetable_url = url_for("select_student_timetable"),
                               about_this_project_url = url_for("display_about_this_project_page"),
                               log_out_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3],
                               current_school_id = session.get("loginId"), )

@app.route("/viewEditSchoolDetails")
def manage_school_details():
    if session.get("loggedIn") == False or session.get("loggedIn") is None or session.get("accountType") != "Administrator":
        session["loggedIn"] = False
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(1, 4)
        return render_template("errorNotLoggedIn.html",
                               logged_in = session.get("loggedIn"),
                               login_screen_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3], )
    else:
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRandom(26, 31)
        schoolDetails = DataProcessing.getSchoolDetails(session.get("loginId"))
        return render_template("schoolViewEditDetails.html",
                               page_title = "View/Edit School Details",
                               home_page_url = url_for("display_home_page"),
                               school_name = session.get("loginName"),
                               logged_in = session.get("loggedIn"),
                               account_type = session.get("accountType"),
                               login_id = session.get("loginId"),
                               manage_your_account_url = url_for("display_change_account_password"),
                               manage_teacher_accounts_url = url_for("display_manage_teacher_accounts_page"),
                               manage_student_accounts_url = url_for("display_manage_student_accounts_page"),
                               add_new_location_url = url_for("add_new_location"),
                               edit_school_details_url = url_for("manage_school_details"),
                               edit_opening_hours_url = url_for("manage_school_opening_hours"),
                               manage_locations_url = url_for("view_edit_locations"),
                               add_new_lesson_url = url_for("add_new_lesson"),
                               view_edit_lessons_url = url_for("view_edit_lessons"),
                               add_new_student_url = url_for("add_new_student"),
                               view_edit_students_url = url_for("view_edit_students"),
                               add_new_teacher_url = url_for("add_new_teacher"),
                               view_edit_teachers_url = url_for("view_edit_teachers"),
                               add_new_ensemble_group_url = url_for("add_new_ensemble"),
                               manage_ensemble_groups_url = url_for("view_edit_ensemble_groups"),
                               add_new_classroom_url = url_for("add_new_classroom"),
                               view_edit_classrooms_url = url_for("view_edit_classrooms"),
                               manage_a_student_timetable_url = url_for("manage_timetables"),
                               view_a_classroom_timetable_url = url_for("select_classroom_timetable"),
                               view_a_teacher_timetable_url = url_for("select_teacher_timetable"),
                               view_a_student_timetable_url = url_for("select_student_timetable"),
                               about_this_project_url = url_for("display_about_this_project_page"),
                               log_out_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3],
                               school = schoolDetails, )

@app.route("/editSchoolOpeningHours")
def manage_school_opening_hours():
    if session.get("loggedIn") == False or session.get("loggedIn") is None or session.get("accountType") != "Administrator":
        session["loggedIn"] = False
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(1, 4)
        return render_template("errorNotLoggedIn.html",
                               logged_in = session.get("loggedIn"),
                               login_screen_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3], )
    else:
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(32, 35)
        storedDaysAndHoursList = DataProcessing.getSchoolOpeningHours(session.get("loginId"))
        return render_template("schoolManageOpeningHours.html",
                               page_title = "Manage Your Schools Opening Hours",
                               home_page_url = url_for("display_home_page"),
                               school_name = session.get("loginName"),
                               logged_in = session.get("loggedIn"),
                               account_type = session.get("accountType"),
                               login_id = session.get("loginId"),
                               manage_your_account_url = url_for("display_change_account_password"),
                               manage_teacher_accounts_url = url_for("display_manage_teacher_accounts_page"),
                               manage_student_accounts_url = url_for("display_manage_student_accounts_page"),
                               add_new_location_url = url_for("add_new_location"),
                               edit_school_details_url = url_for("manage_school_details"),
                               edit_opening_hours_url = url_for("manage_school_opening_hours"),
                               manage_locations_url = url_for("view_edit_locations"),
                               add_new_lesson_url = url_for("add_new_lesson"),
                               view_edit_lessons_url = url_for("view_edit_lessons"),
                               add_new_student_url = url_for("add_new_student"),
                               view_edit_students_url = url_for("view_edit_students"),
                               add_new_teacher_url = url_for("add_new_teacher"),
                               view_edit_teachers_url = url_for("view_edit_teachers"),
                               add_new_ensemble_group_url = url_for("add_new_ensemble"),
                               manage_ensemble_groups_url = url_for("view_edit_ensemble_groups"),
                               add_new_classroom_url = url_for("add_new_classroom"),
                               view_edit_classrooms_url = url_for("view_edit_classrooms"),
                               manage_a_student_timetable_url = url_for("manage_timetables"),
                               view_a_classroom_timetable_url = url_for("select_classroom_timetable"),
                               view_a_teacher_timetable_url = url_for("select_teacher_timetable"),
                               view_a_student_timetable_url = url_for("select_student_timetable"),
                               about_this_project_url = url_for("display_about_this_project_page"),
                               log_out_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3],
                               list_of_weekdays = storedDaysAndHoursList[0],
                               list_of_opening_hours = storedDaysAndHoursList[1],
                               list_of_times = storedDaysAndHoursList[2], )

@app.route("/editSchoolLocations")
def view_edit_locations():
    if session.get("loggedIn") == False or session.get("loggedIn") is None or session.get("accountType") != "Administrator":
        session["loggedIn"] = False
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(1, 4)
        return render_template("errorNotLoggedIn.html",
                               logged_in = session.get("loggedIn"),
                               login_screen_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3], )
    else:
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(36, 39)
        locationsList = DataProcessing.getListOfSchoolLocations(session.get("loginId"))
        return render_template("locationViewEditDetails.html",
                               page_title = "Manage Your Schools Opening Hours",
                               home_page_url = url_for("display_home_page"),
                               school_name = session.get("loginName"),
                               logged_in = session.get("loggedIn"),
                               account_type = session.get("accountType"),
                               login_id = session.get("loginId"),
                               manage_your_account_url = url_for("display_change_account_password"),
                               manage_teacher_accounts_url = url_for("display_manage_teacher_accounts_page"),
                               manage_student_accounts_url = url_for("display_manage_student_accounts_page"),
                               add_new_location_url = url_for("add_new_location"),
                               edit_school_details_url = url_for("manage_school_details"),
                               edit_opening_hours_url = url_for("manage_school_opening_hours"),
                               manage_locations_url = url_for("view_edit_locations"),
                               add_new_lesson_url = url_for("add_new_lesson"),
                               view_edit_lessons_url = url_for("view_edit_lessons"),
                               add_new_student_url = url_for("add_new_student"),
                               view_edit_students_url = url_for("view_edit_students"),
                               add_new_teacher_url = url_for("add_new_teacher"),
                               view_edit_teachers_url = url_for("view_edit_teachers"),
                               add_new_ensemble_group_url = url_for("add_new_ensemble"),
                               manage_ensemble_groups_url = url_for("view_edit_ensemble_groups"),
                               add_new_classroom_url = url_for("add_new_classroom"),
                               view_edit_classrooms_url = url_for("view_edit_classrooms"),
                               manage_a_student_timetable_url = url_for("manage_timetables"),
                               view_a_classroom_timetable_url = url_for("select_classroom_timetable"),
                               view_a_teacher_timetable_url = url_for("select_teacher_timetable"),
                               view_a_student_timetable_url = url_for("select_student_timetable"),
                               about_this_project_url = url_for("display_about_this_project_page"),
                               log_out_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3], 
                               current_school_id = session.get("loginId"),
                               list_of_locations = locationsList, )

#===== Accounts Management Screens ==================================================================================================================================

@app.route("/changeYourAccountPassword")
def display_change_account_password():
    if session.get("loggedIn") == False or session.get("loggedIn") is None:
        session["loggedIn"] = False
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(1, 4)
        return render_template("errorNotLoggedIn.html",
                               logged_in = session.get("loggedIn"),
                               login_screen_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3], )
    else:
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(72, 75)
        return render_template("usersManageSchoolAccounts.html",
                               page_title = "Change Your School Account Password",
                               home_page_url = url_for("display_home_page"),
                               school_name = session.get("loginName"),
                               logged_in = session.get("loggedIn"),
                               account_type = session.get("accountType"),
                               login_id = session.get("loginId"),
                               manage_your_account_url = url_for("display_change_account_password"),
                               manage_teacher_accounts_url = url_for("display_manage_teacher_accounts_page"),
                               manage_student_accounts_url = url_for("display_manage_student_accounts_page"),
                               add_new_location_url = url_for("add_new_location"),
                               edit_school_details_url = url_for("manage_school_details"),
                               edit_opening_hours_url = url_for("manage_school_opening_hours"),
                               manage_locations_url = url_for("view_edit_locations"),
                               add_new_lesson_url = url_for("add_new_lesson"),
                               view_edit_lessons_url = url_for("view_edit_lessons"),
                               add_new_student_url = url_for("add_new_student"),
                               view_edit_students_url = url_for("view_edit_students"),
                               add_new_teacher_url = url_for("add_new_teacher"),
                               view_edit_teachers_url = url_for("view_edit_teachers"),
                               add_new_ensemble_group_url = url_for("add_new_ensemble"),
                               manage_ensemble_groups_url = url_for("view_edit_ensemble_groups"),
                               add_new_classroom_url = url_for("add_new_classroom"),
                               view_edit_classrooms_url = url_for("view_edit_classrooms"),
                               manage_a_student_timetable_url = url_for("manage_timetables"),
                               view_a_classroom_timetable_url = url_for("select_classroom_timetable"),
                               view_a_teacher_timetable_url = url_for("select_teacher_timetable"),
                               view_a_student_timetable_url = url_for("select_student_timetable"),
                               about_this_project_url = url_for("display_about_this_project_page"),
                               log_out_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3],
                               current_school_id = session.get("loginId"), )

@app.route("/manageTeacherAccounts")
def display_manage_teacher_accounts_page():
    if session.get("loggedIn") == False or session.get("loggedIn") is None or session.get("accountType") != "Administrator":
        session["loggedIn"] = False
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(1, 4)
        return render_template("errorNotLoggedIn.html",
                               logged_in = session.get("loggedIn"),
                               login_screen_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3], )
    else:
        listOfSchoolTeacherNames = DataProcessing.getSchoolTeachersNamesList(session.get("loginId"))
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(76, 79)
        return render_template("usersManageTeacherAccounts.html",
                               page_title = "Manage Your Teachers Accounts",
                               home_page_url = url_for("display_home_page"),
                               school_name = session.get("loginName"),
                               logged_in = session.get("loggedIn"),
                               account_type = session.get("accountType"),
                               login_id = session.get("loginId"),
                               manage_your_account_url = url_for("display_change_account_password"),
                               manage_teacher_accounts_url = url_for("display_manage_teacher_accounts_page"),
                               manage_student_accounts_url = url_for("display_manage_student_accounts_page"),
                               add_new_location_url = url_for("add_new_location"),
                               edit_school_details_url = url_for("manage_school_details"),
                               edit_opening_hours_url = url_for("manage_school_opening_hours"),
                               manage_locations_url = url_for("view_edit_locations"),
                               add_new_lesson_url = url_for("add_new_lesson"),
                               view_edit_lessons_url = url_for("view_edit_lessons"),
                               add_new_student_url = url_for("add_new_student"),
                               view_edit_students_url = url_for("view_edit_students"),
                               add_new_teacher_url = url_for("add_new_teacher"),
                               view_edit_teachers_url = url_for("view_edit_teachers"),
                               add_new_ensemble_group_url = url_for("add_new_ensemble"),
                               manage_ensemble_groups_url = url_for("view_edit_ensemble_groups"),
                               add_new_classroom_url = url_for("add_new_classroom"),
                               view_edit_classrooms_url = url_for("view_edit_classrooms"),
                               manage_a_student_timetable_url = url_for("manage_timetables"),
                               view_a_classroom_timetable_url = url_for("select_classroom_timetable"),
                               view_a_teacher_timetable_url = url_for("select_teacher_timetable"),
                               view_a_student_timetable_url = url_for("select_student_timetable"),
                               about_this_project_url = url_for("display_about_this_project_page"),
                               log_out_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3],
                               current_school_id = session.get("loginId"),
                               list_of_persons = listOfSchoolTeacherNames, )

@app.route("/manageStudentAccounts")
def display_manage_student_accounts_page():
    if session.get("loggedIn") == False or session.get("loggedIn") is None or session.get("accountType") != "Administrator":
        session["loggedIn"] = False
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(1, 4)
        return render_template("errorNotLoggedIn.html",
                               logged_in = session.get("loggedIn"),
                               login_screen_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3], )
    else:
        listOfSchoolStudentNames = DataProcessing.getSchoolStudentsNamesList(session.get("loginId"))
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(80, 83)
        return render_template("usersManageStudentAccounts.html",
                               page_title = "Manage Your Students Accounts",
                               home_page_url = url_for("display_home_page"),
                               school_name = session.get("loginName"),
                               logged_in = session.get("loggedIn"),
                               account_type = session.get("accountType"),
                               login_id = session.get("loginId"),
                               manage_your_account_url = url_for("display_change_account_password"),
                               manage_teacher_accounts_url = url_for("display_manage_teacher_accounts_page"),
                               manage_student_accounts_url = url_for("display_manage_student_accounts_page"),
                               add_new_location_url = url_for("add_new_location"),
                               edit_school_details_url = url_for("manage_school_details"),
                               edit_opening_hours_url = url_for("manage_school_opening_hours"),
                               manage_locations_url = url_for("view_edit_locations"),
                               add_new_lesson_url = url_for("add_new_lesson"),
                               view_edit_lessons_url = url_for("view_edit_lessons"),
                               add_new_student_url = url_for("add_new_student"),
                               view_edit_students_url = url_for("view_edit_students"),
                               add_new_teacher_url = url_for("add_new_teacher"),
                               view_edit_teachers_url = url_for("view_edit_teachers"),
                               add_new_ensemble_group_url = url_for("add_new_ensemble"),
                               manage_ensemble_groups_url = url_for("view_edit_ensemble_groups"),
                               add_new_classroom_url = url_for("add_new_classroom"),
                               view_edit_classrooms_url = url_for("view_edit_classrooms"),
                               manage_a_student_timetable_url = url_for("manage_timetables"),
                               view_a_classroom_timetable_url = url_for("select_classroom_timetable"),
                               view_a_teacher_timetable_url = url_for("select_teacher_timetable"),
                               view_a_student_timetable_url = url_for("select_student_timetable"),
                               about_this_project_url = url_for("display_about_this_project_page"),
                               log_out_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3],
                               current_school_id = session.get("loginId"),
                               list_of_persons = listOfSchoolStudentNames, )

#===== Lesson Management Screens ====================================================================================================================================

@app.route("/addNewLesson")
def add_new_lesson():
    if session.get("loggedIn") == False or session.get("loggedIn") is None or session.get("accountType") != "Administrator":
        session["loggedIn"] = False
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(1, 4)
        return render_template("errorNotLoggedIn.html",
                               logged_in = session.get("loggedIn"),
                               login_screen_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3], )
    else:
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(40, 43)
        return render_template("lessonAddNew.html",
                               page_title = "Add New Lesson",
                               home_page_url = url_for("display_home_page"),
                               school_name = session.get("loginName"),
                               logged_in = session.get("loggedIn"),
                               account_type = session.get("accountType"),
                               login_id = session.get("loginId"),
                               manage_your_account_url = url_for("display_change_account_password"),
                               manage_teacher_accounts_url = url_for("display_manage_teacher_accounts_page"),
                               manage_student_accounts_url = url_for("display_manage_student_accounts_page"),
                               add_new_location_url = url_for("add_new_location"),
                               edit_school_details_url = url_for("manage_school_details"),
                               edit_opening_hours_url = url_for("manage_school_opening_hours"),
                               manage_locations_url = url_for("view_edit_locations"),
                               add_new_lesson_url = url_for("add_new_lesson"),
                               view_edit_lessons_url = url_for("view_edit_lessons"),
                               add_new_student_url = url_for("add_new_student"),
                               view_edit_students_url = url_for("view_edit_students"),
                               add_new_teacher_url = url_for("add_new_teacher"),
                               view_edit_teachers_url = url_for("view_edit_teachers"),
                               add_new_ensemble_group_url = url_for("add_new_ensemble"),
                               manage_ensemble_groups_url = url_for("view_edit_ensemble_groups"),
                               add_new_classroom_url = url_for("add_new_classroom"),
                               view_edit_classrooms_url = url_for("view_edit_classrooms"),
                               manage_a_student_timetable_url = url_for("manage_timetables"),
                               view_a_classroom_timetable_url = url_for("select_classroom_timetable"),
                               view_a_teacher_timetable_url = url_for("select_teacher_timetable"),
                               view_a_student_timetable_url = url_for("select_student_timetable"),
                               about_this_project_url = url_for("display_about_this_project_page"),
                               log_out_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3],
                               current_school_id = session.get("loginId"), )

@app.route("/viewEditLessonDetails")
def view_edit_lessons():
    if session.get("loggedIn") == False or session.get("loggedIn") is None or session.get("accountType") != "Administrator":
        session["loggedIn"] = False
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(1, 4)
        return render_template("errorNotLoggedIn.html",
                               logged_in = session.get("loggedIn"),
                               login_screen_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3], )
    else:
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(44, 47)
        listOfLessonNames = DataProcessing.getSchoolLessonsList(session.get("loginId"))
        return render_template("lessonViewEditDetails.html",
                               page_title = "View/Edit Your Lessons",
                               home_page_url = url_for("display_home_page"),
                               school_name = session.get("loginName"),
                               logged_in = session.get("loggedIn"),
                               account_type = session.get("accountType"),
                               login_id = session.get("loginId"),
                               manage_your_account_url = url_for("display_change_account_password"),
                               manage_teacher_accounts_url = url_for("display_manage_teacher_accounts_page"),
                               manage_student_accounts_url = url_for("display_manage_student_accounts_page"),
                               add_new_location_url = url_for("add_new_location"),
                               edit_school_details_url = url_for("manage_school_details"),
                               edit_opening_hours_url = url_for("manage_school_opening_hours"),
                               manage_locations_url = url_for("view_edit_locations"),
                               add_new_lesson_url = url_for("add_new_lesson"),
                               view_edit_lessons_url = url_for("view_edit_lessons"),
                               add_new_student_url = url_for("add_new_student"),
                               view_edit_students_url = url_for("view_edit_students"),
                               add_new_teacher_url = url_for("add_new_teacher"),
                               view_edit_teachers_url = url_for("view_edit_teachers"),
                               add_new_ensemble_group_url = url_for("add_new_ensemble"),
                               manage_ensemble_groups_url = url_for("view_edit_ensemble_groups"),
                               add_new_classroom_url = url_for("add_new_classroom"),
                               view_edit_classrooms_url = url_for("view_edit_classrooms"),
                               manage_a_student_timetable_url = url_for("manage_timetables"),
                               view_a_classroom_timetable_url = url_for("select_classroom_timetable"),
                               view_a_teacher_timetable_url = url_for("select_teacher_timetable"),
                               view_a_student_timetable_url = url_for("select_student_timetable"),
                               about_this_project_url = url_for("display_about_this_project_page"),
                               log_out_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3], 
                               list_of_lessons = listOfLessonNames,
                               current_school_id = session.get("loginId"), )

#===== Student Management Screens ===================================================================================================================================

@app.route("/addNewStudent")
def add_new_student():
    if session.get("loggedIn") == False or session.get("loggedIn") is None or session.get("accountType") != "Administrator":
        session["loggedIn"] = False
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(1, 4)
        return render_template("errorNotLoggedIn.html",
                               logged_in = session.get("loggedIn"),
                               login_screen_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3], )
    else:
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRandom(48, 55)
        return render_template("studentAddNew.html",
                               page_title = "Add New Student",
                               home_page_url = url_for("display_home_page"),
                               school_name = session.get("loginName"),
                               logged_in = session.get("loggedIn"),
                               account_type = session.get("accountType"),
                               login_id = session.get("loginId"),
                               manage_your_account_url = url_for("display_change_account_password"),
                               manage_teacher_accounts_url = url_for("display_manage_teacher_accounts_page"),
                               manage_student_accounts_url = url_for("display_manage_student_accounts_page"),
                               add_new_location_url = url_for("add_new_location"),
                               edit_school_details_url = url_for("manage_school_details"),
                               edit_opening_hours_url = url_for("manage_school_opening_hours"),
                               manage_locations_url = url_for("view_edit_locations"),
                               add_new_lesson_url = url_for("add_new_lesson"),
                               view_edit_lessons_url = url_for("view_edit_lessons"),
                               add_new_student_url = url_for("add_new_student"),
                               view_edit_students_url = url_for("view_edit_students"),
                               add_new_teacher_url = url_for("add_new_teacher"),
                               view_edit_teachers_url = url_for("view_edit_teachers"),
                               add_new_ensemble_group_url = url_for("add_new_ensemble"),
                               manage_ensemble_groups_url = url_for("view_edit_ensemble_groups"),
                               add_new_classroom_url = url_for("add_new_classroom"),
                               view_edit_classrooms_url = url_for("view_edit_classrooms"),
                               manage_a_student_timetable_url = url_for("manage_timetables"),
                               view_a_classroom_timetable_url = url_for("select_classroom_timetable"),
                               view_a_teacher_timetable_url = url_for("select_teacher_timetable"),
                               view_a_student_timetable_url = url_for("select_student_timetable"),
                               about_this_project_url = url_for("display_about_this_project_page"),
                               log_out_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3],  
                               current_school_id = session.get("loginId"), )

@app.route("/viewEditStudentDetails")
def view_edit_students():
    if session.get("loggedIn") == False or session.get("loggedIn") is None or session.get("accountType") != "Administrator":
        session["loggedIn"] = False
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(1, 4)
        return render_template("errorNotLoggedIn.html",
                               logged_in = session.get("loggedIn"),
                               login_screen_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3], )
    else:
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(56, 59)
        listOfSchoolStudentNames = DataProcessing.getSchoolStudentsNamesList(session.get("loginId"))
        return render_template("studentViewEditDetails.html",
                               page_title = "View/Edit Your Students",
                               home_page_url = url_for("display_home_page"),
                               school_name = session.get("loginName"),
                               logged_in = session.get("loggedIn"),
                               account_type = session.get("accountType"),
                               login_id = session.get("loginId"),
                               manage_your_account_url = url_for("display_change_account_password"),
                               manage_teacher_accounts_url = url_for("display_manage_teacher_accounts_page"),
                               manage_student_accounts_url = url_for("display_manage_student_accounts_page"),
                               add_new_location_url = url_for("add_new_location"),
                               edit_school_details_url = url_for("manage_school_details"),
                               edit_opening_hours_url = url_for("manage_school_opening_hours"),
                               manage_locations_url = url_for("view_edit_locations"),
                               add_new_lesson_url = url_for("add_new_lesson"),
                               view_edit_lessons_url = url_for("view_edit_lessons"),
                               add_new_student_url = url_for("add_new_student"),
                               view_edit_students_url = url_for("view_edit_students"),
                               add_new_teacher_url = url_for("add_new_teacher"),
                               view_edit_teachers_url = url_for("view_edit_teachers"),
                               add_new_ensemble_group_url = url_for("add_new_ensemble"),
                               manage_ensemble_groups_url = url_for("view_edit_ensemble_groups"),
                               add_new_classroom_url = url_for("add_new_classroom"),
                               view_edit_classrooms_url = url_for("view_edit_classrooms"),
                               manage_a_student_timetable_url = url_for("manage_timetables"),
                               view_a_classroom_timetable_url = url_for("select_classroom_timetable"),
                               view_a_teacher_timetable_url = url_for("select_teacher_timetable"),
                               view_a_student_timetable_url = url_for("select_student_timetable"),
                               about_this_project_url = url_for("display_about_this_project_page"),
                               log_out_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3], 
                               current_school_id = session.get("loginId"),
                               list_of_persons = listOfSchoolStudentNames, )

#===== Ensemble Management Screens ==================================================================================================================================

@app.route("/addNewEnsemble")
def add_new_ensemble():
    if session.get("loggedIn") == False or session.get("loggedIn") is None or session.get("accountType") != "Administrator":
        session["loggedIn"] = False
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(1, 4)
        return render_template("errorNotLoggedIn.html",
                               logged_in = session.get("loggedIn"),
                               login_screen_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3], )
    else:
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRandom(13, 21)
        return render_template("ensembleAddNew.html",
                               page_title = "Add New Ensemble Group",
                               home_page_url = url_for("display_home_page"),
                               school_name = session.get("loginName"),
                               logged_in = session.get("loggedIn"),
                               account_type = session.get("accountType"),
                               login_id = session.get("loginId"),
                               manage_your_account_url = url_for("display_change_account_password"),
                               manage_teacher_accounts_url = url_for("display_manage_teacher_accounts_page"),
                               manage_student_accounts_url = url_for("display_manage_student_accounts_page"),
                               add_new_location_url = url_for("add_new_location"),
                               edit_school_details_url = url_for("manage_school_details"),
                               edit_opening_hours_url = url_for("manage_school_opening_hours"),
                               manage_locations_url = url_for("view_edit_locations"),
                               add_new_lesson_url = url_for("add_new_lesson"),
                               view_edit_lessons_url = url_for("view_edit_lessons"),
                               add_new_student_url = url_for("add_new_student"),
                               view_edit_students_url = url_for("view_edit_students"),
                               add_new_teacher_url = url_for("add_new_teacher"),
                               view_edit_teachers_url = url_for("view_edit_teachers"),
                               add_new_ensemble_group_url = url_for("add_new_ensemble"),
                               manage_ensemble_groups_url = url_for("view_edit_ensemble_groups"),
                               add_new_classroom_url = url_for("add_new_classroom"),
                               view_edit_classrooms_url = url_for("view_edit_classrooms"),
                               manage_a_student_timetable_url = url_for("manage_timetables"),
                               view_a_classroom_timetable_url = url_for("select_classroom_timetable"),
                               view_a_teacher_timetable_url = url_for("select_teacher_timetable"),
                               view_a_student_timetable_url = url_for("select_student_timetable"),
                               about_this_project_url = url_for("display_about_this_project_page"),
                               log_out_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3],
                               current_school_id = session.get("loginId"), )

@app.route("/manageEnsembleGroups")
def view_edit_ensemble_groups():
    if session.get("loggedIn") == False or session.get("loggedIn") is None or session.get("accountType") != "Administrator":
        session["loggedIn"] = False
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(1, 4)
        return render_template("errorNotLoggedIn.html",
                               logged_in = session.get("loggedIn"),
                               login_screen_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3], )
    else:
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRandom(13, 21)
        return render_template("ensembleViewEditDetails.html",
                               page_title = "Manage Your Ensemble Groups",
                               home_page_url = url_for("display_home_page"),
                               school_name = session.get("loginName"),
                               logged_in = session.get("loggedIn"),
                               account_type = session.get("accountType"),
                               login_id = session.get("loginId"),
                               manage_your_account_url = url_for("display_change_account_password"),
                               manage_teacher_accounts_url = url_for("display_manage_teacher_accounts_page"),
                               manage_student_accounts_url = url_for("display_manage_student_accounts_page"),
                               add_new_location_url = url_for("add_new_location"),
                               edit_school_details_url = url_for("manage_school_details"),
                               edit_opening_hours_url = url_for("manage_school_opening_hours"),
                               manage_locations_url = url_for("view_edit_locations"),
                               add_new_lesson_url = url_for("add_new_lesson"),
                               view_edit_lessons_url = url_for("view_edit_lessons"),
                               add_new_student_url = url_for("add_new_student"),
                               view_edit_students_url = url_for("view_edit_students"),
                               add_new_teacher_url = url_for("add_new_teacher"),
                               view_edit_teachers_url = url_for("view_edit_teachers"),
                               add_new_ensemble_group_url = url_for("add_new_ensemble"),
                               manage_ensemble_groups_url = url_for("view_edit_ensemble_groups"),
                               add_new_classroom_url = url_for("add_new_classroom"),
                               view_edit_classrooms_url = url_for("view_edit_classrooms"),
                               manage_a_student_timetable_url = url_for("manage_timetables"),
                               view_a_classroom_timetable_url = url_for("select_classroom_timetable"),
                               view_a_teacher_timetable_url = url_for("select_teacher_timetable"),
                               view_a_student_timetable_url = url_for("select_student_timetable"),
                               about_this_project_url = url_for("display_about_this_project_page"),
                               log_out_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3], 
                               current_school_id = session.get("loginId"), )

#===== Teacher Management Screens ===================================================================================================================================

@app.route("/addNewTeacher")
def add_new_teacher():
    if session.get("loggedIn") == False or session.get("loggedIn") is None or session.get("accountType") != "Administrator":
        session["loggedIn"] = False
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(1, 4)
        return render_template("errorNotLoggedIn.html",
                               logged_in = session.get("loggedIn"),
                               login_screen_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3], )
    else:
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRandom(60, 67)
        return render_template("teacherAddNew.html",
                               page_title = "Add New Teacher",
                               home_page_url = url_for("display_home_page"),
                               school_name = session.get("loginName"),
                               logged_in = session.get("loggedIn"),
                               account_type = session.get("accountType"),
                               login_id = session.get("loginId"),
                               manage_your_account_url = url_for("display_change_account_password"),
                               manage_teacher_accounts_url = url_for("display_manage_teacher_accounts_page"),
                               manage_student_accounts_url = url_for("display_manage_student_accounts_page"),
                               add_new_location_url = url_for("add_new_location"),
                               edit_school_details_url = url_for("manage_school_details"),
                               edit_opening_hours_url = url_for("manage_school_opening_hours"),
                               manage_locations_url = url_for("view_edit_locations"),
                               add_new_lesson_url = url_for("add_new_lesson"),
                               view_edit_lessons_url = url_for("view_edit_lessons"),
                               add_new_student_url = url_for("add_new_student"),
                               view_edit_students_url = url_for("view_edit_students"),
                               add_new_teacher_url = url_for("add_new_teacher"),
                               view_edit_teachers_url = url_for("view_edit_teachers"),
                               add_new_ensemble_group_url = url_for("add_new_ensemble"),
                               manage_ensemble_groups_url = url_for("view_edit_ensemble_groups"),
                               add_new_classroom_url = url_for("add_new_classroom"),
                               view_edit_classrooms_url = url_for("view_edit_classrooms"),
                               manage_a_student_timetable_url = url_for("manage_timetables"),
                               view_a_classroom_timetable_url = url_for("select_classroom_timetable"),
                               view_a_teacher_timetable_url = url_for("select_teacher_timetable"),
                               view_a_student_timetable_url = url_for("select_student_timetable"),
                               about_this_project_url = url_for("display_about_this_project_page"),
                               log_out_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3], 
                               current_school_id = session.get("loginId"), )

@app.route("/viewEditTeacherDetails")
def view_edit_teachers():
    if session.get("loggedIn") == False or session.get("loggedIn") is None or session.get("accountType") != "Administrator":
        session["loggedIn"] = False
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(1, 4)
        return render_template("errorNotLoggedIn.html",
                               logged_in = session.get("loggedIn"),
                               login_screen_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3], )
    else:
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(68, 71)
        listOfSchoolTeacherNames = DataProcessing.getSchoolTeachersNamesList(session.get("loginId"))
        return render_template("teacherViewEditDetails.html",
                               page_title = "View/Edit Your Teachers",
                               home_page_url = url_for("display_home_page"),
                               school_name = session.get("loginName"),
                               logged_in = session.get("loggedIn"),
                               account_type = session.get("accountType"),
                               login_id = session.get("loginId"),
                               manage_your_account_url = url_for("display_change_account_password"),
                               manage_teacher_accounts_url = url_for("display_manage_teacher_accounts_page"),
                               manage_student_accounts_url = url_for("display_manage_student_accounts_page"),
                               add_new_location_url = url_for("add_new_location"),
                               edit_school_details_url = url_for("manage_school_details"),
                               edit_opening_hours_url = url_for("manage_school_opening_hours"),
                               manage_locations_url = url_for("view_edit_locations"),
                               add_new_lesson_url = url_for("add_new_lesson"),
                               view_edit_lessons_url = url_for("view_edit_lessons"),
                               add_new_student_url = url_for("add_new_student"),
                               view_edit_students_url = url_for("view_edit_students"),
                               add_new_teacher_url = url_for("add_new_teacher"),
                               view_edit_teachers_url = url_for("view_edit_teachers"),
                               add_new_ensemble_group_url = url_for("add_new_ensemble"),
                               manage_ensemble_groups_url = url_for("view_edit_ensemble_groups"),
                               add_new_classroom_url = url_for("add_new_classroom"),
                               view_edit_classrooms_url = url_for("view_edit_classrooms"),
                               manage_a_student_timetable_url = url_for("manage_timetables"),
                               view_a_classroom_timetable_url = url_for("select_classroom_timetable"),
                               view_a_teacher_timetable_url = url_for("select_teacher_timetable"),
                               view_a_student_timetable_url = url_for("select_student_timetable"),
                               about_this_project_url = url_for("display_about_this_project_page"),
                               log_out_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3],  
                               current_school_id = session.get("loginId"),
                               list_of_persons = listOfSchoolTeacherNames, )

#===== Classroom Management Screens =================================================================================================================================

@app.route("/addNewClassroom")
def add_new_classroom():
    if session.get("loggedIn") == False or session.get("loggedIn") is None or session.get("accountType") != "Administrator":
        session["loggedIn"] = False
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(1, 4)
        return render_template("errorNotLoggedIn.html",
                               logged_in = session.get("loggedIn"),
                               login_screen_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3], )
    else:
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(84, 87)
        locationsList = DataProcessing.getListOfSchoolLocations(session.get("loginId"))
        return render_template("classroomAddNew.html",
                               page_title = "Add New Classroom",
                               home_page_url = url_for("display_home_page"),
                               school_name = session.get("loginName"),
                               logged_in = session.get("loggedIn"),
                               account_type = session.get("accountType"),
                               login_id = session.get("loginId"),
                               manage_your_account_url = url_for("display_change_account_password"),
                               manage_teacher_accounts_url = url_for("display_manage_teacher_accounts_page"),
                               manage_student_accounts_url = url_for("display_manage_student_accounts_page"),
                               add_new_location_url = url_for("add_new_location"),
                               edit_school_details_url = url_for("manage_school_details"),
                               edit_opening_hours_url = url_for("manage_school_opening_hours"),
                               manage_locations_url = url_for("view_edit_locations"),
                               add_new_lesson_url = url_for("add_new_lesson"),
                               view_edit_lessons_url = url_for("view_edit_lessons"),
                               add_new_student_url = url_for("add_new_student"),
                               view_edit_students_url = url_for("view_edit_students"),
                               add_new_teacher_url = url_for("add_new_teacher"),
                               view_edit_teachers_url = url_for("view_edit_teachers"),
                               add_new_ensemble_group_url = url_for("add_new_ensemble"),
                               manage_ensemble_groups_url = url_for("view_edit_ensemble_groups"),
                               add_new_classroom_url = url_for("add_new_classroom"),
                               view_edit_classrooms_url = url_for("view_edit_classrooms"),
                               manage_a_student_timetable_url = url_for("manage_timetables"),
                               view_a_classroom_timetable_url = url_for("select_classroom_timetable"),
                               view_a_teacher_timetable_url = url_for("select_teacher_timetable"),
                               view_a_student_timetable_url = url_for("select_student_timetable"),
                               about_this_project_url = url_for("display_about_this_project_page"),
                               log_out_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3], 
                               list_of_locations = locationsList, )

@app.route("/viewEditClassrooms")
def view_edit_classrooms():
    if session.get("loggedIn") == False or session.get("loggedIn") is None or session.get("accountType") != "Administrator":
        session["loggedIn"] = False
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(1, 4)
        return render_template("errorNotLoggedIn.html",
                               logged_in = session.get("loggedIn"),
                               login_screen_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3], )
    else:
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(88, 91)
        locationsList = DataProcessing.getListOfSchoolLocations(session.get("loginId"))
        return render_template("classroomViewEditDetails.html",
                               page_title = "View/Edit Your Classrooms",
                               home_page_url = url_for("display_home_page"),
                               school_name = session.get("loginName"),
                               logged_in = session.get("loggedIn"),
                               account_type = session.get("accountType"),
                               login_id = session.get("loginId"),
                               manage_your_account_url = url_for("display_change_account_password"),
                               manage_teacher_accounts_url = url_for("display_manage_teacher_accounts_page"),
                               manage_student_accounts_url = url_for("display_manage_student_accounts_page"),
                               add_new_location_url = url_for("add_new_location"),
                               edit_school_details_url = url_for("manage_school_details"),
                               edit_opening_hours_url = url_for("manage_school_opening_hours"),
                               manage_locations_url = url_for("view_edit_locations"),
                               add_new_lesson_url = url_for("add_new_lesson"),
                               view_edit_lessons_url = url_for("view_edit_lessons"),
                               add_new_student_url = url_for("add_new_student"),
                               view_edit_students_url = url_for("view_edit_students"),
                               add_new_teacher_url = url_for("add_new_teacher"),
                               view_edit_teachers_url = url_for("view_edit_teachers"),
                               add_new_ensemble_group_url = url_for("add_new_ensemble"),
                               manage_ensemble_groups_url = url_for("view_edit_ensemble_groups"),
                               add_new_classroom_url = url_for("add_new_classroom"),
                               view_edit_classrooms_url = url_for("view_edit_classrooms"),
                               manage_a_student_timetable_url = url_for("manage_timetables"),
                               view_a_classroom_timetable_url = url_for("select_classroom_timetable"),
                               view_a_teacher_timetable_url = url_for("select_teacher_timetable"),
                               view_a_student_timetable_url = url_for("select_student_timetable"),
                               about_this_project_url = url_for("display_about_this_project_page"),
                               log_out_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3],
                               list_of_locations = locationsList, )

#===== Timetable Management Screens =================================================================================================================================

@app.route("/manageStudentTimetables")
def manage_timetables():
    if session.get("loggedIn") == False or session.get("loggedIn") is None or session.get("accountType") != "Administrator":
        session["loggedIn"] = False
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(1, 4)
        return render_template("errorNotLoggedIn.html",
                               logged_in = session.get("loggedIn"),
                               login_screen_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3], )
    else:
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(92, 95)
        listOfSchoolStudentNames = DataProcessing.getSchoolStudentsNamesList(session.get("loginId"))
        return render_template("timetableManageStudent.html",
                               page_title = "Manage a Student Timetable",
                               home_page_url = url_for("display_home_page"),
                               school_name = session.get("loginName"),
                               logged_in = session.get("loggedIn"),
                               account_type = session.get("accountType"),
                               login_id = session.get("loginId"),
                               manage_your_account_url = url_for("display_change_account_password"),
                               manage_teacher_accounts_url = url_for("display_manage_teacher_accounts_page"),
                               manage_student_accounts_url = url_for("display_manage_student_accounts_page"),
                               add_new_location_url = url_for("add_new_location"),
                               edit_school_details_url = url_for("manage_school_details"),
                               edit_opening_hours_url = url_for("manage_school_opening_hours"),
                               manage_locations_url = url_for("view_edit_locations"),
                               add_new_lesson_url = url_for("add_new_lesson"),
                               view_edit_lessons_url = url_for("view_edit_lessons"),
                               add_new_student_url = url_for("add_new_student"),
                               view_edit_students_url = url_for("view_edit_students"),
                               add_new_teacher_url = url_for("add_new_teacher"),
                               view_edit_teachers_url = url_for("view_edit_teachers"),
                               add_new_ensemble_group_url = url_for("add_new_ensemble"),
                               manage_ensemble_groups_url = url_for("view_edit_ensemble_groups"),
                               add_new_classroom_url = url_for("add_new_classroom"),
                               view_edit_classrooms_url = url_for("view_edit_classrooms"),
                               manage_a_student_timetable_url = url_for("manage_timetables"),
                               view_a_classroom_timetable_url = url_for("select_classroom_timetable"),
                               view_a_teacher_timetable_url = url_for("select_teacher_timetable"),
                               view_a_student_timetable_url = url_for("select_student_timetable"),
                               about_this_project_url = url_for("display_about_this_project_page"),
                               log_out_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3],
                               list_of_students = listOfSchoolStudentNames, )

@app.route("/selectClassroomTimetable")
def select_classroom_timetable():
    if session.get("loggedIn") == False or session.get("loggedIn") is None or session.get("accountType") != "Administrator":
        session["loggedIn"] = False
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(1, 4)
        return render_template("errorNotLoggedIn.html",
                               logged_in = session.get("loggedIn"),
                               login_screen_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3], )
    else:
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(96, 99)
        locationsList = DataProcessing.getListOfSchoolLocations(session.get("loginId"))
        return render_template("timetableClassroomSelect.html",
                               page_title = "Select a Classroom Timetable",
                               home_page_url = url_for("display_home_page"),
                               school_name = session.get("loginName"),
                               logged_in = session.get("loggedIn"),
                               account_type = session.get("accountType"),
                               login_id = session.get("loginId"),
                               manage_your_account_url = url_for("display_change_account_password"),
                               manage_teacher_accounts_url = url_for("display_manage_teacher_accounts_page"),
                               manage_student_accounts_url = url_for("display_manage_student_accounts_page"),
                               add_new_location_url = url_for("add_new_location"),
                               edit_school_details_url = url_for("manage_school_details"),
                               edit_opening_hours_url = url_for("manage_school_opening_hours"),
                               manage_locations_url = url_for("view_edit_locations"),
                               add_new_lesson_url = url_for("add_new_lesson"),
                               view_edit_lessons_url = url_for("view_edit_lessons"),
                               add_new_student_url = url_for("add_new_student"),
                               view_edit_students_url = url_for("view_edit_students"),
                               add_new_teacher_url = url_for("add_new_teacher"),
                               view_edit_teachers_url = url_for("view_edit_teachers"),
                               add_new_ensemble_group_url = url_for("add_new_ensemble"),
                               manage_ensemble_groups_url = url_for("view_edit_ensemble_groups"),
                               add_new_classroom_url = url_for("add_new_classroom"),
                               view_edit_classrooms_url = url_for("view_edit_classrooms"),
                               manage_a_student_timetable_url = url_for("manage_timetables"),
                               view_a_classroom_timetable_url = url_for("select_classroom_timetable"),
                               view_a_teacher_timetable_url = url_for("select_teacher_timetable"),
                               view_a_student_timetable_url = url_for("select_student_timetable"),
                               about_this_project_url = url_for("display_about_this_project_page"),
                               log_out_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3],
                               list_of_locations = locationsList, )

@app.route("/selectTeacherTimetable")
def select_teacher_timetable():
    if session.get("loggedIn") == False or session.get("loggedIn") is None or session.get("accountType") != "Administrator":
        session["loggedIn"] = False
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(1, 4)
        return render_template("errorNotLoggedIn.html",
                               logged_in = session.get("loggedIn"),
                               login_screen_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3], )
    else:
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(100, 103)
        listOfSchoolTeacherNames = DataProcessing.getSchoolTeachersNamesList(session.get("loginId"))
        return render_template("timetableTeacherSelect.html",
                               page_title = "Select a Teacher Timetable",
                               home_page_url = url_for("display_home_page"),
                               school_name = session.get("loginName"),
                               logged_in = session.get("loggedIn"),
                               account_type = session.get("accountType"),
                               login_id = session.get("loginId"),
                               manage_your_account_url = url_for("display_change_account_password"),
                               manage_teacher_accounts_url = url_for("display_manage_teacher_accounts_page"),
                               manage_student_accounts_url = url_for("display_manage_student_accounts_page"),
                               add_new_location_url = url_for("add_new_location"),
                               edit_school_details_url = url_for("manage_school_details"),
                               edit_opening_hours_url = url_for("manage_school_opening_hours"),
                               manage_locations_url = url_for("view_edit_locations"),
                               add_new_lesson_url = url_for("add_new_lesson"),
                               view_edit_lessons_url = url_for("view_edit_lessons"),
                               add_new_student_url = url_for("add_new_student"),
                               view_edit_students_url = url_for("view_edit_students"),
                               add_new_teacher_url = url_for("add_new_teacher"),
                               view_edit_teachers_url = url_for("view_edit_teachers"),
                               add_new_ensemble_group_url = url_for("add_new_ensemble"),
                               manage_ensemble_groups_url = url_for("view_edit_ensemble_groups"),
                               add_new_classroom_url = url_for("add_new_classroom"),
                               view_edit_classrooms_url = url_for("view_edit_classrooms"),
                               manage_a_student_timetable_url = url_for("manage_timetables"),
                               view_a_classroom_timetable_url = url_for("select_classroom_timetable"),
                               view_a_teacher_timetable_url = url_for("select_teacher_timetable"),
                               view_a_student_timetable_url = url_for("select_student_timetable"),
                               about_this_project_url = url_for("display_about_this_project_page"),
                               log_out_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3],
                               list_of_persons = listOfSchoolTeacherNames, )

@app.route("/selectStudentTimetable")
def select_student_timetable():
    if session.get("loggedIn") == False or session.get("loggedIn") is None or session.get("accountType") != "Administrator":
        session["loggedIn"] = False
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(1, 4)
        return render_template("errorNotLoggedIn.html",
                               logged_in = session.get("loggedIn"),
                               login_screen_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3], )
    else:
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(104, 107)
        listOfSchoolStudentNames = DataProcessing.getSchoolStudentsNamesList(session.get("loginId"))
        return render_template("timetableStudentSelect.html",
                               page_title = "Select a Student Timetable",
                               home_page_url = url_for("display_home_page"),
                               school_name = session.get("loginName"),
                               logged_in = session.get("loggedIn"),
                               account_type = session.get("accountType"),
                               login_id = session.get("loginId"),
                               manage_your_account_url = url_for("display_change_account_password"),
                               manage_teacher_accounts_url = url_for("display_manage_teacher_accounts_page"),
                               manage_student_accounts_url = url_for("display_manage_student_accounts_page"),
                               add_new_location_url = url_for("add_new_location"),
                               edit_school_details_url = url_for("manage_school_details"),
                               edit_opening_hours_url = url_for("manage_school_opening_hours"),
                               manage_locations_url = url_for("view_edit_locations"),
                               add_new_lesson_url = url_for("add_new_lesson"),
                               view_edit_lessons_url = url_for("view_edit_lessons"),
                               add_new_student_url = url_for("add_new_student"),
                               view_edit_students_url = url_for("view_edit_students"),
                               add_new_teacher_url = url_for("add_new_teacher"),
                               view_edit_teachers_url = url_for("view_edit_teachers"),
                               add_new_ensemble_group_url = url_for("add_new_ensemble"),
                               manage_ensemble_groups_url = url_for("view_edit_ensemble_groups"),
                               add_new_classroom_url = url_for("add_new_classroom"),
                               view_edit_classrooms_url = url_for("view_edit_classrooms"),
                               manage_a_student_timetable_url = url_for("manage_timetables"),
                               view_a_classroom_timetable_url = url_for("select_classroom_timetable"),
                               view_a_teacher_timetable_url = url_for("select_teacher_timetable"),
                               view_a_student_timetable_url = url_for("select_student_timetable"),
                               about_this_project_url = url_for("display_about_this_project_page"),
                               log_out_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3],
                               list_of_persons = listOfSchoolStudentNames, )

@app.route("/viewAllTimetables")
def display_all_timetables():
    if session.get("loggedIn") == False or session.get("loggedIn") is None:
        session["loggedIn"] = False
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(1, 4)
        return render_template("errorNotLoggedIn.html",
                               logged_in = session.get("loggedIn"),
                               login_screen_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3], )
    else:
        # Check if a student or teacher has logged in (ie not an Administrator account)
        accountLoggedIn = session.get("accountType")
        if accountLoggedIn == "Teacher":
            session["timetableId"] = session.get("loginId")
            session["timetableType"] = "TeacherAll"
        elif accountLoggedIn == "Student":
            session["timetableId"] = session.get("loginId")
            session["timetableType"] = "StudentAll"
        
        # Get the timetable to be displayed
        timetableDisplay = []
        listOfAllDetails = []
        timetableType = session.get("timetableType")
        if timetableType == "StudentSchool":
            timetableDisplay = DataProcessing.getStudentSchoolTimetable(session.get("loginId"), session.get("timetableId"))
            listOfAllDetails = DataProcessing.getSchoolOpenDaysAndTimesDetails(session.get("loginId"))
        elif timetableType == "StudentAll":
            timetableDisplay = DataProcessing.getStudentAllTimetable(session.get("timetableId"))
            listOfAllDetails = DataProcessing.getGeneralOpenDaysAndTimesDetails(session.get("loginId"), "Student")
        elif timetableType == "TeacherSchool":
            timetableDisplay = DataProcessing.getTeacherSchoolTimetable(session.get("loginId"), session.get("timetableId"))
            listOfAllDetails = DataProcessing.getSchoolOpenDaysAndTimesDetails(session.get("loginId"))
        elif timetableType == "TeacherAll":
            timetableDisplay = DataProcessing.getTeacherAllTimetable(session.get("timetableId"))
            listOfAllDetails = DataProcessing.getGeneralOpenDaysAndTimesDetails(session.get("loginId"), "Teacher")
        elif timetableType == "Classroom":
            timetableDisplay = DataProcessing.getClassroomTimetable(session.get("timetableId"))
            listOfAllDetails = DataProcessing.getSchoolOpenDaysAndTimesDetails(session.get("loginId"))

        # Get additional information in order to display the timetable
        listOfOpenDayIndexes = listOfAllDetails[0]
        earliestStartTime = listOfAllDetails[1]
        latestEndTime = listOfAllDetails[2]
        openingDaysAndTimes = listOfAllDetails[3]
        openingTimes = listOfAllDetails[4]
        
        return render_template("timetableViewAll.html",
                               page_title = "View Timetable",
                               home_page_url = url_for("display_home_page"),
                               school_name = session.get("loginName"),
                               logged_in = session.get("loggedIn"),
                               account_type = session.get("accountType"),
                               login_id = session.get("loginId"),
                               manage_your_account_url = url_for("display_change_account_password"),
                               manage_teacher_accounts_url = url_for("display_manage_teacher_accounts_page"),
                               manage_student_accounts_url = url_for("display_manage_student_accounts_page"),
                               add_new_location_url = url_for("add_new_location"),
                               edit_school_details_url = url_for("manage_school_details"),
                               edit_opening_hours_url = url_for("manage_school_opening_hours"),
                               manage_locations_url = url_for("view_edit_locations"),
                               add_new_lesson_url = url_for("add_new_lesson"),
                               view_edit_lessons_url = url_for("view_edit_lessons"),
                               add_new_student_url = url_for("add_new_student"),
                               view_edit_students_url = url_for("view_edit_students"),
                               add_new_teacher_url = url_for("add_new_teacher"),
                               view_edit_teachers_url = url_for("view_edit_teachers"),
                               add_new_ensemble_group_url = url_for("add_new_ensemble"),
                               manage_ensemble_groups_url = url_for("view_edit_ensemble_groups"),
                               add_new_classroom_url = url_for("add_new_classroom"),
                               view_edit_classrooms_url = url_for("view_edit_classrooms"),
                               manage_a_student_timetable_url = url_for("manage_timetables"),
                               view_a_classroom_timetable_url = url_for("select_classroom_timetable"),
                               view_a_teacher_timetable_url = url_for("select_teacher_timetable"),
                               view_a_student_timetable_url = url_for("select_student_timetable"),
                               about_this_project_url = url_for("display_about_this_project_page"),
                               log_out_url = url_for("display_login_page"),
                               list_of_weekdays = listOfOpenDayIndexes,
                               start_hour = earliestStartTime,
                               end_hour = latestEndTime,
                               open_days_and_times = openingDaysAndTimes,
                               open_times = openingTimes,
                               list_of_timetabled_lessons = timetableDisplay,
                               timetable_to_draw = timetableType, )

@app.route("/timetableEditor")
def display_timetable_editor():
    if session.get("loggedIn") == False or session.get("loggedIn") is None or session.get("accountType") != "Administrator":
        session["loggedIn"] = False
        footerDisplays = WebTipsDisplay.determineFooterTutorialDisplayByRange(1, 4)
        return render_template("errorNotLoggedIn.html",
                               logged_in = session.get("loggedIn"),
                               login_screen_url = url_for("display_login_page"),
                               footer_one = footerDisplays[0],
                               footer_two = footerDisplays[1],
                               footer_three = footerDisplays[2],
                               footer_four = footerDisplays[3], )
    else:
        # Get the schools open days, hours and determine the min and max hours for timetable display
        listOfAllDetails = DataProcessing.getSchoolOpenDaysAndTimesDetails(session.get("loginId"))
        listOfOpenDayIndexes = listOfAllDetails[0]
        earliestStartTime = listOfAllDetails[1]
        latestEndTime = listOfAllDetails[2]
        openingDaysAndTimes = listOfAllDetails[3]
        openingTimes = listOfAllDetails[4]

        # Get the list of the schools lessons
        listOfLessonDetails = DataProcessing.getSchoolFullLessonDetailsList(session.get("loginId"))

        # Get the list of the schools teachers
        listOfTeacherDetails = DataProcessing.getSchoolTeacherIdAndNamesList(session.get("loginId"))

        # Get the list of the schools locations and classrooms
        listOfClassroomDetails = DataProcessing.getSchoolClassroomNamesAndLocations(session.get("loginId"))

        # Get the list of timetabled lessons associated with this student
        listOfScheduledLessons = DataProcessing.getStudentTimetable(session.get("loginId"), session.get("studentId"))

        # Load the timetable editor screen
        return render_template("timetableEditorScreen.html",
                               page_title = "Student Timetable Editor",
                               home_page_url = url_for("display_home_page"),
                               school_name = session.get("loginName"),
                               logged_in = session.get("loggedIn"),
                               account_type = session.get("accountType"),
                               login_id = session.get("loginId"),
                               manage_your_account_url = url_for("display_change_account_password"),
                               manage_teacher_accounts_url = url_for("display_manage_teacher_accounts_page"),
                               manage_student_accounts_url = url_for("display_manage_student_accounts_page"),
                               add_new_location_url = url_for("add_new_location"),
                               edit_school_details_url = url_for("manage_school_details"),
                               edit_opening_hours_url = url_for("manage_school_opening_hours"),
                               manage_locations_url = url_for("view_edit_locations"),
                               add_new_lesson_url = url_for("add_new_lesson"),
                               view_edit_lessons_url = url_for("view_edit_lessons"),
                               add_new_student_url = url_for("add_new_student"),
                               view_edit_students_url = url_for("view_edit_students"),
                               add_new_teacher_url = url_for("add_new_teacher"),
                               view_edit_teachers_url = url_for("view_edit_teachers"),
                               add_new_ensemble_group_url = url_for("add_new_ensemble"),
                               manage_ensemble_groups_url = url_for("view_edit_ensemble_groups"),
                               add_new_classroom_url = url_for("add_new_classroom"),
                               view_edit_classrooms_url = url_for("view_edit_classrooms"),
                               manage_a_student_timetable_url = url_for("manage_timetables"),
                               view_a_classroom_timetable_url = url_for("select_classroom_timetable"),
                               view_a_teacher_timetable_url = url_for("select_teacher_timetable"),
                               view_a_student_timetable_url = url_for("select_student_timetable"),
                               about_this_project_url = url_for("display_about_this_project_page"),
                               log_out_url = url_for("display_login_page"),
                               list_of_weekdays = listOfOpenDayIndexes,
                               start_hour = earliestStartTime,
                               end_hour = latestEndTime,
                               open_days_and_times = openingDaysAndTimes,
                               open_times = openingTimes,
                               list_of_lessons = listOfLessonDetails,
                               list_of_teachers = listOfTeacherDetails,
                               list_of_classrooms = listOfClassroomDetails,
                               list_of_timetabled_lessons = listOfScheduledLessons,
                               current_school_id = session.get("loginId"),
                               current_student_id = session.get("studentId"), )

#===== AJAX Login and Registration Methods ==========================================================================================================================

@app.route("/validateFirstRegistrationPage", methods = ["POST"])
def validate_registration_details_page_one():
    schoolName = request.form["schoolName"].strip()
    emailAddress = request.form["emailAddress"].strip()
    confirmEmail = request.form["confirmEmailAddress"].strip()
    password = request.form["password"].strip()
    confirmPassword = request.form["confirmPassword"].strip()
    validationResult = WebValidation.validateFirstRegistrationDetails(schoolName, emailAddress, confirmEmail, password, confirmPassword)
    if validationResult == "OK":
        session["schoolName"] = schoolName
        session["emailAddress"] = emailAddress
        session["password"] = password
    return validationResult

@app.route("/validateSecondRegistrationPage", methods = ["POST"])
def validate_registration_details_page_two():
    streetName1 = request.form["streetName1"].strip()
    streetName2 = request.form["streetName2"].strip()
    townOrCity = request.form["townOrCity"].strip()
    county = request.form["county"].strip()
    phoneNumber = request.form["phoneNumber"].strip()
    validationResult = WebValidation.validateSecondRegistrationDetails(session.get("emailAddress"), streetName1, streetName2, townOrCity, county, phoneNumber)
    if validationResult == "OK":
        DataProcessing.insertNewSchoolRecord(session.get("schoolName"), session.get("emailAddress"), streetName1, streetName2, townOrCity, county,
                                             phoneNumber, session.get("password"))
        resetAllSessionVariables()
        session["registered"] = True
    return validationResult

@app.route("/validateLogin", methods = ["POST"])
def validate_user_login():
    emailAddress = request.form["emailAddress"].strip()
    password = request.form["password"].strip()
    validationResult = DataProcessing.verifyUserLoginDetails(emailAddress, password)
    if validationResult == True:
        return "OK"
    else:
        return "We are sorry but there is no account linked to this email address and password combination.\n\nPlease try entering a registered email address and password."
    
#===== AJAX School Management Methods ===============================================================================================================================
    
@app.route("/updateSchoolDetails", methods = ["POST"])
def update_school_details():
    schoolId = request.form["schoolId"].strip()
    oldSchoolName = request.form["oldSchoolName"].strip()
    editedSchoolName = request.form["schoolName"].strip()
    addressId = request.form["addressId"].strip()
    streetName1 = request.form["streetName1"].strip()
    streetName2 = request.form["streetName2"].strip()
    townOrCity = request.form["townOrCity"].strip()
    county = request.form["county"].strip()
    phoneNumber = request.form["phoneNumber"].strip()
    emailAddress = request.form["emailAddress"].strip()
    confirmedEmail = request.form["confirmEmailAddress"].strip()
    validationResult = WebValidation.validateSchoolDetails(schoolId, editedSchoolName, addressId, streetName1, streetName2, townOrCity, county, phoneNumber,
                                                   emailAddress, confirmedEmail)
    if validationResult == "OK":
        DataProcessing.updateSchoolDetails(schoolId, oldSchoolName, editedSchoolName, addressId, streetName1, streetName2, townOrCity, county,
                                           phoneNumber, emailAddress)
    return validationResult

@app.route("/updateSchoolOpeningHours", methods = ["POST"])
def update_school_opening_hours():
    listOfOpeningHoursSettings = []
    for index in range(0, 7):
        openOrClosed = request.form["openOrClosed" + str(index)]
        selectedOpeningTime = request.form["openingTimeSelect" + str(index)]
        selectedClosingTime = request.form["closingTimeSelect" + str(index)]
        currentOpeningHours = ClassesList.OpeningHoursSettings(openOrClosed, selectedOpeningTime, selectedClosingTime)
        listOfOpeningHoursSettings.append(currentOpeningHours)
    validationResult = WebValidation.validateOpeningHours(listOfOpeningHoursSettings)
    if validationResult == "OK":
        earliestStartTime = -1
        latestEndTime = -1
        for index in range(0, 7):
            # Determine the earliest start time for the school and the latest end time
            currentOpeningTimeRecord = listOfOpeningHoursSettings[index].openingTime
            currentClosingTimeRecord = listOfOpeningHoursSettings[index].closingTime
            openHour = int(currentOpeningTimeRecord[0:currentOpeningTimeRecord.index(":")])
            closeHour = int(currentClosingTimeRecord[0:currentClosingTimeRecord.index(":")])
            if earliestStartTime == -1 and latestEndTime == -1:
                earliestStartTime = openHour
                latestEndTime = closeHour
            if openHour < earliestStartTime:
                earliestStartTime = openHour
            if closeHour > latestEndTime:
                latestEndTime = closeHour

            # Update the stored opening hours
            DataProcessing.updateSchoolOpeningHours(session.get("loginId"), (index + 1), listOfOpeningHoursSettings[index].openOrClosed,
                                                    listOfOpeningHoursSettings[index].openingTime, listOfOpeningHoursSettings[index].closingTime)
        # Delete any timetabled records outside of the schools opening hours
        DataProcessing.deleteTimetableRecordsOutsideSchoolHours(session.get("loginId"), earliestStartTime, latestEndTime)
    return validationResult

@app.route("/submitNewLocation", methods = ["POST"])
def submit_new_location():
    schoolId = request.form["schoolId"].strip()
    locationName = request.form["locationName"].strip()
    streetName1 = request.form["streetName1"].strip()
    streetName2 = request.form["streetName2"].strip()
    townOrCity = request.form["townOrCity"].strip()
    county = request.form["county"].strip()
    validationResult = WebValidation.validateNewSchoolLocation(schoolId, locationName, streetName1, streetName2, townOrCity, county)
    if validationResult == "OK":
        headLocation = 0
        DataProcessing.insertNewLocationRecord(schoolId, locationName, streetName1, streetName2, townOrCity, county, headLocation)
    return validationResult

@app.route("/submitEditedLocation", methods = ["POST"])
def update_location_details():
    schoolId = request.form["schoolId"].strip()
    locationId = request.form["locationId"].strip()
    addressId = request.form["addressId"].strip()
    locationName = request.form["locationName"].strip()
    streetName1 = request.form["streetName1"].strip()
    streetName2 = request.form["streetName2"].strip()
    townOrCity = request.form["townOrCity"].strip()
    county = request.form["county"].strip()
    validationResult = WebValidation.validateEditedSchoolLocation(schoolId, locationId, addressId, locationName, streetName1, streetName2, townOrCity, county)
    if validationResult == "OK":
        DataProcessing.updateLocationDetails(schoolId, locationId, addressId, locationName, streetName1, streetName2, townOrCity, county)
    return validationResult

@app.route("/removeLocation", methods = ["POST"])
def submit_remove_location():
    locationId = request.form["locationId"].strip()
    addressId = request.form["addressId"].strip()
    locationRemoved = DataProcessing.removeLocationRecord(locationId, addressId)
    if locationRemoved == True:
        return "OK"
    else:
        return "This location is the main location directly linked to your registered school account.\n\nThis location can only be edited. It cannot be removed."

#===== AJAX Account Management Methods ==============================================================================================================================

@app.route("/submitNewAccountPassword", methods = ["POST"])
def update_account_password():
    schoolId = request.form["schoolId"].strip()
    accountStyle = request.form["accountType"].strip()
    currentPassword = request.form["currentPassword"].strip()
    newPassword = request.form["newPassword"].strip()
    confirmPassword = request.form["confirmPassword"].strip()
    validationResult = ""

    if accountStyle == "Administrator":
        validationResult = WebValidation.validateSchoolAccountDetails(schoolId, currentPassword, newPassword, confirmPassword)
    else:
        validationResult = WebValidation.validatePersonAccountDetails(schoolId, accountStyle, currentPassword, newPassword, confirmPassword)

    if validationResult == "OK":
        if accountStyle == "Administrator":
            DataProcessing.updateAccountPassword(schoolId, newPassword, "school")
        elif accountStyle == "Teacher":
            DataProcessing.updateAccountPassword(schoolId, newPassword, "teacher")
        elif accountStyle == "Student":
            DataProcessing.updateAccountPassword(schoolId, newPassword, "student")
    return validationResult

@app.route("/searchForTeacherAccount", methods = ["POST"])
def search_for_teacher_account():
    personName = request.form["searchEntry"]
    try:
        firstName = personName[0:personName.index(" ")]
        surname = personName[personName.index(" ") + 1:]
    except ValueError:
        firstName = ""
        surname = ""
    listOfTeacherAccounts = DataProcessing.getTeacherAccountsList(session.get("loginId"), firstName, surname)
    return json.dumps(listOfTeacherAccounts)

@app.route("/searchForStudentAccount", methods = ["POST"])
def search_for_student_account():
    personName = request.form["searchEntry"]
    try:
        firstName = personName[0:personName.index(" ")]
        surname = personName[personName.index(" ") + 1:]
    except ValueError:
        firstName = ""
        surname = ""
    listOfStudentAccounts = DataProcessing.getStudentAccountsList(session.get("loginId"), firstName, surname)
    return json.dumps(listOfStudentAccounts)

@app.route("/createNewPersonAccount", methods = ["POST"])
def create_new_person_account():
    personId = request.form["newAccountPersonId"]
    accountStyle = request.form["newAccountType"]
    password = request.form["newAccountPassword"]
    confirmPassword = request.form["newAccountConfirmPassword"]
    validationResult = WebValidation.validateExistingPersonAccountDetails(password, confirmPassword)
    if validationResult == "OK":
        DataProcessing.insertNewPersonAccount(accountStyle, personId, password)
    return validationResult

@app.route("/resetPersonAccount", methods = ["POST"])
def reset_existing_person_account():
    personId = request.form["resetAccountPersonId"]
    accountStyle = request.form["resetAccountType"]
    password = request.form["resetAccountPassword"]
    confirmPassword = request.form["resetAccountConfirmPassword"]
    validationResult = WebValidation.validateExistingPersonAccountDetails(password, confirmPassword)
    if validationResult == "OK":
        DataProcessing.updateExistingPersonAccount(accountStyle, personId, password)
    return validationResult

@app.route("/removeSelectedAccount", methods = ["POST"])
def remove_existing_person_account():
    personId = request.form["resetAccountPersonId"]
    accountStyle = request.form["resetAccountType"]
    DataProcessing.deletePersonAccount(personId, accountStyle)
    return "OK"

#===== AJAX Lesson Management Methods ===============================================================================================================================

@app.route("/submitNewLesson", methods = ["POST"])
def insert_new_lesson():
    schoolId = request.form["schoolId"].strip()
    lessonName = request.form["nameOfLesson"].strip()
    abbreviatedName = request.form["abbreviatedName"].strip()
    lessonColour = request.form["colourOfLesson"].strip()
    validationResult = WebValidation.validateNewLessonDetails(schoolId, lessonName, abbreviatedName, lessonColour)
    if validationResult == "OK":
        DataProcessing.insertNewLessonRecord(schoolId, lessonName, abbreviatedName, lessonColour)
    return validationResult

@app.route("/searchForLesson", methods = ["POST"])
def search_for_lesson():
    lessonName = request.form["entrySearchBox"]
    listOfSchoolLessons = DataProcessing.getSchoolLessonDetails(session.get("loginId"), lessonName)
    return json.dumps(listOfSchoolLessons)

@app.route("/submitEditedLesson", methods = ["POST"])
def update_lesson_details():
    schoolLessonId = request.form["schoolLessonId"].strip()
    schoolId = request.form["schoolId"].strip()
    lessonId = request.form["lessonId"].strip()
    lessonName = request.form["nameOfLesson"].strip()
    abbreviatedName = request.form["abbreviatedName"].strip()
    lessonColour = request.form["colourOfLesson"].strip()
    validationResult = WebValidation.validateEditedLessonDetails(schoolLessonId, schoolId, lessonName, abbreviatedName, lessonColour)
    if validationResult == "OK":
        DataProcessing.updateLessonRecord(schoolLessonId, schoolId, lessonId, lessonName, abbreviatedName, lessonColour)
    return validationResult

@app.route("/removeLesson", methods = ["POST"])
def submit_remove_lesson():
    schoolLessonId = request.form["schoolLessonId"].strip()
    lessonId = request.form["lessonId"].strip()
    DataProcessing.deleteLessonRecord(schoolLessonId, lessonId)
    return "OK"

#===== AJAX Student Management Methods ==============================================================================================================================

@app.route("/submitNewStudent", methods = ["POST"])
def insert_new_student():
    schoolId = request.form["schoolId"].strip()
    firstName = request.form["firstName"].strip()
    surname = request.form["surname"].strip()
    dateOfBirth = request.form["dateOfBirth"].strip()
    streetName1 = request.form["streetName1"].strip()
    streetName2 = request.form["streetName2"].strip()
    townOrCity = request.form["townOrCity"].strip()
    county = request.form["county"].strip()
    phoneNumber = request.form["phoneNumber"].strip()
    emailAddress = request.form["emailAddress"].strip()
    confirmedEmail = request.form["confirmedEmail"].strip()
    validationResult = WebValidation.validateNewStudentDetails(schoolId, firstName, surname, dateOfBirth, phoneNumber, emailAddress, confirmedEmail,
                                                               streetName1, streetName2, townOrCity, county)
    if validationResult == "OK":
        DataProcessing.insertNewStudentRecord(schoolId, firstName, surname, dateOfBirth, phoneNumber, emailAddress, streetName1, streetName2, townOrCity, county)
    return validationResult

@app.route("/searchForStudent", methods = ["POST"])
def search_for_student():
    studentName = request.form["searchEntry"]
    try:
        firstName = studentName[0:studentName.index(" ")]
        surname = studentName[studentName.index(" ") + 1:]
    except ValueError:
        firstName = ""
        surname = ""
    listOfSchoolStudents = DataProcessing.getSchoolStudentsList(session.get("loginId"), firstName, surname)
    return json.dumps(listOfSchoolStudents)
    
@app.route("/submitEditedStudent", methods = ["POST"])
def update_student_details():
    schoolId = request.form["schoolId"].strip()
    personId = request.form["personId"].strip()
    studentId = request.form["thisPersonId"].strip()
    firstName = request.form["firstName"].strip()
    surname = request.form["surname"].strip()
    dateOfBirth = request.form["dateOfBirth"].strip()
    phoneNumber = request.form["phoneNumber"].strip()
    emailAddress = request.form["emailAddress"].strip()
    addressId = request.form["addressId"].strip()
    streetName1 = request.form["streetName1"].strip()
    streetName2 = request.form["streetName2"].strip()
    townOrCity = request.form["townOrCity"].strip()
    county = request.form["county"].strip()
    validationResult = WebValidation.validateEditedStudentDetails(schoolId, personId, firstName, surname, dateOfBirth, phoneNumber, emailAddress, streetName1,
                                                                  streetName2, townOrCity, county)
    if validationResult == "OK":
        DataProcessing.updateStudentRecord(schoolId, personId, studentId, addressId, firstName, surname, dateOfBirth, phoneNumber, emailAddress, streetName1,
                                           streetName2, townOrCity, county)
    return validationResult

@app.route("/removeStudent", methods = ["POST"])
def submit_remove_student():
    schoolId = request.form["schoolId"].strip()
    personId = request.form["personId"].strip()
    studentId = request.form["thisPersonId"].strip()
    addressId = request.form["addressId"].strip()
    DataProcessing.deleteStudentRecord(schoolId, personId, studentId, addressId)
    return "OK"

#===== AJAX Teacher Management Methods ==============================================================================================================================

@app.route("/submitNewTeacher", methods = ["POST"])
def insert_new_teacher():
    schoolId = request.form["schoolId"].strip()
    firstName = request.form["firstName"].strip()
    surname = request.form["surname"].strip()
    dateOfBirth = request.form["dateOfBirth"].strip()
    streetName1 = request.form["streetName1"].strip()
    streetName2 = request.form["streetName2"].strip()
    townOrCity = request.form["townOrCity"].strip()
    county = request.form["county"].strip()
    phoneNumber = request.form["phoneNumber"].strip()
    emailAddress = request.form["emailAddress"].strip()
    confirmedEmail = request.form["confirmedEmail"].strip()
    validationResult = WebValidation.validateNewTeacherDetails(schoolId, firstName, surname, dateOfBirth, phoneNumber, emailAddress, confirmedEmail,
                                                               streetName1, streetName2, townOrCity, county)
    if validationResult == "OK":
        DataProcessing.insertNewTeacherRecord(schoolId, firstName, surname, dateOfBirth, phoneNumber, emailAddress, streetName1, streetName2, townOrCity, county)
    return validationResult

@app.route("/searchForTeacher", methods = ["POST"])
def search_for_teacher():
    teacherName = request.form["searchEntry"] 
    try:
        firstName = teacherName[0:teacherName.index(" ")]
        surname = teacherName[teacherName.index(" ") + 1:]
    except ValueError:
        firstName = ""
        surname = ""
    listOfSchoolTeachers = DataProcessing.getSchoolTeachersList(session.get("loginId"), firstName, surname)
    return json.dumps(listOfSchoolTeachers)

@app.route("/submitEditedTeacher", methods = ["POST"])
def update_teacher_details():
    schoolId = request.form["schoolId"].strip()
    personId = request.form["personId"].strip()
    teacherId = request.form["thisPersonId"].strip()
    firstName = request.form["firstName"].strip()
    surname = request.form["surname"].strip()
    dateOfBirth = request.form["dateOfBirth"].strip()
    phoneNumber = request.form["phoneNumber"].strip()
    emailAddress = request.form["emailAddress"].strip()
    addressId = request.form["addressId"].strip()
    streetName1 = request.form["streetName1"].strip()
    streetName2 = request.form["streetName2"].strip()
    townOrCity = request.form["townOrCity"].strip()
    county = request.form["county"].strip()
    validationResult = WebValidation.validateEditedTeacherDetails(schoolId, personId, firstName, surname, dateOfBirth, phoneNumber, emailAddress, streetName1,
                                                                  streetName2, townOrCity, county)
    if validationResult == "OK":
        DataProcessing.updateTeacherRecord(schoolId, personId, teacherId, addressId, firstName, surname, dateOfBirth, phoneNumber, emailAddress, streetName1,
                                           streetName2, townOrCity, county)
    return validationResult

@app.route("/removeTeacher", methods = ["POST"])
def submit_remove_teacher():
    schoolId = request.form["schoolId"].strip()
    personId = request.form["personId"].strip()
    teacherId = request.form["thisPersonId"].strip()
    addressId = request.form["addressId"].strip()
    DataProcessing.deleteTeacherRecord(schoolId, personId, teacherId, addressId)
    return "OK"

#===== AJAX Classroom Management Methods ============================================================================================================================

@app.route("/submitNewClassroom", methods = ["POST"])
def submit_new_classroom():
    locationId = request.form["locationId"].strip()
    roomName = request.form["roomName"].strip()
    validationResult = WebValidation.validateClassroomDetails(locationId, roomName)
    if validationResult == "OK":
        DataProcessing.insertNewClassroomRecord(locationId, roomName)
    return validationResult

@app.route("/retrieveClassroomsList", methods = ["POST"])
def search_for_classrooms():
    locationId = request.form["locationId"].strip()
    listOfClassrooms = DataProcessing.getLocationClassroomsList(locationId)
    return json.dumps(listOfClassrooms)

@app.route("/submitEditedClassroom", methods = ["POST"])
def update_classroom_details():
    oldLocationId = request.form["originalLocationId"].strip()
    newLocationId = request.form["editableLocationId"].strip()
    classroomId = request.form["classroomId"].strip()
    roomName = request.form["roomName"].strip()
    validationResult = WebValidation.validateClassroomDetails(newLocationId, roomName)
    if validationResult == "OK":
        DataProcessing.updateEditedClassroomRecord(oldLocationId, newLocationId, classroomId, roomName)
    return validationResult

@app.route("/removeClassroom", methods = ["POST"])
def submit_remove_classroom():
    oldLocationId = request.form["originalLocationId"].strip()
    classroomId = request.form["classroomId"].strip()
    DataProcessing.deleteClassroomRecord(oldLocationId, classroomId)
    return "OK"

#===== AJAX Timetable Management Methods ============================================================================================================================

@app.route("/timetableStudentSearch", methods = ["POST"])
def retrieve_student_details():
    studentName = request.form["searchEntry"]
    try:
        firstName = studentName[0:studentName.index(" ")]
        surname = studentName[studentName.index(" ") + 1:]
    except ValueError:
        firstName = ""
        surname = ""       
    listOfStudents = DataProcessing.getListOfStudentNamesAndIds(session.get("loginId"), firstName, surname)
    return json.dumps(listOfStudents)

@app.route("/setSessionStudentId", methods = ["POST"])
def set_session_student_id():
    studentId = request.form["selectedStudentId"]
    try:
        session["studentId"] = int(studentId)
    except ValueError:
        session["studentId"] = 0

    if session.get("studentId") > 0:
        return "OK"
    else:
        return "ERROR"

@app.route("/scheduleALesson", methods = ["POST"])
def validate_scheduled_lesson():
    lessonValue = request.form["lessonEntryValue"]
    teacherValue = request.form["teacherEntryValue"]
    classroomValue = request.form["classroomEntryValue"]
    validationResult = WebValidation.validateScheduleLessonDetails(lessonValue, teacherValue, classroomValue)
    return validationResult

@app.route("/updateTimetable", methods = ["POST"])
def update_timetable():
    timetableStartHour = request.form["timetableStartHour"]
    timetableData = request.form["timetableData"]
    listOfTimetableData = timetableData.split()
    validationResult = WebValidation.validateLessonCollisions(int(timetableStartHour), listOfTimetableData)
    if validationResult == "OK":
        DataProcessing.updateTimetable(listOfTimetableData)
    return validationResult

@app.route("/updateALesson", methods = ["POST"])
def validate_updated_lesson():
    lessonValue = request.form["editedLessonValue"]
    teacherValue = request.form["editedTeacherValue"]
    classroomValue = request.form["editedClassroomValue"]
    validationResult = WebValidation.validateScheduleLessonDetails(lessonValue, teacherValue, classroomValue)
    return validationResult

@app.route("/loadRoomTimetable", methods = ["POST"])
def prepare_classroom_timetable():
    locationId = request.form["requestedLocationId"].strip()
    classroomId = request.form["classroomId"].strip()
    classroomLocationId = DataProcessing.getClassroomLocationIdForTimetable(int(locationId), int(classroomId))
    session["timetableId"] = classroomLocationId
    session["timetableType"] = "Classroom"
    return "OK"

@app.route("/loadTeacherSchoolTimetable", methods = ["POST"])
def prepare_teacher_school_timetable():
    teacherId = request.form["personId"]
    session["timetableId"] = teacherId
    session["timetableType"] = "TeacherSchool"
    return "OK"

@app.route("/loadStudentSchoolTimetable", methods = ["POST"])
def prepare_student_school_timetable():
    studentId = request.form["personId"]
    session["timetableId"] = studentId
    session["timetableType"] = "StudentSchool"
    return "OK"

#===== Other Methods ================================================================================================================================================

# Reset all of the session variables to their default values
def resetAllSessionVariables():
    session["loginId"] = 0
    session["loginName"] = "Undefined"
    session["loggedIn"] = False
    session["accountType"] = "Undefined"
    session["schoolName"] = "Not set"
    session["emailAddress"] = "Not set"
    session["password"] = "Not set"
    session["registered"] = False
    session["studentId"] = 0
    session["timetableId"] = 0
    session["timetableType"] = "Not set"

app.config['SECRET_KEY'] = 'SteinUmSteinMauerIchDichEinIchWerdeImmerBeiDirSein'
#if __name__ == "__main__":
app.run(debug = True)
