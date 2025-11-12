from abc import ABC, abstractmethod
class Shapes(ABC):
    def area(self):
        pass
class Square(Shapes):
    def area(self):
        print("Area is 25cm")
class Rectangle(Shapes):
    def area(self):
        print("Area is 40cm")
class Triangle(Shapes):
    def area(self):
        print("Area is 12cm")
class Parallelogram(Shapes):
    def area(self):
        print("Area is 40 cm ")
A = Square()
A.area()

B = Rectangle()
B.area()

C = Triangle()
C.area()

D = Parallelogram()
D.area()