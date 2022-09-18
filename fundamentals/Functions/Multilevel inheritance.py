#Multilevel inheritance
#A-->B-->C
#Student-->Parent class
#  def getdata()-->roll,name
#  def printdata()
#Mark-->child
#  def getmark()-->read mark-->out of 500
#  def printmark()
#Garde
#  def calculate grade()
#  p=mark/500*100
class Student:
    def getdata(self):
        self.roll=int(input("Enter the roll number"))
        self.name=input("Enter the name")
    def printdata(self):
        print("Roll no is",self.roll)
        print("Name is",self.name)
class Mark(Student):
    def getmark(self):
        self.mark=int(input("Enter the mark"))
    def printmark(self):
        print("Mark is",self.mark)
class Grade(Mark):
    def calculategrade(self):
        p=self.mark/500*100
        if(p>=80):
            print("Grade A")
        elif(p>=70):
            print("Grade B")
        elif(p>=60):
            print("Grade C")
        elif(p>=50):
            print("Grade D")
        else:
            print("Grade F, Failed")
obj1=Grade()
obj1.getdata()
obj1.getmark()
obj1.printdata()
obj1.printmark()
obj1.calculategrade()


#Same prgrm using "__init__"

class Student:
    def __init__(self,r,n):
        self.roll=r
        self.name=n
    def printdata(self):
        print("Roll no is",self.roll)
        print("Name is",self.name)
class Mark(Student):
    def __init__(self,r,n,m):
        Student.__init__(self,r,n)
        self.mark=m
    def printmark(self):
        print("Mark is",self.mark)
class Grade(Mark):
    def __init__(self,r,n,m):
        Mark.__init__(self,r,n,m)
    def calculategrade(self):
        p=self.mark/500*100
        if(p>=80):
            print("Grade A")
        elif(p>=70):
            print("Grade B")
        elif(p>=60):
            print("Grade C")
        elif(p>=50):
            print("Grade D")
        else:
            print("Grade F, Failed")
obj1=Grade(12,"Ardhra",490)
obj1.printdata()
obj1.printmark()
obj1.calculategrade()