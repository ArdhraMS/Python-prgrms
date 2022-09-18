n=int(input("Enter the number"))
num=n
sum=0
while(n>0):
    d=n%10
    sum+=(d**3)
    n=n//10
print(sum)
if(sum==num):
    print(num,"is an amtrsong number")
else:
    print("Not an anmstronge number")