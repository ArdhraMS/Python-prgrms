#OOPs-Object Oriented Programming
#class
#object
#Consider plan of house.                                        -->CLASS
#We are specificing no of doors, no of windows, no of bedrooms. --> DATA MEMEBERS
#Now we are making house 1, house 2, house 3 based on plan.     -->OBJECTS
#Data members are same for all the objects.

#Class--vechicle
#Colour
#Fuel Capacity
#Mileage
#Wheels
#Apply break() -->Function
#Change gear() -->Function
#Car,bus,bike  -->Ojects

#1.Abstraction   -->Act of representation essentail features without including background details. We can hide data.
#Data hiding     -->We need not represent all the data to viewers.
#2.Encapsulation -->Wrapping up of data memebers and methods.
#3.Inheritence   -->Inherite properties from parents.
#Eg: Class-bird
#Eyes,feathers,wings,legs,eat food()                        -->objective
#Flying birds                     Non flying birds          --->Another two classes
#Can fly()                        Not fly()                 --->Inherite objectives from parent class and get an addon features.
#Crow,parrot                      pegeion,emu               --->Objects
#4.Polymorphisym  -->Ability to exists in more than one form.
#Eg: 2+3=5                  -------->Here plus sign show arithematic addition.
#Hai+student= Haistudent    -------->Here plus sign add two strings together.
#In the above examples + means two different meanings.
class Student:#Refer notebook
     def read(self):
       self.rollno=int(input("Enter the roll number")) #------>Including data members
       self.name=input("Enter the name")               #------>Including data memebers
     def display(self):
        print("Roll no",self.rollno)
        print("Name",self.name)
#Object name=class name
s1=Student() #---->First object.
s1.read()    #---->Reading first data member.
s1.display() #---->Reading second data member.
s2=Student() #---->Second object.
s2.read()    #---->Reading first data member.
s2.display() #---->Reading second data member.
s3=Student() #---->Third object.
s3.read()    #---->Reading first data member.
s3.display() #---->Reading second data member.

