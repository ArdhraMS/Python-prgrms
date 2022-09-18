#Read the data from File 1 and write it on File 2.
f1=open("File 1","r")
lst=f1.readlines()
f2=open("File 2","w")
print(lst)
f2.writelines(lst)
f1.close()
f2.close()

#Read the number of words in File 1
f1=open("File 1","r")
r=f1.read()    #Now the stmts in the file 1 has been read.
words=r.split()#The stmts are splitted and stored in words.
print(words)
n=0
for i in words:
    n=n+1
print("No of words=",n)
#Now print the words only 1 time so first we convert them into set.
word1=set(words)
print(word1)
print("No of words",len(word1))
#Now from words print how many times each words are repeated
#how 2
#hello 2
# dict={"Hello":1,"Where":2} #----|
# print(dict)                #    |
# dict["are"]=4              #    |---->Basic concept of dictionary.
# dict["Hello"]+=1           #    |
# print(dict)                #----|
def wordcount(lst):
    dict={}
    for word in lst:
        if word in dict:
            dict[word]+=1  #----->Incrementing the number of word.
        else:
            dict[word]=1   #----->Adding the word to the dictionary.
    for k,v in dict.items(): #k for key and v for value
        print(k,":",v)
f1=open("File 1","r")
r=f1.read()
words=r.split()
wordcount(words)