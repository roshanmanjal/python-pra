#  Use a static method to print Hello there!
class Calculator():
    def __init__(self, n):
        self.n = n
        
    def square(self):
        print(f"The square is -  {self.n*self.n}")
    def cube(self):
        print(f"The cube is - {self.n*self.n*self.n}")
    def squarroot(self):
        print(f"The squareroot is -  {self.n**1/2}")
    def add(self):
        print(f"The add is - {self.n+self.n}")
    @staticmethod  # static method does not require self it is called on own
    def hello():
        print("Hello There !!")
            
a  = Calculator(5)
a.hello()
a.square()
a.add()
a.cube()
a.squarroot()