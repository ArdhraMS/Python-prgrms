# #INHERITANCE
# #Parent class/super class
# #Child class/derived
# #Single inheritance--> only one child class and one parent class.
# class Person:
#    def getdata(self):
#        self.vid=input("Enter voter id")
#        self.name=input("Enter the Name")
#    def printdata(self):
#        print("Voter ID",self.vid)
#        print("Name",self.name)
# class Employee(Person):
#     def getsalary(self):
#         self.salary=int(input("Enter the salary"))
#     def printsalary(self):
#         print("Salary is",self.salary)
# emp1=Employee()
# emp1.getdata()
# emp1.getsalary()
# emp1.printdata()
# emp1.printsalary()
#
#
# #Overriding --->Here the child class will execute when both the data objects in parent and child class are same
# #Prgrm
# class Person:
#    def getdata(self):
#        self.vid=input("Enter voter id")
#        self.name=input("Enter the Name")
#    def printdata(self):
#        print("Voter ID",self.vid)
#        print("Name",self.name)
# class Employee(Person):
#     def getdata(self):
#         super().getdata() #--->Here super makes execution of stmts in parent class
#         self.salary=int(input("Enter the salary"))
#     def printdata(self):
#         super().printdata()
#         print("Salary is",self.salary)
# emp1=Employee()
# emp1.getdata()   #-->Here the first priority will be for child class, as "super()" is written in rhe child function it will execute parent class.
# emp1.printdata()
#
# #Using "__init__" in the child class  as constructor is used it means it will automatically execute
# class Person:
#    def getdata(self):
#        self.vid=input("Enter voter id")
#        self.name=input("Enter the Name")
#    def printdata(self):
#        print("Voter ID",self.vid)
#        print("Name",self.name)
# class Employee(Person):
#     def __init__(self):
#         super().__init__()
#         self.salary=int(input("Enter the salary"))
#     def printdata(self):
#         super().printdata()
#         print("Salary is",self.salary)
# emp1=Employee()
# emp1.printdata()
#
##Giving "__init__" to both parent and child class having variables
class Person:
   def __init__(self,l,b):
       self.vid=l
       self.name=b
   def printdata(self):
       print("Voter ID",self.vid)
       print("Name",self.name)
class Employee(Person):        #class child (parent class)
    def __init__(self,l,b,s):  #Here values 123=l,ardhra=b,20000=s
        super().__init__(l,b)  #Here value of l and b will be given to parent class.
        self.salary=s
    def printdata(self):
        super().printdata()
        print("Salary is",self.salary)
emp1=Employee(123,"Ardhra",20000)  #Data of super class and sub class given in one stmt.
emp1.printdata()