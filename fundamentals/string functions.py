#find
str1="i like python"
r=str1.find("python")
print(r)
#read a string and a substring and print whether the substring is present in the string.
#i am very happy
#sad
#substring in not present in the string
#present at the location
str1=input("Enter the string")
sub=input("Enter the substring")
r=str1.find(sub)
if (r>=0):
    print("Substring is present at the location",r)
else:
    print("Substring is not present")