#Importing the library math and numpy 
import math
import numpy as np
import curses 

from domain.Student import * 
from domain.Course import *
from domain.Mark import *

#Using the curses
T_pain=curses.initscr()
curses.start_color()

class put_in():
    def numberofstudent(self):
        while True:
            T_pain.addstr("Enter the number of student in  class:")
            T_pain.refresh()
            student_class=int(T_pain.getstr().decode())
            if(student_class<=0):
                curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
                T_pain.addstr("Does not exits!!!\n", curses.color_pair(1))
                T_pain.refresh()
                curses.napms(3000)
                T_pain.clear()
                T_pain.refresh()
            else:
                return student_class


    #Create function and add-student-information into this function
    def add_student_infor(self):
        T_pain.addstr("=== ADD STUDENT INFORMATION ===\n")
        T_pain.addstr("Enter the ID:")
        T_pain.refresh()
        id=T_pain.getstr().decode()

        T_pain.addstr("Enter the student name:")
        T_pain.refresh()
        name=T_pain.getstr().decode()

        T_pain.addstr("Enter the dob student:")
        T_pain.refresh()
        dob=T_pain.getstr().decode()

        st_infor=Students(id,name,dob)
        StudentID.append(id)
        Student.append(st_infor)
        T_pain.refresh()
        T_pain.clear()
        


    #Create function to input number of course
    def number_course(self):
        while True:
            T_pain.addstr("====NUMBER COURSE===\n")
            T_pain.refresh()
            T_pain.addstr("Enter the number of course are:")
            T_pain.refresh()
            number_course=int(T_pain.getstr().decode())
            if(number_course<=0):
                curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
                T_pain.addstr("Does not exits!!!\n", curses.color_pair(1))
                T_pain.refresh()
                curses.napms(3000)
                T_pain.clear()
                T_pain.refresh()
                
            else:
                return number_course

    #Create a function to add course         
    def add_course():
        T_pain.addstr("Enter the name course:")
        T_pain.refresh()
        name=T_pain.getstr().decode()
        
        T_pain.addstr("Enter the ID course:")
        T_pain.refresh()
        id=T_pain.getstr().decode()

        T_pain.addstr("Enter the credits are:")
        T_pain.refresh()
        credit_course=T_pain.getstr().decode()

        course_f=Courses(name,id,credit_course)
        Course.append(course_f)
        Credit.append(credit_course)
        CourseID.append(id)
        T_pain.refresh()
        T_pain.clear()


    #Create mark for students
    def mark_mana(): 
        for i in range(0,len(Student)):
            T_pain.clear()
            T_pain.addstr("===========INPUT MARK FOR STUDENT=============\n")
            T_pain.addstr("Enter the ID student:")
            id_student=T_pain.getstr().decode()
            T_pain.refresh()
            if id_student in StudentID:
                for j in range(0,len(Course)):
                    T_pain.addstr("Enter the ID course:")
                    id_course= T_pain.getstr().decode()
                    T_pain.refresh()
                    if id_course in CourseID:
                        T_pain.addstr("Enter the mark of student:")
                        mark=math.floor(float(T_pain.getstr().decode()))
                        T_pain.refresh()
                        if (mark<0) or (mark>20):
                            curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
                            try:
                                T_pain.addstr("Faild\n",curses.color_pair(1))
                            except curses.error:
                                pass
                            T_pain.refresh()
                            curses.napms(2000)
                            T_pain.clear()
                            T_pain.refresh()
                            T_pain.addstr("Try again\n")
                            mark=math.floor(float(T_pain.getstr().decode()))
                    
                    else:
                        exit()
            else:
                exit()                

        infor_mark=Marks(id_student,id_course,mark)
        Mark.append(infor_mark)
        gpa_d.append(mark)
    

    def aver_gpa():
        var=np.array([gpa_d])
        cred=np.array([Credit])
        T_pain.addstr("Enter name student that you want to calculate GPA:")
        name =T_pain.getstr().decode()
        if name in Student:
            for i in range(len(Mark)):
                recallcre=np.sum(cred)
                recallvar=np.sum(np.multiply(var,cred))
                T_pain.refresh()
                Gpa=recallvar/recallcre
                T_pain.refresh()                
        else: 
            return 0

        gpa_s.append(Gpa)
        T_pain.refresh()

        for st_infor in Mark:
            T_pain.clear()
            T_pain.refresh()
            T_pain.addstr(" Mark_studentid: %s   Gpa:%s \n" %(st_infor.get_id_course(), Gpa))
            T_pain.refresh()

            break
        