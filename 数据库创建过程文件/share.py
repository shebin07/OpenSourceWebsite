import  os
import sqlite3
cx=sqlite3.connect("thetest1.db")
cu=cx.cursor()
#cx.execute('drop table history_table')
sql1=f"""create table share_table(
name varchar(50) primary key,
web varchar(50),
content text,
img blob
);
"""
cx.execute(sql1)


sql4='drop table share_table'
#cx.execute(sql4)
cx.commit()

sql3='select * from sqlite_master where type="table" and name="share_table";'#查看share_table 表结构的语句
print(list(cu.execute(sql3)))
cx.commit()
#cx.execute(sql2,(period,time,content))




#print((cx))
