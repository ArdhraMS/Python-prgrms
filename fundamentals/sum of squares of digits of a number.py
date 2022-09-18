n=int(input("Enter thr number"))
sum=0
while(n>0):
    d=n%10
    sum+=(d*d)
    n=n//10
print("Sum is",sum)