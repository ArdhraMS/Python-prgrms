#Variables length arugment *args
def var_length(*arg):  #--->Onyly * is important arg is just a variable name.
   print(type(arg))
   for i in arg:
        print(i)
var_length(10,20)         #---->Here the values are stored as tuple.
var_length(1,2,3)

#Variable length arguments **kargs-keyword argument
def fun(**karg):    #-->Will be reading as dictioanry
    print(type(karg))
    for k,v in karg.items():
        print(k,":",v)

fun(Name="Anu",cls="BCA")


#Regular expression
import re
str="python programming is fun"
result=re.search("python",str)  #re.search(pattern,string)-->format
if result:                      #here we are searching "python" in str
    print("pattern exists")
else:
    print("pattern not exists")

import re
str="python programming is fun"
result=re.match("python",str) #Here as it is match only if the word exsist at the begining it will say pattern exists.
if result:
    print("pattern exists")
else:
    print("pattern not exists")

import re
zipcode="13242-4343-33-23aa"
new=re.findall('\d',zipcode)  #-->Here \d returns the digits
print(new)
new1=re.sub('\d','@',zipcode) #-->Here substitution takes place, here digits are sudstituted with @
print(new1)

#Checking if the password is valid.
#Conditions:
#characters 6-16
#a-z
#A-Z
#@$&
#If condions satiesfies then it is valid password else not valid password
import re
p=input("Enter the password")
if len(p)<=6 and len(p)>=16:
    print("Invalid passowrd")
elif not re.search("[a-z]",p): #Here if we dont find any characters from a to z then not true.
    print("Invalid password")
elif not re.search("[A-z]",p):
    print("Invalid password")
elif not re.search("[0-9]",p):
    print("Invalid password")
elif not re.search("[@$&]",p):
    print("Invalid password")
else:
    print("Valid password")