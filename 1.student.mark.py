#student management 
Student=[]
StudentID=[]
Course=[]
CourseID=[]
Mark=[]

#Create input of number of student 
def numberofstudent():
    student_class=int(input("Enter the number of class:"))
    if(student_class<=0):
        print("Doesn't exits")
        return 'False'
    else:
        return student_class


#Create function and add-student-information into this function
def add_student_infor():
    print("=== ADD STUDENT INFORMATION ===")
    
    id=input("Enter the ID:")
    name=input("Enter the student name:")
    dob=input("Enter the dob student:")
    st_infor={
        'id':id,
        'name':name,
        'dob':dob
    }
    StudentID.append(id)
    Student.append(st_infor)


#Create function to input number of course
def number_course():
    print("====NUMBER COURSE===")
    number_course=int(input("Enter the number of course are:"))
    if(number_course<=0):
        print("Doesn't exits")
        return 0
    else:
        return number_course

#Create a function to add course         
def add_course():
    name=input("Enter the name course:")
    id=input("Enten the ID course: ")
    course_f={
        'name':name,
        'id':id
    }
    Course.append(course_f)
    CourseID.append(id)


#Create mark for students
def mark_mana(): 
    g=1
    tu=len(Student)
    while g<=tu:
        g+=1
        a= input("Enter the ID Student: ")
        if a in StudentID:
            for i in range(0,len(Course)):
                b= input("Enter the ID Course: ")
                if b in CourseID:
                    mark= float(input("Enter mark of Student: "))
                    kk={
                       'a':a,
                       'b':b,
                       'mark':mark
                   }
                else:
                    print("Flase ID Student")
                    break
                Mark.append(kk)
        else:
            print("False ID course")
            break
        
#Create a function to show all of student in class
def show_student():
    print("==== LÍST STUDENT === ")
    for i in range(0,len(Student)):
        print(f"ID:{Student[i]['id']} name:{Student[i]['name']} DoB:{Student[i]['dob']}")

#Create a function to show all of student course 
def show_course():
    print("=== LIST COURSE ===")
    for i in range(0,len(Course)):
        print(f"ID:{Course[i]['id']}  name : {Course[i]['name']}")

#Function to show the mark of student 
def show_mark():
    print("=== LIST MARK ===")
    for i in range(0,len(Mark)):
        print(f"ID-course: {Mark[i]['b']} ID-Student: {Mark[i]['a']}  mark:{Mark[i]['mark']}")


#main 
#recall student 
s=int(numberofstudent())
l=1
while l<=s: 
    l+=1
    add_student_infor()
show_student()

#recall course 
c=int(number_course())
p=1
while p<=c:
    p+=1
    add_course()
show_course()

#recall mark
mark_mana()

print("""===YOUR OPTION===""")
print("1.YES")
print("2.NO")
for i in range (0,len(Course)):
    ol=int(input("Enter your option are:"))
    if ol ==1:
        print("====MARK OF STUDENT ====")
        show_mark()
        break
    else:
        break   











   