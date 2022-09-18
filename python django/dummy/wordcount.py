#Homework1: text="hello","hai","hello","hai","hai".
#Find the wordcount.
#Homework2: pattern:"ABAABCBBBBB"
#Find the first recursive character A
#Find the most recursive character B.

#Answer to homework1:
text="hello hai hello hai hai"
#Here () means tuple {} means dict.
#If we need set we have to write set{} and for list we have to write list().
wc={} #EMpty dictionary.
words=text.split(" ") #Here all the words in text will be splitted.
for w in words:
    if w in wc:  #Here first to come is hello, if hello was presnet before, it goes to "else" otherwise it goes to "if".
        wc[w]+=1
    else:
        wc[w]=1
print(wc)

#Answer to homework2:
pattern="ABAABCBBBBB"
wc1={}
for char in pattern: #Here each charcter from pattern will be read, then if is reading for first time it goes to "else" otherwise goes to "if".
    if char in wc1:
        print(char,"first rec character")
        break
    else:
        wc1[char]=1


#Homework3: master_word="AACCTTEGGROOB"
#chk_word="CAT",chk_word="CARROTT"
#Check if chk_work are made from master_word.