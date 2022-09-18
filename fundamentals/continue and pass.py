#The statement in the loop skips while the condtion for CONTINUE is satisfied.

for i in range(1,6):
    if(i==3):
        continue
    print(i)
    print("hello")

#There is no much difference when PASS is used.

for i in range(1,6):
    if(i==3):
        pass
    print(i)
    print("hello")