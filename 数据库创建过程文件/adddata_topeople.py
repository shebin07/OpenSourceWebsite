# coding:utf-8
import  os
import sqlite3


cx=sqlite3.connect("thetest1.db")
cu=cx.cursor()
sql1='insert into people_table values(?,?,?,?)'

name='Eric Steven Raymond'
time='1957'
content="""埃里克·雷蒙德，全名“埃里克·S·雷蒙德”（Eric Steven Raymond）。常用名称ESR，著名的计算机程序员，开源软件运动的旗手。1957年，雷蒙德出生于美国马萨诸塞州的波士顿，正好就是黑客文化发源地MIT的所在，也是斯托尔曼发动自由软件运动的大本营。但雷蒙德从小就跟随父母在世界各地东奔西走，13岁之前已经学会了两种语言。1971年，他回到美国宾夕法尼亚州，1976年起开始接触黑客文化，1982年完成第一个开放源代码软件项目。雷蒙德不是光说不练的笔杆子，他是INTERCAL编程语言的主要创作者之一，曾经为EMACS编辑器作出贡献。雷蒙德还是著名的Fetchmail程序的作者。最近他还编写了一个最初用于Linux内核设置的设置程序。
雷蒙德的名言,“足够多的眼睛，就可让所有问题浮现。”（Given enough eyeballs, all bugs are shallow），对开放源代码运动影响很大，这亦即是著名的林纳斯定律。
1997年以后，雷蒙成为了开放源代码运动的主要理论家，以及开放源代码促进会（Open Source Initiative）的主要创办人之一。他还担任了开放源代码运动对媒体、商界以及主流文化的形象大使。他是一名优秀的演说家，并曾经到过六大洲的15个国家进行演说。他的话经常被主流媒体所引用，并是所有黑客中曝光率最高的。
"""
f=open('img8.jpg','rb')
img=f.read()
cx.execute(sql1,(name,time,content,img))

#sql2='delete from history_table where period="GNU 的诞生"'
#cx.execute(sql2)
#print(content)
cx.commit()