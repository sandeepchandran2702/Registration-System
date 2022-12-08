class Generatereport():
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
     #4. view report
    def viewReport(self):
        regno=input("Enter your register number : \n")
        semester=input("Enter your semester number : \n")
        print("\nGRADE REPORT")
        print("------------")
        print("Reg No:",regno)
        print("Semester:",semester)
        print("------------")
        print("Course 1 : ",self.Student_grades[regno][semester]['Sub_1'])
        print("Course 2 : ",self.Student_grades[regno][semester]['Sub_2'])
        print("Course 3 : ",self.Student_grades[regno][semester]['Sub_3'])
        print("Course 4 : ",self.Student_grades[regno][semester]['Sub_4'])
        print("---------------------------")