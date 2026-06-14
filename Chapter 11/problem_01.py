# pgm to show 2Dand 3D vectors

class Twodvector():
    def __init__(self, i, j):
        self.i = i    
        self.j = j
    
    def show(self):
        print(f"The vector is :-  {self.i}i + {self.j}j ")
        
    
class threedvector(Twodvector):
    def __init__(self, i, j, k):
        super().__init__(i,j)
        self.k = k
        
    def show(self):
        print(f"The vector is :-  {self.i}i + {self.j}j + {self.k}k")
        
    
a = Twodvector(4,3)
a.show()
b = threedvector(1,34,5)
b.show()

