#Read a list str
#map              int
#odd list, even list             filter
#sum odd list        reduce
#sum even list       reduce
import functools
lst=input("Enter the elements in the list").split()
newlst=list(map(int,lst))
oddlist=list(filter(lambda x:x%2!=0,newlst))
evenlist=list(filter(lambda x:x%2==0,newlst))
print(newlst)
print(oddlist)
print(evenlist)
sumoddlist=functools.reduce(lambda x,y:x+y,oddlist)
sumevenlist=functools.reduce(lambda x,y:x+y,evenlist)
print(sumoddlist)
print(sumevenlist)