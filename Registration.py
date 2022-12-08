from User import *
from Billing import *
from Professor import *
from Registrar import *
from Student import *
from Generatereport import *
from Gradestudent import *

class Registration:

    print("STUDENT REGISTRATION SYSTEM")
    print("---------------------------")
    print("LOGIN")
    username=input("Enter the username: ")
    password=input("Enter the password: ")
    user=User(username,password)
    if(user.authentication()):
        designation=input("Enter your Designation :\n1. Professor\n2. Student\n3. Registrar\n")
        print("")
        if designation == "1":
            p1=Professor()
            g1=Gradestudent()
            while True:
                choice=int(input("1. SignUp for course\n2. Students Detail\n3. Grade Students\n4. Exit\n"))
                if choice == 1:
                    p1.addProfessor()
                elif choice == 2:
                    p1.studentsDetail()
                elif choice == 3:
                    g1.gradeStudent()
                else:
                    break

        elif designation == "2":
            s1=Student()
            b1=Billing()
            g2=Generatereport()
            while True:
                choice=int(input("1. Registration\n2. Generate Report\n3. View Courses\n4. Billing\n5. exit\n"))
                if choice == 1:
                    s1.addStudent()
                elif choice == 2:
                    g2.viewReport()
                elif choice ==3:
                    s1.viewCourses()
                elif choice ==4:
                    b1.calculateAmount()
                else:
                    break

        else:
            r1=Registrar()
            while True:
                choice=int(input("1. Add Student\n2. Edit Student\n3. Delete Student\n4. Add Course\n5. Edit Course\n6. Delete Course\n7. Add Professor\n8. Edit Professor\n9. Delete Professor\n10.exit\n"))
                if choice == 1:
                    r1.addStudent()
                elif choice == 2:
                    r1.editStudent()
                elif choice ==3:
                    r1.deleteStudent()
                elif choice == 4:
                    r1.addCourse()
                elif choice ==5:
                    r1.editCourse()
                elif choice == 6:
                    r1.deleteCourse()
                elif choice ==7:
                    r1.addProfessor()
                elif choice == 8:
                    r1.editProfessor()
                elif choice ==9:
                    r1.deleteProfessor()
                else:
                    break
    else:
        print("Try again!!!")
        print("")