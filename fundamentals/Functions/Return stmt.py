def sum(a,b):
    c=a+b
    return c
n1=int(input("Enter the first number"))
n2=int(input("Enter the second number"))
s=sum(n1,n2)
avg=s/2
print("Average is",avg)

def calc(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum,sub,mul,div
m,n,o,p=calc(n1,n2)
print("Sum is",m)
print("Difference is",n)
print("Product is",o)
print("Quoitent is",p)