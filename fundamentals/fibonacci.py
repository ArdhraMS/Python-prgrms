n=(int(input("Enter the limit")))
first=0
second=1
third=0
print(first,second,end=" ")
for i in range(2,n):
    third=first+second
    first=second
    second=third
    print(third,end=" ")