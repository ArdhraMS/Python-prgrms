#A function called by itself.
#Factorial of a number.
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(4))


#Sum of first n natural  numbers using recursion
def func(n):
    if n==0:
        return 0
    else:
        return n+func(n-1)
print(func(4))
