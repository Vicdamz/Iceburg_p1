# basic about how to define class, methods and objects
class Student:
    
    def __init__(self, name, marks_1, marks_2, marks_3):               #class initialize
        self.name = name
        self.marks_1 = marks_1
        self.marks_2 = marks_2
        self.marks_3 = marks_3
    def welcome(self):                             #methods
        print("welcome student". self.name)

    def avg(self):
        return (self.marks_1 + self.marks_2 + self.marks_3)/3

s1 = Student("Kumar vikhyat",66, 24, 33)                    #object creation
s2 = Student("Swarnalina", 24, 67, 66)
s3 = Student("Mohan", 45, 84, 54)

print(s3.avg())