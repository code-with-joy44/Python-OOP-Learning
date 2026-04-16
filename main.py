#class and object
class stuent :
    roll=""
    gpa=""
joy=stuent()
print(isinstance(joy,stuent))
joy.roll=758516
joy.gpa=5.00
print(f"Roll:{joy.roll},GPA:{joy.gpa}")

class stuent :
    roll=""
    gpa=""
    def display(self):
        print(f"Roll:{self.roll},GPA:{self.gpa}")
joy=stuent()
joy.roll=758516
joy.gpa=5.00
joy.display()

karim=stuent()
karim.roll=102
karim.gpa=4.50
karim.display()

class stuent :
    roll=""
    gpa=""
    def setvalue(self,roll,gpa):
        self.roll=roll
        self.gpa=gpa
    def display(self):
        print(f"Roll:{self.roll},GPA:{self.gpa}")
joy=stuent()
joy.setvalue(101,5.00)
joy.display()

karim=stuent()
karim.setvalue(102,4.50)
karim.display()

#constructor
class stuent :
    roll=""
    gpa=""
    def in00t(self,roll,gpa):
        self.roll=roll
        self.gpa=gpa
    def display(self):
        print(f"Roll:{self.roll},GPA:{self.gpa}")
joy=stuent(101,5.00)
joy.display()

karim=stuent(102,4.50)
karim.display()







