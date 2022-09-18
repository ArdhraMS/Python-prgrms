import pymysql
db=pymysql.connect(host="localhost",user="root",passwd="root",db="database1")

#Prepare cursor object using cursor() method.
cur1=db.cursor()
sql="create table student1(Id int,Name varchar (10))"
cur1.execute(sql)
db.commit()

#Now just change the stmts in sql to insert values alter values etc...
cur1=db.cursor()
sql="insert into student1 values(14,Manna)"
cur1.execute(sql)
db.commit()

#To select the values the steps are different.
cur1=db.cursor()
sql="select * from student"
cur1.execute(sql)
rows=cur1.fetchall()
print("ID Name")
for i in rows:
    print(i[0],i[1])
db.commit()

#To print the name column only
cur1=db.cursor()
sql="select * from student"
cur1.execute(sql)
rows=cur1.fetchall()
print("Name")
for i in rows:
    print(i[1])
db.commit()

#To fetchone only fetch data from one row
cur1=db.cursor()
sql="select * from student"
cur1.execute(sql)
row=cur1.fetchone()
print("ID Name")
for i in row:
    print(row[0],row[1])
db.commit()