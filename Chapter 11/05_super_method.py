# multilevel inheritance
class Employee:
    def __init__(self):
        print("This is of Employee,")
    a = 1

class prgmer(Employee):
    def __init__(self):
        print("This is of prgmr,")
    b = 3
    
class Manager(prgmer):
    def __init__(self):
        super().__init__()  # this is used to call prgmr also [to access a super class super method is used] no need to run it again
        print("This is of Manager,")
    c = 3
    
# o = Employee()
# print(o.a)
# p = prgmer()
# print(f"This is taking value from Employee - {p.a}") 
# print(p.b)  # this is from prgmer
m = Manager()
print(m.b) # this value is from prgmer
print(m.c) # this value is from  manager own
print(m.a)  # this goes like manager -> prgmr -> Employee [MRO - Method Resolution Order]