def BinarySearch(list,key):
    mid=0
    low=0
    high=len(list)-1
    while(low<=high):
        mid=(low+high)//2
        if(list[mid]<key):
            low=mid+1
        elif(list[mid]>key):
            high=mid-1
        else:
            return mid
    return -1
list=input('Enter the items in the list').split()
list.sort()
key=input("Enter the element to be searched")
f=BinarySearch(list,key)
if(f==-1):
    print("Key not found")
else:
    print("Key found at",f+1)