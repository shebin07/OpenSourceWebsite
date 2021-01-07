import  os
import sqlite3
cx=sqlite3.connect("thetest1.db")
cu=cx.cursor()
#cx.execute('drop table history_table')
sql1=f"""create table history_table(
period varchar(50),
time varchar(50),
content text,
img blob
);
"""
#cx.execute(sql1)
#构建history表格

sql3='select * from sqlite_master where type="table" and name="history_table";'#查看history_table 表结构的语句

#cx.execute(sql2,(period,time,content))

cx.execute(sql1)
#print((cx))
print(list(cu.execute(sql3)))
cx.commit()

