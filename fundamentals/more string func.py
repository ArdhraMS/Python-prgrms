str1="Python programming"
print(str1.replace("m","n")) #to replace particular string
print(str1.replace("Python","c"))
#count the number of vowels in the string
str=input("Enter the string")
p=0
for ch in str:
    if ch in 'aeiouAEIOU':
        p+=1
print("No of vowels",p)
#count the number of a e i o u
str2=input("Enter the string")
a,e,I,o,u=0,0,0,0,0
for i in str2:
    if i in "aA":
        a+=1
    elif i in "eE":
        e+=1
    elif i in "iI":
        I+=1
    elif i in "oO":
        o+=1
    elif i in "uU":
        u+=1
print("No of a and A =",a)
print("No of e and E =",e)
print("No of i and I=",I)
print("No of o and O=",o)
print("No of u and U=",u)

      #0R
str3=input("Enter the string")
str4=str3.lower()
print("count of a",str4.count("a"))
print("count of e",str4.count("e"))
print("count of i",str4.count("i"))
print("count of o",str4.count("o"))
print("count of u",str4.count("u"))