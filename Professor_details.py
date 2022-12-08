from Student_details import *

class Professor_details(Student_details):
    def __init__(self):
        super().__init__()
        self.Professor_Details = {'Prof_001':{'Prof_name':'Arun','Handling_subject':['OOPS','ADC'],'Department':'CSE'},
                    'Prof_002':{'Prof_name':'Samuel','Handling_subject':['BEEE','ITE'],'Department':'CSE'},
                    'Prof_003':{'Prof_name':'Surraj','Handling_subject':['CA','DBMS'],'Department':'CSE'},
                    'Prof_004':{'Prof_name':'Somesh','Handling_subject':['PS','CA'],'Department':'CSE'},}