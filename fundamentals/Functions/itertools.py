import itertools
lst=[1,2,3,4]
res=list(itertools.accumulate(lst))
print(res)
#If we dont mention any operations in itertools it carryout addition.
#First element will be the same.
#The second element will be the sum of first and second element.
# The third element will be the sum of first three elements.
#The fourth element will be the sum of the first four elements.
#Output[1,1+2,1+2+3,1+2+3+4]=[1,3,6,10]
import itertools
lst1=[1,2,3,4]
res1=list(itertools.accumulate(lst1,lambda x,y:x*y))
print(res1)