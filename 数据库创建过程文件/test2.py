import os
import sqlite3

cx=sqlite3.connect('thetest1.db')
sql1='insert into share_table(name,content) values(?,?)'
content='ok'
name='myname'
#cx.execute(sql1,(name,content))

sql2='select img from share_table where name=?'
list1=list(cx.execute(sql2,(name,)))
print(list1)
if list1[0][0]==None :
    print("空")
else :
    print('非空')

cx.commit()
cx.close()