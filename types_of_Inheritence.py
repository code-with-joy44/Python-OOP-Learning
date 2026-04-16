 #Multilevel Inheritence
'''
class a:
    def t1(self):
        print("I am in class a")
class b(a):
    def t2(self):
        print("I am in class b")
class c(b):
    def t3(self):
        super().t1()
        super().t2()
        print("I am in class c")
ob1=c()
ob1.t3()
'''
#Multiple Inheritence
class a:
    def display(self):
        print("I am in class a")
class b:
    def display(self):
        print("I am in class b")
class c(a,b):
    def dis(self):
         print("I am in class c")
ob1=c()
ob1.display()
ob1.dis()

