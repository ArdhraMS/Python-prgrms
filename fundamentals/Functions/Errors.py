#ZeroDivisionError-division by zero
#NameError-variable is not defined, eg: if we are printing a non defined variable
#ValueError-invalid literal, eg: if we are inputing string in place of an integer.
try:
    a=int(input("Enter the first number"))
    b=int(input("Enter the second number"))
    c=a/b
    print(a,"/",b,"=",c)
except ValueError:   #Need to mention the errors else for any error the output will be shown as the string present in the except.
    print("You must enter a number")
except ZeroDivisionError: #Here if we are entering a string instead of integer it will show the result as "Division with zero not possible"
    print("Division with zero not possible")
#except (ValueError,ZeroDivisionError):
#    print("Handle both value errors and zero division errors")
except:
    print("All other errors handle error")
else:
    print("Execute if there is no errrors")
finally:
    print("Always execute")