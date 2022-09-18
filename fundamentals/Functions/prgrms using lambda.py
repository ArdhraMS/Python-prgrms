#Using function find the largest among 3 numbers
def largest(a,b,c):
    if(a>b and b>a):
        print("Largest is",a)
    elif(b>c and b>a):
        print("Largest is",b)
    else:
        print("Largest is",c)
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
c=int(input("Enter the third number"))
largest(a,b,c)


#Using function return even number list
def evenfunc(lst):
    evenlist=[]
    for i in lst:
        if(i%2==0):
            evenlist.append(i)
    print(evenlist)
lst=[1,2,3,4,5,6,7,8,9,10]
evenfunc(lst)

#Linear search
def linearsearch(lst,key):
    for i in lst:
        if(i==key):
            print("Key found at",lst.index(i)+1)
            break
    else:
        print("Key not found")
lst=[1,2,3,4,5,6,7,8,9]
key=3
linearsearch(lst,key)