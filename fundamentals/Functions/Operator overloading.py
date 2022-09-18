#Operator overloading-->Similar to polymorphisum, here we can decide the action of operators.
#function overloading-->Not supported in python
#eg for function overloading
#int sum(int a,int b,int c)
#int sum(int a,int b)
#sum(2,3)
#sum(1,2,3)
#In the above example both the function name is sum but according the no of values given they are given to different function.
#In the above example sum(2,3) is given to int sum(int a,int b).
#In the above example sum(1,2,3) is given to int sum(int a,int b,int c).
class Point:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,other):
        newa=self.a+other.a
        newb=self.b+other.b
        return Point(newa,newb)
    def __str__(self):
        return"({0},{1})".format(self.a,self.b)
p1=Point(2,3)
p2=Point(3,4)
print(p1)
print(p2)
print(p1+p2)

#Creat a class with Complex number
# class complex:
