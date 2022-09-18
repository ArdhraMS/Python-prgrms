#Write a prgrm code for class rectangle with length and breadth as data members and display it and make objects.
class Rectangel:
    def getdata(self):
        self.length=int(input("Enter the length"))
        self.breadth=int(input("Enter the breadth"))
    def display(self):
        print("Length",self.length)
        print("Breadth",self.breadth)
#Print the area
    def area(self):
        a=self.length*self.breadth
        print("Area is",a)
R1=Rectangel()
R1.getdata()
R1.display()
R1.area()
R2=Rectangel()
R2.getdata()
R2.display()
R2.area()


#Read the class circle and find the area
class circle:
    def read(self,r):  #---->Given r in funcion definition  now it is a parametric function
        self.radius=r
        a=3.14*self.radius*self.radius
        print("Area is",a)
    def display(self):
        print("Radius is",self.radius)
C1=circle()
C1.read(12)   #--->Reads the value of r
C1.display()