n=(int(input("Enter a number")))
num=n
sum=0
while(n>0):
    d=n%10
    sum=sum*10+d
    n=n//10
print('Reverse of',num,'is',sum)
