#List comprehension
flowers=['lotus',"lilly","rose","sunflower"]
newlistf=[]
for i in flowers:
    if "o" in i:
        newlistf.append(i)
print(newlistf)

#cut shorting the prgrm= comprehending
#comprehended prgrm
newlist1=[i for i in flowers if 'o' in i]
print(newlist1)

#Converting the list to upper case
newlist3=[i.upper() for i in flowers]
print(newlist3)

#Change sunflower into any other flower
newlist4=["Hibiscus" if i=="sunflower" else i for i in flowers]
print(newlist4)


#Change all flowers except lilly to hibiscus
newlist5=["Hibiscus" if i!="lilly" else i for i in flowers]
print(newlist5)

#sqaure of numbers in the list
num=[1,2,3,4]
newnum=[i**2 for i in num]
print(newnum)

#without any list given
newlst=[i for i in range(1,6)]
print(newlst)


#Even number list
num1=[1,2,3,4,5,6,7,8,9]
newnum1=[i for i in num1 if i%2==0]
print(newnum1)

#Odd number list
newnum2=[i for i in num1 if i%2==1]
print(newnum2)

#print odd for odd numbers and even for even numbers in a new list
list=[1,2,3,4,5,6]
newlist=['even' if i%2==0 else 'odd' for i in list]
print(newlist)