# coding:utf-8
import  os
import sqlite3
#history_table 的相关内容读取
thedb="thetest1.db"#实际数据库文件的储存位置
#以列表形式返回所有的阶段名称
def readperiods():
    cx = sqlite3.connect(thedb)
    cu = cx.cursor()
    sql1='select period from history_table'
    thelist1=list(cx.execute(sql1))
    thelist2=[]
    resultnumbers=thelist1.__len__()
    for i in range(0,resultnumbers):
        thelist2.append(thelist1[i][0])
    cx.close()
    return thelist2

#给定period值返回对应的 content
def readcontent(period):
    cx = sqlite3.connect(thedb)
    cu = cx.cursor()
    sql1 = 'select content from history_table where period=?'
    thelist1=list(cx.execute(sql1,(period,)))
    content=thelist1[0][0]
    cx.close()
    return content

#给定period值返回对应的 time
def readtime(period):
    cx = sqlite3.connect(thedb)
    cu = cx.cursor()
    sql1 = 'select time from history_table where period=?'
    thelist1=list(cx.execute(sql1,(period,)))
    time=thelist1[0][0]
    cx.close()
    return time

#按照给定的period生成jpg文件 文件名由参数给出
def readimg(period,imgname):
    cx = sqlite3.connect(thedb)
    cu = cx.cursor()
    f=open(imgname,'wb')
    sql1 = 'select img from history_table where period=?'
    thelist1 = list(cx.execute(sql1, (period,)))
    f.write(thelist1[0][0])
    cx.close()
    return



