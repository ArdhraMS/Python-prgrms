#file-->collection of data
#fileobject=open(file_name,mode)
#Here modes are
# r-->read
# r+-->read and write
# w-->write
# w+-->read and write
# a-->append
f1=open("File 1","r")
print("First location:",f1.tell())  #To print the initial pointer-->0,"tell()"-->to find the postion of the file pointer
print(f1.read(3))#Here first three contents get read from the file named "File 1"
print("Second location:",f1.tell())
print(f1.read(3)) #Here the output will produce next three charcter which also include \n which is not visible after the hai
print("Third location:",f1.tell())
print(f1.read(3))
print("Fourth location:",f1.seek(0))  #Here "seek" will make the pointer to go to the postion mentioned inside the bracket.
print(f1.read(3))  #Here as the seek(0) the pointer gors to zeroth postion and read three characters.
f1.close()
f2=open(r"C:\Users\ardhr\Desktop\Abc.txt","r") #Here we have given the location of a file created in desktop and read it.
print(f2.read(3))
f1.close()
f1=open("File 1","r")
print(f1.readline()) #Here we are reading one sentence.
f1.close()
f1=open("File 1","r")
print(f1.readlines()) #Here we are reading all the sentences which also includes \n.
f1.close()

#Write a prgrm so that all the stmts in the files come after other in down wards.
f1=open("File 1","r")
lst=f1.readlines() #We are making the data to a list.
for i in lst:
    print(i.strip())  #we wre striping off the space between two sentences.
f1.close()

#WRITE operation
f1=open("File 1","w")
f1.write("Hello")  #Here all the stmts will be over written by this stmt.
f1.close()
f1=open("File 1","w+")
f1.write("Hi")
print(f1.readlines())
f1.close()

#Write multiple lines
f1=open("File 1","w")
lst=["hello\n","how are you\n","where are you\n"]
f1.writelines(lst)
f1.close
#To append multiple lines
f1=open("File 1","a")
lst=["hello\n","how are you\n","where are you\n"]
f1.writelines(lst)
f1.close