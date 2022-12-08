from Student_details import *

class Billing(Student_details):
    def __init__(self):
        super().__init__()

    def calculateAmount(self):
        reg=input("\nEnter the Student ID: ")
        print("\nBilling Details")
        print("---------------------------")
        temp=self.Student_Details[reg]['Primary_course']
        for sub in temp:
            print(sub,"  :$15")
        print("Total :$60")
        print("---------------------------")
        