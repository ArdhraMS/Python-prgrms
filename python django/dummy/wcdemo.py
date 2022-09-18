person={
    "eid":1000,
    "dept":"market",
    "name":"Ram",
    "salary":25000
}
print(person)
print(person.get("salary"))
# print["gender"]="male"  #Here even though the code is wrong thr prgrm will exeute with only this stmt as error.
# print(person.get("gender"))="male" #Here the code will show error and output of previous code will not be shhown.
# print(person.get("gender")) #Here the ouyput eill be written as none.


#print person gender
person["gender"]="male"
print(person)

#update salary in person
person["salary"]+=5000
print(person)