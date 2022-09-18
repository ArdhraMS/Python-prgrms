#count the space vowels and consonents
str=input("Enter the string")
str1=str.lower()
space=0
count=0
vowel=0
for i in str1:
    if i in 'aeiou':
        vowel+=1
    elif i in " ":
        space+=1
    else:
        count+=1
print("Number of space",space)
print("Number of vowels",vowel)
print("Number of consonrnts",count)