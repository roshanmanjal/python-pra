# multilevel inheritance
class Employee:
    a = 1

class prgmer(Employee):
    b = 3
    
class Manager(prgmer):
    c = 3
    
o = Employee()
print(o.a)
p = prgmer() # from Employee..
print(f"This is taking value from Employee - {p.a}") 
print(p.b)  # this is from prgmer
m = Manager()
print(p.b) # this value is from prgmer
print(m.c) # this value is from  manager own
print(m.a)  # this goes like manager -> prgmr -> Employee [MRO - Method Resolution Order]