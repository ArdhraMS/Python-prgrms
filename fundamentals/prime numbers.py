#upper limit=100
#lower limit=50
#for loop
u=int(input("Enter the upper limit"))
l=int(input("Enter the lower limit"))
for i in range(l,u):
    for j in range(2,i-1):
        if (i%j==0):
            break
 #dbt
    else:
            print(i,end=" ")