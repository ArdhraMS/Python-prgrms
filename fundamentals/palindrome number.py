n=int(input("Enter the number"))
str1=str(n)      #converted n into string
str2=str1[::-1]
print(str2)
if(str1==str2):
    print("Is palindrome")
else:
    print("Not palindrome")
