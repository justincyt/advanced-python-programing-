import math
import numpy as np
import curses 

from domain.Student import *
from domain.Course import *
from domain.Mark import *
from input import number_course,numberofstudent,add_course,add_student_infor,mark_mana,aver_gpa
from output import GPA_decending,show_course,show_student,show_mark
#Using the curses
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

    T_pain.addstr(0,5,"""=====YOUR OPTION=====\n""")
    T_pain.addstr(1,5,"1.VIEW THE MARK OF STUDENT")
    T_pain.addstr(2,5,"2.NO\n")
        
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
    else:
        T_pain.addstr("THE END")
        curses.napms(2000)
        curses.endwin()




