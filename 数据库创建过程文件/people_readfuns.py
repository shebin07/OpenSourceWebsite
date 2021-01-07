# coding:utf-8
import  os
import sqlite3
#peopele_table 的相关内容读取
thedb="thetest1.db"#实际数据库文件的储存位置
#以列表形式返回所有的人名
def readnames():
    cx = sqlite3.connect(thedb)
    cu = cx.cursor()
    sql1='select name from people_table'
    thelist1=list(cx.execute(sql1))
    thelist2=[]
    resultnumbers=thelist1.__len__()
    for i in range(0,resultnumbers):
        thelist2.append(thelist1[i][0])
    cx.close()
    return thelist2

#给定name值返回对应的 content
def readcontent(name):
    cx = sqlite3.connect(thedb)
    cu = cx.cursor()
    sql1 = 'select content from people_table where name=?'
    thelist1=list(cx.execute(sql1,(name,)))
    content=thelist1[0][0]
    cx.close()
    return content

#给定name值返回对应的 time
def readtime(name):
    cx = sqlite3.connect(thedb)
    cu = cx.cursor()
    sql1 = 'select time from people_table where name=?'
    thelist1=list(cx.execute(sql1,(name,)))
    time=thelist1[0][0]
    cx.close()
    return time

#按照给定的name生成jpg文件 文件名由参数给出
def readimg(name,imgname):
    cx = sqlite3.connect(thedb)
    cu = cx.cursor()
    f=open(imgname,'wb')
    sql1 = 'select img from people_table where name=?'
    thelist1 = list(cx.execute(sql1, (name,)))
    f.write(thelist1[0][0])
    f.close()
    cx.close()
    return



