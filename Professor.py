from Professor_details import *

class Professor(Professor_details):
    def __init__(self):  
        super().__init__()         
        self.signcourse = []
        
    #8. View Students Details
    def studentsDetail(self):        
        print("Student Details")
        print("----------------")
        for student in self.Student_Details:
            # print("Student ID : ",self.Student_Details[student])
            print("Student Name : ",self.Student_Details[student]['Stud_name'])
            print("Primary Course: ",self.Student_Details[student]['Primary_course'])
            print("Secondary Course: ",self.Student_Details[student]['secondary_course'])
            print("----------------")
        print("")

    #9.Sign Up To Teach
    def signUp(self):
        professorId= input("Enter your ID : ")
        professorName= input("Enter your Name : ")
        for i in range(0,4):
            a=input("Enter the course name : ")
            self.signcourse.append(a)
        print(professorName," with professor ID",professorId," will handle ",self.signcourse)
        src=[professorId,professorName,self.signcourse]
        print("")
        return src
    
    #9. Add Professor
    def addProfessor(self):
        professorId= input("Enter your ID : ")
        professorName= input("Enter your Name : ")
        n=int(input("Enter the number of subjects handled : "))
        for i in range(0,n):
            a=input("Enter the course name : ")
            self.signcourse.append(a)
        print(professorName," with professor ID",professorId," will handle ",self.signcourse)
        department = input("Enter the department : ")
        self.Professor_Details[professorId]= {'Prof_name':professorName,'Handling_subject':self.signcourse,'Department':department}
        print("Professor is successfully added\n")
