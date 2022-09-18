import pymysql
db=pymysql.connect(host="localhost",user="root",passwd="root",db="database1")
cur1=db.cursor()
sql="create table student_details(Adno int,Name varchar(10),Average int, Sex varchar(1))"
cur1.execute(sql)
db.commit()