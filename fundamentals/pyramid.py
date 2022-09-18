n=int(input("Enter the number"))
x=1
for i in range(0,n):
    for k in range(0,n-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print(x,end=" ")
        x+=1
    print()
