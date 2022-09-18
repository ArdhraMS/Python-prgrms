#julyn10
#tuple
tuple0=(1,3,45,1,2,1)
#tuple[1]=12  #Unmutable
print(tuple0)
print(len(tuple0))
print(tuple0.count(1))
print(tuple0.index(1))
#print(tuple.append(11)) #Unmutable
print(tuple0)
print(min(tuple0))
print(max(tuple0))
#sum of the digit
tuple1=(1,2,3,4,5,6,7,8,9,10)
sum=0
for i in tuple1:
    sum=sum+int(i)
print("The sum is",sum)
#or
#print(tuple1.sum())

#search a particular elemet in tuple9
tuple2=(1,2,3,4,5,6,7,8,9,0)
n=int(input("Enter the data to search"))
for i in tuple2:
    if i==n:
        print("Item found")
        break
else:
    print("Item not found")

#Enter the value in tuple
item=input("Enter the data").split()  #input taken as list
n=int(input("Enter the item tosearch"))
print(item)
tuple3=tuple(item)  #convert list to tuple
print(tuple3)
for i in tuple3:
    if(int(i)==n):
        print("Item found")
        break
else:
    print("Item not found")