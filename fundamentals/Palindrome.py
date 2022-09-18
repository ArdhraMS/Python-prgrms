#string palindrome
str=input("Enter the string")
str1=str[::-1]
print(str1)
if(str==str1):
    print("palindrome")
else:
    print("not palindrome")