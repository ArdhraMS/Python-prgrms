#Check a given number is perfect number or not.
#Perfect number=sum of factors give that number
#eg: 6=1+2+3+6
def func(n):
    sum=0
    for i in range(1,n):
        if(n%i==0):
            sum+=i
    if(sum==n):
        print(n,"is a perfect number")
    else:
        print(n,"is not a perfect number")
a=int(input("Enter the number"))
func(a)