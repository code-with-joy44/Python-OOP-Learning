
class phone:
    def call(selfn):
        print("You Can Call")
    def messege(self):
        print("You Can Messege")
class realme(phone):
    def photo(self):
        print("You Can Take Photo")
r=realme()
r.call()
r.messege()
r.photo()
print(issubclass(realme,phone))
print(issubclass(phone,realme))
#Here phone is called parent class,super class,base class
#here realme is called child class,sub class,derived clas

#method overriding
class phone:
    def __init__(self):
        print("I am In phone class")
class realme(phone):
    def __init__(self):
        print("I am in realme class")
r=realme()
class phone:
    def __init__(self):
        print("I am In phone class")
class realme(phone):
    def __init__(self):
        super().__init__()
        print("I am in realme class")
r=realme()
#inheritence practise
class shape:
    def __init__(self,dim1,dim2):
        self.dim1=dim1
        self.dim2=dim2
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

