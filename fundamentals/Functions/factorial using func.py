def fact(n):
    f=1
    for i in range (1,n+1):
        f=f*i
    print("Factorial of",n,"is",f)
a=int(input("Enter the number"))
fact(a)