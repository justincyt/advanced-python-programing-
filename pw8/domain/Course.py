Course=[]
CourseID=[]
Credit=[]

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