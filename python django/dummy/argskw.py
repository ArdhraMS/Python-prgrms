# def add(n1,n2):
#     return n1+n2
# def add(n1,n2,n3):
#     return n1+n2+n3
# def add(n1,n2,n3,n4):
#     return n1+n2+n3+n4
#The above def of add will not be interpreted by python, it only use one add or one def.
#Here without definging add for differnt no of variables we can use arg.

def add(*args):
    print(args) #Here the value will be taken as tuple which is unmutable.
    return
add(2,3,4)


def display_person_data(*args,**kwargs):#**kwargs can also be written as **kw, only ** is important.
     print(kwargs)#Here kwarg is used to read to data i.e: key and value. In case of arg it is not possible.
display_person_data(eid=100,location="kakkanad",name="ram",job_loc="banglore")

