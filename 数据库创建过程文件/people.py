import  os
import sqlite3
cx=sqlite3.connect("thetest1.db")
cu=cx.cursor()
#cx.execute('drop table history_table')
sql1=f"""create table people_table(
name varchar(50),
time varchar(50),
content text,
img blob
);
"""
#cx.execute(sql1)
#构建history表格

sql4=''

sql3='select * from sqlite_master where type="table" and name="people_table";'#查看history_table 表结构的语句

#cx.execute(sql2,(period,time,content))
sql2='update people_table set img=? where name=?'
f=open('img7.jpg','rb')
img=f.read()

cx.execute(sql2,(img,'Guido van Rossum'))
#print((cx))
print(list(cu.execute(sql3)))
cx.commit()