#Exception-unnormal errors during execution of prgrms
a=int(input("Enter the first number"))
b=int(input('Enter the second number'))
div=a/b
print("Result:",div)
#Here if we give value of a=8 and value of b=0 then it will show error irespective of our correct prgrm code.
#In such cases we use 'try' and 'except'.
a=int(input("Enter the first number"))
b=int(input('Enter the second number'))
try:  #Suspected code- chances of having errors in run time
    div=a/b
    print("Result:",div)
except:  #Code for handling exceptions
    print("Do not enter zero as second number")