Mark=[]
gpa_s=[]
gpa_d=[]

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
   
