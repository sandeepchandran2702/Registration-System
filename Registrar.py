from Professor_details import *

class Registrar(Professor_details):
    def __init__(self):
        super().__init__()
        self.pricourse = []
        self.seccourse = []
        self.signcourse = []
        self.studentDetails = []

   #11. Registration for primary course
    def primaryCourse(self):
        for i in range(0,4):
            a=input("Enter the course name ")
            available=self.notification(a)
            if(available == 1):
                print("Select other course")
                i-=1
            else:
                self.pricourse.append(a)
        print("Your primary courses are ",self.pricourse,"\n")
        return self.pricourse

    #12. Registration for Secondary course
    def secondaryCourse(self):
        for i in range(0,2):
            a=input("Enter the course name ")
            available=self.notification(a)
            if(available == 1):
                print("Select other course")
                i-=1
            else:
                self.seccourse.append(a)
        print("Your Secondary courses are ",self.seccourse,"\n")
        return self.seccourse

    #13. notification
    def notification(self,course_name):
        if(self.Course_Details[course_name]['no_of_students'] == 10):
            print("Selected course is full")
            return 1
        return 0
   

    #15. Cancel the course
    def cancelCourse(self):
        course=input("Enter the course Name : ")
        if(self.Course_Details[course]['no_of_students'] < 3):
            print("The course is deleted\n")
        else:
            print("The course cannot be deleted\n")

    #16. Add Students
    def addStudent(self):
        studentName = input("Enter the name : ")
        studentId = input("Enter the Id : ")
        pc=self.primaryCourse()
        sc=self.secondaryCourse()
        self.Student_Details[studentId] = {'Stud_name':studentName,'Primary_course':pc,'secondary_course':sc}
        print("Student is successfully added")

    #17. Add Professor
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
        print("Professor is successfully added")

    #18. Add course
    def addCourse(self):
        courseName = input("Enter the Course name :")
        semester = input("Enter the semester :")
        department = input("Enter the department :")
        prerequisites = input("Enter the prerequisites :")
        self.Course_Details[courseName]= {'Sem':semester,'Department':department,'Handled_by':['Ajay','Deepak'],'Prerequisites':prerequisites,'no_of_students':0}
        print(self.Course_Details)

    #19. Edit Student
    def editStudent(self):
        studentName = input("Enter the name : ")
        StudentId = input("Enter the Id : ")
        pc=self.primaryCourse()
        sc=self.secondaryCourse()
        print("Student is successfully edited")

    #20. Edit Professor
    def editProfessor(self):
        self.signUp()
        department = input("Enter the department")
        print("Professor is successfully edited")

    #21. Edit course
    def editCourse(self):
        courseName = input("Enter the Course name :")
        print("Old value :",self.Course_Details[courseName]['Sem']," Enter the new value :")
        semester = input("")
        print("Old value :",self.Course_Details[courseName]['Department']," Enter the new value :")
        department = input("")
        print("Old value :",self.Course_Details[courseName]['Prerequisites']," Enter the new value :")
        prerequisites = input("")
        self.Course_Details[courseName]= {'Sem':semester,'Department':department,'Handled_by':['Ajay','Deepak'],'Prerequisites':prerequisites,'no_of_students':0}
        print("Course is successfully edited")

    #22. Delete Student
    def deleteStudent(self):
        studentId = input("Enter the Id : ")
        del self.Student_Details[studentId]
        print("Student is successfully deleted")

    #23. Delete Professor
    def deleteProfessor(self):
        professorId = input("Enter the Id : ")
        del self.Professor_Details[professorId]
        print("Professor is successfully deleted")

    #24. Delete Courses
    def deleteCourse(self):
        courseName = input("Enter the name : ")
        del self.Course_Details[courseName]
        print("Course is successfully deleted")
        print(self.Course_Details)

    #25. View Courses
    def viewCourses(self):
        print("sem\t\tcourse-1\tcourse-2\tcourse-3\tcourse-4\tcourse-5\tcourse-6\t")
        for sem in self.Course_Catalogue:
            print("")
            print(sem,end='\t\t')
            for sub in range(0,6):
                print(self.Course_Catalogue[sem][sub],end='\t\t')

