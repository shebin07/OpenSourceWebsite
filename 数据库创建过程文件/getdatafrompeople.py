import  os
import sqlite3
cx=sqlite3.connect("thetest1.db")
cu=cx.cursor()
sql1='select * from people_table'
sql2='select * from history_table where period=?'
periods={}
times={}
contents={}
imgs={}


result1=list(cx.execute(sql1))
resultnumbers=result1.__len__()

print(resultnumbers)

"""
f=open('newing1.jpg','wb')
f.write(result1[0][3])
f.close()
"""
#print(result1)
