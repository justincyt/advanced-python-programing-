
import numpy as np
import curses 
import pickle;
from zipfile import ZipFile
import os
from domain.Student import *
from domain.Course import *
from domain.Mark import *
from input import put_in
from output import put_out 
#Using the curses
T_pain=curses.initscr()
curses.start_color()

class mains():
    def management():
        T_pain .refresh()
        T_pain .clear()
        try:
            T_pain .addstr(0,5, "Do you wanna input of student and courses ?")
            T_pain .addstr(1,5, "1. Yes")
            T_pain .addstr(2,5, "2. No \n")
        except curses.error:
            pass
        ol = int(T_pain .getstr().decode()) 
        while True:
            if ol == 1:
                T_pain .clear()
                N_co = int(put_in.number_course())
                T_pain .clear()
                T_pain .refresh()
                for i in range (N_co):
                    T_pain .addstr(f"Course {i+1} \n")
                    put_in.add_course()
                    T_pain .refresh()
                    N_st = int(put_in.numberofstudent())
                    T_pain .refresh()
                    T_pain .clear()
                    for i in range (N_st):
                        T_pain .addstr(f"Student {i+1} \n")
                        put_in.add_student_infor()
                        T_pain .refresh()
                        T_pain .clear()
                        put_in.mark_mana()
                        T_pain .clear()
                        T_pain .refresh()
                break
            else:
                T_pain .addstr("say goodbye!!")
                curses.napms(2000)
                curses.endwin()
                exit()  
                
        T_pain .refresh()
        T_pain .clear()
        try:
            T_pain .addstr(0,5, "Do you want to calculater GPA of student ?")
            T_pain .addstr(1,5, "1. Yes")
            T_pain .addstr(2,5, "2. No \n")
        except curses.error:
            pass
        op_t = int(T_pain .getstr().decode())
        if op_t == 1:
            T_pain .refresh()
            put_in.aver_gpa()
            curses.napms(2000)
            T_pain .clear()
            T_pain .refresh()
        else:
            T_pain .addstr("The End")
            curses.napms(2000)
            curses.endwin()
        
        while True:
            T_pain .addstr("1. Show of Students: \n")
            T_pain .addstr("2. Show of Courses: \n") 
            T_pain .addstr("3. Show marks \n")
            T_pain .addstr("4. GPA_descending \n")
            T_pain .addstr("5. Using pickle to save it to file \"students.txt\" \n")
            T_pain .addstr("6. Decompress and load file \n")
            T_pain .addstr("7. Stop \n")
            ol_p = int(T_pain .getstr().decode())
            T_pain .refresh()
            T_pain .clear()
            T_pain .refresh()
            if ol_p == 1:
                put_out.display_student()
            if ol_p == 2:
                put_out.display_course()
            if ol_p == 3:
                put_out.display_mark()
            if ol_p == 4:
                put_out.GPA_decending()
            if ol_p == 5:
                with open('Student.dat', 'wb') as file_students:
                    for student_in in Student:
                        pickle.dump(student_in, file_students)
                    for course_in in Course:
                        pickle.dump(course_in, file_students)
                    for mark_in in Mark:
                        pickle.dump(mark_in, file_students)
                file_students.close()

            if ol_p == 6:
                if os.path.isfile('students.dat'):
                    T_pain .addstr("This file students.dat exits \n")
                    # open file, where you stored the pickled data
                    file = open('students.dat', 'rb')

                    #  dump information to that file
                    data = pickle.load(file)

                    # close the file
                    file.close()

            elif ol_p == 7:
                T_pain .addstr("Bye\n  ")
                T_pain .refresh()
                curses.napms(1000)
                curses.endwin()
                exit()
              
if __name__ == '__main__':
    mains.management()
  


