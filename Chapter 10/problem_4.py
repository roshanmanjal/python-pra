# create a railway section to book ticket and fare etc
from random import randint

class Train():
    def __init__(self, Train_no):
        self.Train_no = Train_no
    def book(self, fro, to):
        print(f"The train ticket is booked from {fro} to {to} with train no {self.Train_no}")
    
    def getfare(self,fro, to):
        print(f"The train fare from {fro} to {to} with train no {self.Train_no} is {randint(111,5555)}")    
        
    def getstatus(self):
        print(f"The train no {self.Train_no} is runnig on time.")
        

t = Train(445343)
t.book("Rameshgwar","Mumbai")
t.getfare("Rameshgwar","Mumbai")
t.getstatus()