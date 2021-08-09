import numpy as np
import curses 
from domain.Student import * 
from domain.Course import *
from domain.Mark import *
#Using the curses
T_pain=curses.initscr()
curses.start_color()

class put_out:
        def show_student():
            T_pain.addstr("=======LIST STUDENT=======\n")
            T_pain.refresh()
            for Students in Student:
                T_pain.addstr("[ID-student: ] %s   [Name-student: ] %s    [DoB_Student: ] %s\n" % (Students.get_id(),Students.get_name(),Students.get_dob()))
                T_pain.refresh()

        #Create a function to show all of student course 
        def show_course():
            T_pain.addstr("=== LIST COURSE ===\n")
            T_pain.refresh()
            for Courses in Course:
                    T_pain.addstr("[ID-COurses]: %s    [Name-Course]: %s      [Credit-Course]: %s\n"%(Courses.get_id(),Courses.get_name(),Courses.get_credit_course()))
                    T_pain.refresh()

        #Function to show the mark of student 
        def show_mark():
            T_pain.addstr("=== LIST MARK ===\n")
            T_pain.refresh()
            for Marks in Mark:
                T_pain.addstr("[ID-course]: %s      [ID-Student]: %s       [mark]: %s\n"%(Marks.get_id_course(),Marks.get_id_course(),Marks.get_mark()))
                T_pain.refresh()

        #Function to show the GPA of Student
        def GPA_decending():
            arrr=np.array([gpa_s])
            arrr[::-1].sort()
            T_pain.addstr("The list is %s: \n"%(arrr))
            T_pain.refresh()