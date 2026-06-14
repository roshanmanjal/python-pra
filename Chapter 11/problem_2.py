# create a class Animal then pets and then dogs and add mwthod bark in dogs
class Animals():
    pass

class Pets(Animals):
    pass

class Dogs(Pets):
     def bark(self):  # here it is self which takes class attribute if we do not want to write class we will do |
         print("Dogs do Bow Bow !!")
    

d = Dogs()
d.bark()

class Dogs(Pets):
    @staticmethod
    def bark():
         print("Dogs do Bow Bow !!")
    # this does not take any self as its static 

a = Dogs()
a.bark()