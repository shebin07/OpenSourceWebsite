# coding:utf-8
import  os
import sqlite3


cx=sqlite3.connect("thetest1.db")
cu=cx.cursor()
sql1='insert into share_table values(?,?,?,?)'

name='simpleforum'
web='https://github.com/yujiandong/simpleforum'
content="""基于github的开源社区，自由度较高，使用方便。
"""
f=open('img5.jpg','rb')
img=f.read()
cx.execute(sql1,(name,web,content,img))

#sql2='delete from history_table where period="GNU 的诞生"'
#cx.execute(sql2)
#print(content)
cx.commit()