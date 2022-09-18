#map function
mul=lambda n:n*n
num=(1,2,3,4,5)
result=map(mul,num)
print(tuple(result))

#Add each elemts of the list with other list whose has same index postions.
num1=[1,2,3,4,5]
num2=[6,7,8,9,10]
result=map(lambda x,y:x+y,num1,num2)
print(tuple(result))

#Print the length of string.
fruits=['Apple','Mango','Orange','Banana']
result=map(len,fruits)
print(tuple(result))

#Print alphabets of the string in a list as single elements eg: 'apple' ['a','p','p','l','e']
fruits=['Apple','Mango','Banana']
result=map(list,fruits)
print(list(result))