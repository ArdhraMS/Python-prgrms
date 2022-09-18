# #Reduce function is defined in functool module
# import functools
# lst=[1,2,3,4,5,]
# res=functools.reduce(lambda x,y:x+y,lst)
# #Here x=1 and y=2 x+y=3
# #Then x=3 and y=3 x+y=6
# #Then x=6 and y=4 x+y=10
# #Then x=10 and y=5 x+y=15
# print(res)
#
##Return the largest number in the list using reduce function.
import functools
lst1=[1,2,3,4,5,6]
largest=functools.reduce(lambda x,y:,lst1)
print(largest)

