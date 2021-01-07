# coding:utf-8
import  os
import sqlite3


cx=sqlite3.connect("thetest1.db")
cu=cx.cursor()
sql1='insert into history_table values(?,?,?,?)'

period='GitHub 将开源“民主化”'
time='2008'
content="""最初，大多数自由和开源软件项目的贡献者通过电子邮件或私有的版本控制系统（如 Subversion 或 BitKeeper）进行协作。这种做法不仅笨重（因为没有集中的、精简的位置来查找开源项目和为其贡献），而且某些版本控制系统还是专有的。
诞生于2008年的 GitHub 改变了这一情况。GitHub 提供使用 Git 进行版本控制的软件源代码托管服务。Git 是一个开源的分布式版本控制系统，由 Linus Torvalds 开发，于2005年在 GPL 开源许可证下发布。最初目的是为更好地管理 Linux 内核的开发，用于替代他们曾经使用的闭源解决方案 —— BitKeeper。
GitHub 的出现，使得更多开发者能更方便地参与开源项目，为开源项目贡献，任何人都可以轻松提交自己的代码，并在 GitHub 上托管自己的开源项目。
因为几乎所有人都把自己的代码托管在 GitHub 上，所以更容易查找开源项目，而且协作方式的改变，开发者也不再需要获得开发者社区的权限才能参与开源项目。
"""
f=open('img10.jpg','rb')
img=f.read()
cx.execute(sql1,(period,time,content,img))

#sql2='delete from history_table where period="GNU 的诞生"'
#cx.execute(sql2)
#print(content)
cx.commit()
