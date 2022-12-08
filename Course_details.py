class Course_details():
    def __init__(self):
        self.Course_Details = {'CE': {'Sem':'sem_001','Department':'IT','Handled_by':['Ajay','Deepak'],'Prerequisites':'Basic English','no_of_students':'4'},
                  'EM-1': {'Sem':'sem_001','Department':'MATHS','Handled_by':['Ajay','Deepak'],'Prerequisites':'Maths','no_of_students':'4'},
                  'PYTHON': {'Sem':'sem_001','Department':'CSE','Handled_by':['Ajay','Deepak'],'Prerequisites':'C','no_of_students':'4'},
                  'EP-1': {'Sem':'sem_001','Department':'IT','Handled_by':['Ajay','Deepak'],'Prerequisites':'Basic Physics','no_of_students':'4'}}

        self.Course_Catalogue = {'sem_001':('CE','EM-1','EP-1','EC','PYTHON','EG'),
                    'sem_002':('TE','EM-2','EP-2','BEEE','ITE','C'), 
                    'sem_003':('DM','DPSD','DS','OOPS','ADC','IS'), 
                    'sem_004':('PS','CA','DBMS','DAA','OS','ESE'),
                    'sem_005':('CE','EM-1','EP-1','EC','PYTHON','EG'),
                    'sem_006':('TE','EM-2','EP-2','BEEE','ITE','C'), 
                    'sem_007':('DM','DPSD','DS','OOPS','ADC','IS'), 
                    'sem_008':('PS','CA','DBMS','DAA','OS','ESE')
    } 