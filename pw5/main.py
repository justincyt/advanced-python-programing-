import math
import numpy as np
import curses 
from zipfile import ZipFile
import os

from domain.Student import *
from domain.Course import *
from domain.Mark import *
from input import number_course,numberofstudent,add_course,add_student_infor,mark_mana,aver_gpa
from output import GPA_decending,show_course,show_student,show_mark
#Using the curses
T_pain=curses.initscr()
curses.start_color()

class mains():
    s=int(numberofstudent())
    for i in range(0,s):
        add_student_infor()
    show_student()

#recall course 
    c=int(number_course())
    for i in range(0,c):
        add_course()
    show_course()


#recall mark
    mark_mana()

#recall aver_gpa
    aver_gpa()

    T_pain.refresh()
    T_pain.clear()
    while True:
        T_pain.addstr("""=====YOUR OPTION=====\n""")
        T_pain.addstr("1.VIEW THE MARK OF STUDENT\n")
        T_pain.addstr("2.Compression data:\n")
        T_pain.addstr("3.Decompression data:\n")
        T_pain.addstr("4.NO\n")
        T_pain.refresh()
        ol = int(T_pain.getstr().decode())
        if ol == 1:
            T_pain.clear()
            T_pain.addstr("This is mark of student:\n")
            T_pain.refresh()
            T_pain.clear()
            curses.napms(2000)
            show_mark()
            T_pain.addstr("This is GPA of student\n")
            T_pain.refresh()
            curses.napms(2000)
            GPA_decending()
        if ol==2:
            listfile=['Student.txt','Courses.txt','Mark.txt']
            with ZipFile('student.dat','w') as zip_fs:
                for filename in listfile:
                    zip_fs.write(filename)
                for filename in listfile:
                    os.remove(filename)    
        if ol==3:
            if os.path.isfile('student.dat'):
                zip_file=ZipFile('student.dat','r')
                zip_file.extractall()
                if os.path.isfile('Student.txt'):     # Load data from students.txt
                    s = open('Student.txt', 'r').readline()
                if os.path.isfile('Courses.txt'):     # Load data from courses.txt
                    c = open('Courses.txt', 'r').readline()
                if os.path.isfile('Mark.txt'):      # Load data from marks.txt
                    m = open('Mark.txt', 'r').readline()
        elif ol==4:
            T_pain.addstr("THE END")
            curses.napms(2000)
            curses.endwin()
            exit()
mains()



