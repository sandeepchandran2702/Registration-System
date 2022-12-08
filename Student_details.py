from Course_details import *

class Student_details(Course_details):
    def __init__(self):
        super().__init__()
        self.Student_Details = {'Stud_001':{'Stud_name':'Ajay','Primary_course':['ADC','DBMS','CA','DAA'],'secondary_course':['BDA','OS']},
                    'Stud_002':{'Stud_name':'Sharan','Primary_course':['EP-1','EC','PYTHON','EG'],'secondary_course':['BDA','OS']},
                    'Stud_003':{'Stud_name':'Subash','Primary_course':['ADC','DBMS','CA','DAA'],'secondary_course':['BDA','OS']},}

        self.Student_grades={'Stud_001':{'Sem_001':{'Sub_1':'A','Sub_2':'B','Sub_3':'A','Sub_4':'A+'},
                            'Sem_002':{'Sub_1':'A+','Sub_2':'B+','Sub_3':'O','Sub_4':'A+'},
                            'Sem_003':{'Sub_1':'A','Sub_2':'B','Sub_3':'A','Sub_4':'A+'}},
                'Stud_002':{'Sem_001':{'Sub_1':'A','Sub_2':'B','Sub_3':'A','Sub_4':'A+'},
                            'Sem_002':{'Sub_1':'A+','Sub_2':'B+','Sub_3':'O','Sub_4':'A+'},
                            'Sem_003':{'Sub_1':'A','Sub_2':'B','Sub_3':'A','Sub_4':'A+'}},
                'Stud_003':{'Sem_001':{'Sub_1':'A','Sub_2':'B','Sub_3':'A','Sub_4':'A+'},
                            'Sem_002':{'Sub_1':'A+','Sub_2':'B+','Sub_3':'O','Sub_4':'A+'},
                            'Sem_003':{'Sub_1':'A','Sub_2':'B','Sub_3':'A','Sub_4':'A+'}}}