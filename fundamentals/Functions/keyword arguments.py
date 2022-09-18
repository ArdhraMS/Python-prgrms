def data(r,n):
    print("Roll no:",r)
    print("Name:",n)
data(n="Ram",r="10")  #These type of assignement of values to actual arugments are called KEYWORD ARGUMENTS.

def student_details(r,n,d="BCA"):  #DEFAULT ARGUMENTS, when the value is already given in the definition
    print("Roll no:",r)          #Default values should be written last.
    print("Name:",n)
    print("Departement",d)
student_details(1,"Adam")
student_details(1,"Adam","BSc")#If we give values to the default arguments it will change, if no values are given default will be printed

#Variable length arguments
def fun(*args):  #We can have varible length for the formal arguments.
    print(type(args))
    for i in args:
        print(i)
fun(1,2,3,4,5,6)