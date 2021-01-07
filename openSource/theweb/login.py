import flask
import sqlite3
import history_readfuns
import  os
import people_readfuns
import share_funs
app=flask.Flask(__name__)


@app.errorhandler(404)
def error_404(e):
    return flask.render_template("error_404.html"),404

@app.errorhandler(500)
def error_500(e):
    return flask.render_template("error_500.html"),500

@app.route('/')#最初首页
def login():
    return flask.render_template('login.html')

@app.route('/login_1/')#跳转界面1 开源历史
def login_1():
    thelist=history_readfuns.readperiods()#获得数据库中的所有历史信息的 阶段
    number=thelist.__len__()
    return flask.render_template('login_1.html',number=number,thelist=thelist)

@app.route('/login_2/')#跳转界面2 著名人物
def login_2():
    thelist = people_readfuns.readnames()  # 获得数据库中的所有人物信息的 人名
    number = thelist.__len__()
    return flask.render_template('login_2.html', number=number, thelist=thelist)

@app.route('/login_3/')#跳转界面3  优势
def login_3():
    return flask.render_template('login_3.html')

@app.route('/login_4/')#跳转界面4 协议
def login_4():
    return flask.render_template('login_4.html')

@app.route('/login_5/')#跳转界面5 分享
def login_5():
    thelist=share_funs.readnames()
    workpath=os.getcwd()
    number=1
    contents=[]
    webs=[]
    thepaths=[]
    for name in thelist:
        thepaths.append('../static/shareimgs/'+str(number)+'.jpg')
        thepath=workpath+'/static/shareimgs/'+str(number)+'.jpg'
        contents.append(share_funs.readcontent(name))
        webs.append(share_funs.readweb(name))
        share_funs.readimg(name,thepath)
        number=number+1
    return flask.render_template('login_5.html',contents=contents,webs=webs,thelist=thelist,thepaths=thepaths,number=number-1)

@app.route('/history/')  #接受查询的时期
def history_check():
    part_period=flask.request.args.get('period') #获得login_1返回的参数
    thelist=history_readfuns.readperiods()
    number=1
    for i in thelist:
        if str(i).startswith(part_period) :
            period=i
            break
        number=number+1
    time=history_readfuns.readtime(period)   #获取查询的内容
    content=history_readfuns.readcontent(period)
    contents=str(content).splitlines()
    imgpath=os.getcwd()+'/static/historyimgs/'+str(number)+'.jpg'   #不同的查询结果 生成的文件名称也不相同 避免浏览器缓存问题
    history_readfuns.readimg(period,imgpath)  #生成查询图片
    path='../static/historyimgs/'+str(number)+'.jpg'  #html中需要的图片路径
    return flask.render_template('history.html',contents=contents,time=time,period=period,path=path)

@app.route('/people/')  #接受查询的人名
def people_check():
    part_name=flask.request.args.get('name') #获得login_1返回的参数
    thelist=people_readfuns.readnames()
    number=1
    for i in thelist:
        if str(i).startswith(part_name) :
            name=i
            break
        number=number+1
    time=people_readfuns.readtime(name)   #获取查询的内容
    content=people_readfuns.readcontent(name)
    contents=str(content).splitlines()
    imgpath=os.getcwd()+'/static/peopleimgs/'+str(number)+'.jpg'   #不同的查询结果 生成的文件名称也不相同 避免浏览器缓存问题
    people_readfuns.readimg(name,imgpath)  #生成查询图片
    path='../static/peopleimgs/'+str(number)+'.jpg'  #html中需要的图片路径
    return flask.render_template('people.html',contents=contents,time=time,name=name,path=path)

if __name__=='__main__' :
    app.run()