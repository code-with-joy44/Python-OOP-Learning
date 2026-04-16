from abc import ABCxz,abstractmethod
class shape(ABC):#Here ABC=Abstract Base Class
    def __init__(self,dim1,dim2):
        self.dim1=dim1
        self.dim2=dim2
    @abstractmethod
    def area(self):
        pass
class triangle(shape):
    def area(self):
        result=0.5*self.dim1*self.dim2
        print("The area is:",result)
class rectangle(shape):
    def area(self):
        total=self.dim1*self.dim2
        print("The area is:",total)

t1=triangle(5,5)
t1.area()
t2=rectangle(5,5)
t2.area()