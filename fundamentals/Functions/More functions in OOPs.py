#Hide data members ABSTRACTION
class Rectangel:
    def read(self,l,b):
        self.length=l     #public data member   --->Can be accessed anywhere.
        self.__breadth=b  #private data member  --->Can only be accessed inside the class.
        # Here "__" is used to hide the data.
    def display(self):
        print("Length",self.length)
        print("Breadth",self.__breadth)
#Print the area
    def area(self):
        a=self.length*self.__breadth
        print("Area is",a)
R1=Rectangel()
R1.read(10,5)
R1.display()  #Here the hidden data member can only be accessed using a function.
R1.area()
print(R1.length)
print(R1.__breadth) #Here the hidden data memeber can not be accessed.

#Constructor -->Member function. ENCAPSULATION
#It is used to intialize data members.
#Default constructor is "__init__"
class Rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def display(self):
        print("Length",self.length)
        print("Breadth",self.breadth)
R1=Rectangle(10,5) #--->Here values will be given to respective variables
R1.display()
