class phone:
    def call(self):
        print('You can call')
    def messege(self):
        print('You can messege')
class realmi(phone):
    pass
p=realmi()
p.call()
print(issubclass(realmi,phone))
print(issubclass(phone,realmi))
#method overriding
class phn():
    def __init__(self):
        print('I am in phn class')
class oppo(phn):
    def __init__(self):
        super().__init__()
        print('I am in oppo class')

a=oppo()
class triangle:
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        area=0.5*self.base*self.height
        print(f"Area of triangle:",area)
t1=triangle(10,20)
t1.area()
t2=triangle(20,30)
t2.area()
#Abstraction
from abc import ABC,abstractmethod
class shape:
    def __init__(self,dim1,dim2):
        self.dim1=dim1
        self.dim2=dim2
    @abstractmethod
    def cal_area(self):
        pass
class Triangle(shape):
    def cal_area(self):
        result=0.5*self.dim1*self.dim2
        print("The area of triangle is:",result)
class Rectangle(shape):
    def cal_area(self):
        result=self.dim1*self.dim2
        print("The area of triangle is:",result)
T1=Triangle(20,30)
T1.cal_area()
T2=Rectangle(20,30)
T2.cal_area()




