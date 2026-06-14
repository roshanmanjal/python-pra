class Employee_data:
    company = "Microsoft"
    
    def __init__(self, name, salary, pin):
        self.name = name 
        self.salary = salary
        self.pin = pin
        
p = Employee_data("Roshan", 120000, 421501)
print(f"Your name is -, {p.name} \nYour company name is -, {p.company} \nYour pin is -  {p.pin}, \nYour salary is -  {p.salary}")
