def reverse(n):
    sum=0
    num=n
    while(n>0):
        r=n%10
        n=n//10
        sum=sum*10+r
    print("Reverse of",num,"is",sum)

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=i*fact
    print("Factorial of",n,"is",fact)