n=int(input("Enter thr number"))
sum=0
while(n>0):
    d=n%10
    sum+=(d**3)
    n=n//10
print("Sum is",sum)