#Difference between map and filter function
#Map function makes the sequence under go the change as a whole
#i.e;All the elements in the list undergo changes
#Filter function only make changes in sequence to the elements which satisfies the condition
#i.e;The elements which satisfies the condition is filtered out from the list
lst=[15,11,12,4,8,6,7,9]
newlst=map(lambda x:x*x,lst)
print(list(newlst))
newlst1=filter(lambda x:x>10,lst)
print(list(newlst1))