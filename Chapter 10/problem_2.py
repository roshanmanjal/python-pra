#calculator to find square, cube, squareroot
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

a  = Calculator(5)
a.square()
a.add()
a.cube()
a.squarroot()