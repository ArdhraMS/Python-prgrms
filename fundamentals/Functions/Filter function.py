#Filter function
#Syntax  filter(function,sequence)
lst=[1,2,3,4,5]
result=filter(lambda x:x%2==0,lst)  #Only the elemets that satisfies the condition in lambda goes to result
print(list(result))

#Print the odd elemts
lst1=[1,2,3,4,5]
result1=filter(lambda x:x%2!=0,lst1)
print(list(result1))

#inputing list
lst2=input("Enter the elemets").split()
list2=map(int,lst2)
result2=filter(lambda x:x%2==0,list2)
print(list(result2))

#Creat a list from existing list which only contains multiples of 5
lst3=input("Enter the elements").split()
list3=map(int,lst3)
result3=filter(lambda x:x%5==0,list3)
print(list(result3))

#Create a list having values greater than 5
lst4=input("Enter the elemets").split()
list4=map(int,lst4)
result4=filter(lambda x:x>5,list4)
print(list(result4))

#Test: print odd number's sqaure even number exactly same
list5=[1,2,3,4,5,6,7,8,9]
print(list5)
result=[i*i if i%2!=0 else i for i in list5]
print(result)