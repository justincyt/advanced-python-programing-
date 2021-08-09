#Importing the library math and numpy 
import pickle 
import math
import numpy as np
import curses 

#student management 
Student=[]
StudentID=[]
Course=[]
CourseID=[]
Mark=[]
Credit=[]
gpa_s=[]
gpa_d=[]

#Using the curses
T_pain=curses.initscr()
curses.start_color()


        #------------------------ Class for Student, Course, Mark ------------------------#
#Create class and object for student, course,mark
class Students:
    def __init__(self,id,name,dob):
        self.id=id
        self.name=name
        self.dob=dob
        
        

    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_dob(self):
        return self.dob    


class Courses:
    def __init__(self,id,name,credit_course):
        self.id=id
        self.name=name
        self.credit_course=credit_course
      

    def get_id(self):
        return self.id
    def get_name(self):
        return self.name 
    def get_credit_course(self):
        return self.credit_course


class Marks:
    def __init__(self,id_student,id_course,mark,Gpa=0):
        self.id_student = id_student
        self.id_course = id_course
        self.mark=mark
        self.Gpa=Gpa
    

    def get_id_student(self):
        return self.id_student
    def get_id_course(self):
        return self.id_course
    def get_mark(self):
        return self.mark
    def get_Gpa(self):
        return self.Gpa
    def set_Gpa(self,Gpa):
        self.Gpa=Gpa
   

        #--------------------Create function get data from user------------------------------#  

#Create input of number of student 
def numberofstudent():
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
def add_student_infor():
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
def number_course():
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
    
             #-------------Function to show information of student, course,mark,GPA-----------------#

#Create a function to show all of student in class
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
    #-------------------------------------MAIN-------------------------------_----#


#recall student 
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




