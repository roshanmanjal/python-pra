class Employee:
    language = "Python,"  # class attribute
    salary = "1200000,"


print("First Employe details are =")
roshan = Employee()
roshan.name = "Roshan"
roshan.language = "Py"  # instance attribute [for changes we can edit some info]
# this will print new language..
print(roshan.language, roshan.salary, roshan.name)

print("Second Employe details are =")
rahul = Employee()
rahul.name = "Rahul"
print(rahul.language, rahul.salary, rahul.name)

print("Third Employe details are =")
rakesh = Employee()
rakesh.name = "Rakesh"
print(rakesh.language, rakesh.salary, rakesh.name)