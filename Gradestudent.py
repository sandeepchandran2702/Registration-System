class Gradestudent():
    def __init__(self):
             self.Student_grades={'Stud_001':{'Sem_001':{'Sub_1':'A','Sub_2':'B','Sub_3':'A','Sub_4':'A+'},
                            'Sem_002':{'Sub_1':'A+','Sub_2':'B+','Sub_3':'O','Sub_4':'A+'},
                            'Sem_003':{'Sub_1':'A','Sub_2':'B','Sub_3':'A','Sub_4':'A+'}},
                'Stud_002':{'Sem_001':{'Sub_1':'A','Sub_2':'B','Sub_3':'A','Sub_4':'A+'},
                            'Sem_002':{'Sub_1':'A+','Sub_2':'B+','Sub_3':'O','Sub_4':'A+'},
                            'Sem_003':{'Sub_1':'A','Sub_2':'B','Sub_3':'A','Sub_4':'A+'}},
                'Stud_003':{'Sem_001':{'Sub_1':'A','Sub_2':'B','Sub_3':'A','Sub_4':'A+'},
                            'Sem_002':{'Sub_1':'A+','Sub_2':'B+','Sub_3':'O','Sub_4':'A+'},
                            'Sem_003':{'Sub_1':'A','Sub_2':'B','Sub_3':'A','Sub_4':'A+'}}}
   #7. Grade Student
    def gradeStudent(self):
        StuID=input("Enter your Student Id : \n")   
        semester=input("Enter your semester number : \n")
        sub1=input("Enter Grade for first course : \n")
        sub2=input("Enter Grade for second course : \n")
        sub3=input("Enter Grade for third course : \n")
        sub4=input("Enter Grade for fourth course : \n")
        self.Student_grades[StuID][semester] = {'Sub_1':sub1,'Sub_2':sub2,'Sub_3':sub3,'Sub_4':sub4}
        print("Successfully Entered the grades")
        print("---------------------------")