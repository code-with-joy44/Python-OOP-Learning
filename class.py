'''
class student:
    semster=""
    cgpa=""
joy=student()
print(isinstance(joy,student))
joy.semster='3rd'
joy.cgpa=3.7
print(f"Semester:{joy.semster} , CGPA:{joy.cgpa}")


class student:
    semster=""
    cgpa=""
    def display(self):
       print(f"Semester:{self.semster} , CGPA:{self.cgpa}")
joy=student()
joy.semster='3rd'
joy.cgpa=3.7
joy.display()

karim=student()
karim.semster='3rd'
karim.cgpa=4.00
karim.display()
'''
class student:
    semster=""
    cgpa=""
    def __init__(self,semester,cgpa):
        self.semster=semester
        self.cgpa=cgpa

    def display(self):
       print(f"Semester:{self.semster} , CGPA:{self.cgpa}")
joy=student(3,3.7)
joy.display()
karim=student(3,4.00)
karim.display()

def add(a,b):
    sum=a+b
    print(sum)
def sum (x,y):
    return x+y
add(3,2)
result=sum(3,2)
print(result)
su=(lambda m,n:m+n)(20,10)
print(su)
def display():
    print("Welcome to cst")
display()
