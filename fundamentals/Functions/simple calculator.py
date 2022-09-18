def sum(n1,n2):
    s=n1+n2
    print("Sum is",s)
def sub(n1,n2):
    s=n1-n2
    print("Difference is",s)
def div(n1,n2):
    d=n1/n2
    print("Quoitent is",d)
def mul(n1,n2):
    m=n1*n2
    print("Product is",m)
while(1):
    print("Choices are 1.Addition 2.Subtarction 3.Multiplication 4.Division")
    n = int(input("Enter your choices"))
    a = int(input("Enter the first number"))
    b = int(input("Enter the second number"))
    if (n == 1):
        sum(a, b)
    elif (n == 2):
        sub(a, b)
    elif (n == 3):
        mul(a, b)
    elif (n == 4):
        div(a, b)
    else:
        print("WRONG CHOICE")
        break
        