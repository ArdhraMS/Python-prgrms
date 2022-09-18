#list
#heterogenous collection of datatypes
lst=[1,2,"adam",3.5,6]
#Both backward and forward indexing are possible
print(lst[-3])
print(lst[2])
print(lst[1:4])   #Forward indexing
print(lst[-4:-1])  #Backward indexing
print(lst[::-1])  #Reversing
print(len(lst))   #Findiing length
lst[0]=9  #Changing the value at[0]
print(lst)    #List is mutable
lst.append(11)  #Adding value to end of the list
lst.append(12)
print(lst)
lst.extend([3,4,5])  #Adding multiple value to the list
print(lst)
lst.insert(6,7)  #Adding value 7 at 6th postion
print(lst)
lst.pop()    #Pop the last element
print(lst)
lst.pop(2)   #Pop the value at lst[2]
print(lst)
lst.remove(2)  #Remove the value 2
print(lst)
lst.sort()   #To sort the list
print(lst)
lst.sort(reverse=True)    #Descending order
print(lst)
lst.reverse()    #Reverses the list
print(lst)
print(min(lst))
print(max(lst))

#Find the second largest element in the list
lst1=[1,2,34,12,89,8]
lst1.sort(reverse=True)
print(lst1)
print("Second largest number",lst1[1])

#Find the sum of all elements in the list
sum=0
for i in lst1:
    sum+=i
print('Sum is',sum)

#input the data value to list
lst=input("Enter the elements sepersted by space").split()  #If the bracket after split contains (","), then the values must be seperated by commas
print(lst)
sum=0
for i in lst:
    sum+=int(i) #Values inputed are entered in the form of string
print('Sum is',sum)

#print only even numbers from the list
lst=input("Enter the elements").split()
print(lst)
for i in lst:
    if(int(i)%2==0):
        print(i)

#print evenlist- only even numbers.
#print oddlist-only odd numbers.
lst2=input("Enter the elements to the list").split()
print(lst2)
oddlist=[]
evenlist=[]
for i in lst2:
    if(int(i)%2==0):
        evenlist.append(i)
    else:
        oddlist.append(i)
print("Odd number list is",oddlist)
print("Even number list is",evenlist)

#list inside list
lst3=[1,2,3,[4,5,[7,8]],9]
print(lst3[3][2][1])