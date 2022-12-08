from Student_details import *

class Student(Student_details):
    def __init__(self):
        super().__init__()
        self.studentDetails = []
        self.pricourse = []
        self.seccourse = []

    #2. Registration for primary course
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

    #3. Registration for Secondary course
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

    #4. notification
    def notification(self,course_name):
        if(self.Course_Details[course_name]['no_of_students'] == 10):
            print("Selected course is full")
            return 1
        return 0
    
    #4. Add Students
    def addStudent(self):
        studentName = input("Enter the name : ")
        studentId = input("Enter the Id : ")
        pc=self.primaryCourse()
        sc=self.secondaryCourse()
        self.Student_Details[studentId] = {'Stud_name':studentName,'Primary_course':pc,'secondary_course':sc}
        print("Student is successfully added")

    #5. View Courses
    def viewCourses(self):
        print("sem\t\tcourse-1\tcourse-2\tcourse-3\tcourse-4\tcourse-5\tcourse-6\t")
        for sem in self.Course_Catalogue:
            print("")
            print(sem,end='\t\t')
            for sub in range(0,6):
                print(self.Course_Catalogue[sem][sub],end='\t\t')
        print("")

