#Find the sum of odd numbers less than n
i=1
sum=0
n=int(input("Enter the limit"))
while(i<=n):
    print(i)
    sum+=i
    i+=2
print("Sum is",sum)