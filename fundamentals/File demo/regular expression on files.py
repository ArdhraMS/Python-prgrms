import re
f1=open("File 1","r")
text=f1.readlines()
for line in text:
    result=re.search("you",line) #Here we are searching the you in the line .
    if(result):  #Here the sentence with you will be the result.
        print(line)

import re
f2=open("File 2","r")
text2=f2.readlines()
for lines in text2:
    result2=re.search(r"\bs.e\b",lines) #Here s will be searched at begining of the sentences it will also read s after comma.
    if(result2):
        print(lines)

import re
f3=open("File 2","r")
text3=f3.readlines()
for lines in text3==:
    result3=re.search(r"\bs\w*e\b",lines)  #\w is used to match characters
    if (result3):
        print(lines)