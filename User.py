class User():
    def __init__(self,username,password):
        self.username=username
        self.password=password
    #1. Authentication
    def authentication(self):
        if len(self.username)>5 and len(self.password)>5: 
            print(self.username," is valid")
            print("Authentication successful!!")
            print("")
            return True
        else:
            print("Authentication Failed!!")
            print("")
            return False