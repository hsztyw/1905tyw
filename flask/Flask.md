# Flask

## 框架简介

重量级框架（django）

   核心代码量：提供了丰富的工具及组件

轻量级框架flask

​    自由灵活，高度订制：flask叫‘microframework’



Flask依赖六个库 

*  jinja2模板引擎，
* werkzeug WSGI工具集   执行流程，非常重要
* ITsdangerous  基于Django签名模块



主流原因

* 有非常齐全的官方文档，上手非常方便
* 有非常好的扩展机制和第三方扩展环境，工作中常见的软件都会有对应的扩展，动手扩展也很容易
* 社区活跃度非常高
* 微型框架的形式给了开发者更大的选择空间



## BS/CS

* bs：browser 浏览器      server  服务器     主流的
  * 打开浏览器就可以用，

* cs：client    客户端    server 服务器     
  * 有客户端的一般用在局域网，相对安全

![BS-CS区别](D:\Flask\writeRecord\img\BS-CS区别.png)





## MVC/MTV

MVC只能多写代码

是一个架构思想，所有编程语言都有。

* 是将MV实现代码分离。从而使同一个程序可以使用不同的表现形式。c的母的是确保M和V的同步，一旦M改变，V则同步更新

**MVC核心思想：解耦合**就是粘合度。降低模型层和视图层的耦合度

面向对象语言：高内聚、低耦合

MVC流程图

用户请求——>控制器——>模型层——>从数据库获取数据——>将数据返回给服务器——>服务器反馈给视图层

![ac6eddc451da81cb26660e7e5066d016](D:\Flask\writeRecord\img\ac6eddc451da81cb26660e7e5066d016.jpg)



## MTV

M ->M   V->T   C->V

M是模型   T是模板 页面   V是视图   控制器

Template  模板，模板可以写动态页面，html是静态页面，如果html需要改动，就需要手动添加html标签

![MTV](D:\Flask\writeRecord\img\MTV.png)



# Flask基本使用

web后端开发流程：

* 概要分析，分析要干什么
* 详细设计，把需要干的东西，详细设计
* 编码
* 测试
* 申请IP
* 备案
* 租赁服务器
* 部署    把项目放到服务器里
  * 浏览器
  * DNS服务器，专门做域名解析，浏览器先向dns服务器发送域名，dns解析之后ip发给浏览器，浏览器再用ip去访问服务器
  * 浏览器发送请求报文（请求头、请求体、请求行）给服务器
  * 服务器返回response（响应头、响应体、相应行）给浏览器
  * WSGI服务器网关接口，符合统一的规范叫规范。只要符合wsgi就可以自动部署到服务器上



![1568690670924](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568690670924.png)



虚拟环境、虚拟机、虚拟容器

虚拟环境是python独有的，隔离不同项目的玩意

~~~
virtualenv env  #在当前项目（目录）下创建一个虚拟环境，env名字可以随便取

source env/bin/activate   #激活虚拟环境，这里的env是上面的名字
#进入虚拟环境后，一切环境、软件包都没有，需要重新安装
~~~







## 创建Flask项目

~~~
1.安装
   pip install flask
   豆瓣源：pip install flask -i httt://douban什么玩意

2.创建第一个Flask项目
________________________________________________________
    from flask import Flask
    
    app=Flask(__name__)   #创建一个flask对象
    
    #这下面就是一个控制器
    @app.route('/')       #route按某路线分发，/表示根路由
    def hello（）         #定义一个视图函数
        return ‘百因必有果，你的报应就是我’
        
    app.run()             #运行
__________________________________________________________

2.启动flask对接的服务器，默认是开发者服务器 很low
   python 文件名 
   
3.代码写入方式
   a.终端中写flask代码
   b.专业版 creat project 选择flask
   c.社区版 直接创建文件，代码和终端写入的一样
   
3.服务器默认的端口号是5000，Django默认端口号是 8000

4.修改flask启动参数、命令参数
~~~

四套数据环境：开发环境，测试环境，演示环境，线上环境

* 创建一个flask项目
  * 在一个文件夹下面创建一个文件 hellofLASk.py
  * 在文件中写入代码
  * 访问项目   127.0.001:5000  默认端口号

**注** 如果终端中已经开启了服务器，namepycharm





## 修改Flask启动参数

~~~
修改端口和主机号
app.run（host  port  debug）   #默认情况下：_host='127.0.0.1'  _port=5000

可以在run的时候，修改为 run(host='0.0.0.0', port=999) 
-host是字符串
-port可以是正数也可以是字符串，其他必须是整型

一般不用run里修改

命令行参数：
   第三方扩展库可以让不修改启动参数，可以直接使用
   pip install flask-script
 
 --------------------------------------
   1.修改  .py文件为Manger.py
   
   2.manager = Manger(app=app)
   
   3.manager.run()
     就是将run交给manager
 --------------------------------------  

启动服务器改为   python manger.py  runserver
如果要按照自己的端口号来访问，则可以 python manger.py runserver -h 11.0.2.15   -p 3000

命令行运行参数：python manager.py runserver -h xx.xx.xx.xx -p xxxx -d  -r
     -p  port端口号
     -h  host主机
     -d  debug调试模式
     -r  reload重启加载，表示在改动python代码后，会自动重启，不需要关闭服务器

代码更新后，只能把服务器停了，才可以执行新的代码  
python manger.py runserver -r 实现了这个问题，在我们修改python代码后，服务器会自动重启
但如果是修改html不会自动重启，必须手动重启

python manger.py runserver -d   跟  run(debug=True)一样的意思

~~~



**PIN码，启动PIN码，每次开机后就要输入4-8位PIN码，三次输错，手机自动锁卡，并提示PUK码解锁**





## 视图函数

**对应的是MVC的C**

~~~
@app.route('/idex')
def index()
  return 'index请求'
如果路由的格式是/index/那么请求的资源路径是/127.0.0.1:5000/index,如果后面不写斜杠，会自动补全

@app.route('/index1/')
def index1():
    return 'index1'
如果路由格式的/index 不加斜杠，那么视图函数的请求资源路径用/index1/是无法请求的，必须与/index一致
~~~



## 视图函数的返回值

~~~
@app.route('/viewreturn/')
def viewreturn():
    return  ‘1’   #返回类型必须是一个字符串、字典，元组和response

执行函数，然后跳转到一个template文件夹的一个viewturn1的html页面
@app.route('/viewreturn1/')
def viewreturn1():
    return render_template('viewtrun1.html')    #render_template得到的返回值是一个字符串，具体是由flask自己设定的


静态文件css
@app.route('/staticss')
def  staticss():
    return render_template('viewtrun1.html')   只需要在html文件里导入静态文件就可以
~~~

![1568707376276](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568707376276.png)



**viewtrun的html页面**   

~~~
<link rel="stylesheet" href="/static/staticss.css">

<div>
   <ul>
      <li>sss</li>
      <li>fff</li>
      <li>bbb</li>
      <li>mmm</li>
      <li>aaaa</li>
   </ul>
</div>
~~~



## Flask启动参数、路由、动静态文件流程

~~~
#根据上面viewtrun的html页面来显示流程

from flask import Flask                  #导入Flask模块
from flask_script import Manager         #导入管理启动参数manager
===============================================================

app = Flask()                            #调用Flask类
manager = Manager(app=app)               #调用manager，取代app启动
===============================================================

@app.route('/')                          #路由函数
def route():
   return '这是首页'                      #给浏览器返回字符串
===============================================================
  
@app.route('/viewtrun/')                 #路由函数
def viewtrun():
   return render_template('viewtrun.html')   #给浏览器返回一个页面
#如果是导入项目中模块包的文件则要放到view视图里
===============================================================

manager.run()                            #从这里开始运行
===============================================================

终端启动：
python manager.py runserver -h 127.0.0.1 -p 5001 -r
~~~







## Flask基础结构

封装Flask，项目架构更加清晰，后面维护更加方便

~~~
1.创建一个App的python pack什么的，再把静态文件什么的文件夹放进去
  App
     templates
              html
     static
             css
             js
     views.py
     model.py
~~~

模板是做数据展示

***模型是表和类一一对应，表的字段就是类的属性***



## 蓝图

~~~
作用是用来规划urls（路由）

蓝图安装  pip install falsk-blueprint

初始化蓝图  blue=Blueprint（‘蓝图名’，__name_）
                                   #蓝图对象的创建和使用必须都在views里
注册蓝图    app.register_buleprint(blueprint=blue)
                                   #要在manager里注册蓝图

流程 
from flask  imoprt  Blueprint

blue = Blueprint（‘blues’，__name__）

app.register_blueprint(blueprint=bule)
                                                                                                         
~~~

循环引用

~~~
循环导入，在python中 1导入  B也可以导入A 但如果A来导入B则不行
        底层是线程挂起，两者都在等待状态
~~~



## 蓝图架构流程

### namager代码

~~~
#from flask import Flask                     #1.导入Flask
from flask_script import Manger              #1.导入manager
from App import create_app               #2.从init中导入app
from App.views import blue            #3.导入view的蓝图

#app = Flask(__name__)                       #1.调用flask
app=create_app()                         #2.这一步开始导入flask

manager = Manager(app=app)                   #1.使用manager管理app

#@app.route('/index')                        #1.设置路由函数
#def index():                                
#    return 'hello'

app.register_buleprint(blueprint=blue) #3.注册蓝图，需要从view视图里导入blue

if __name__=='__main__':
    manager.run()                            #1.使用manager管理启动       
~~~



### \_\_init_\_ 

~~~
from flask import  Flask                 #2.把app调到这里

def create_app()
   app=Flask(__name__)
   return app                            #2.导入这个包的时候，调用这个函数，返回一个app
~~~



### view

~~~
from flask import Blueprint             #2.导入蓝图包 
#蓝图的创建和使用必须在view里，其他地方不可行，也不报错
#用的是flask这个包，不用flask_blueprint的包

blue = Blueprint('first',__name__)       #2.初始化蓝图

#@app.route('/index/')                   #2.把路由路径放到view里，MVC问题
   #app.route（）放这里不可行，需要用蓝图

@blue.route('/index/')           #3.用蓝图来引导路由，资源路径
def index():
    return 'hello'
~~~

![蓝图创建说明版](D:\Flask\writeRecord\img\蓝图创建说明版.png)





1、封装的步骤

* 1.使用命令行参数
* 文件的封装
  * 创建一个python pack包、static、templates文件夹，views.py model.py
  * 在manager、views、models  瓜分代码
* 蓝图





# Flask请求流程

* 请求到路由    app.route()
* 视图函数      def index
* 视图函数和models交互
* 模型返回数据到视图函数
* 视图函数渲染模板
* 模板返回给用户

Flask最重要的就是路由的分发

![Flask请求流程](D:\Flask\writeRecord\img\Flask请求流程.png)





## 路由参数

路由参数：http:\//www\.baidu.com/s/1/

请求资源路径参数：http:\//www\.baidu.com/s?wd=韩跳跳

~~~
@app.route('/sss/<id>')     ——>路由参数
def sss(id):                ——>视图参数
    return 'ssss'
~~~





![1568771709735](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568771709735.png)

报错

![1568771744734](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568771744734.png)

<center>对的</center>
路由参数的基本结构/资源路径/<变量>/

路由参数的访问路径 http://127.0.0.1:5000/testsRoute/1

路由参数的名字一定要和视图参数一致。

路由参数传递到视图函数是字符串类型



### 路由参数的类型

**路由参数的类型默认情况下是字符串     还有Path  int  float  uuid  any**



**路由参数基础语法**

~~~~
<converter: var_name >
~~~~

  

### string

~~~
@blue.rout('/test/<string:name>/')
~~~



![1568773932023](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568773932023.png)

### Path

~~~~
@blue.rout('/test/<path:name>/')
~~~~

**String和path的区别**

string遇到/会当做结束标签

path遇到/会当做字符串



### int

~~~
@blue.rout('/test/<int:money>/')
def test(money)：
   return 'testmoney'
~~~



### Float

~~~
@blue.rout('/test/<float:price>/')
def test(price):
    return '啥玩意'
~~~



### UUID

~~~
先生成一个uuid
@blue.rout('/test/<uuid:uid>/')
def testuuid(uid):
~~~

![1568774590297](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568774590297.png)

### any

~~~
@blue.rout('/test/<any(a,b):p>/')      #表示浏览器给的数请求的参数是a，要么是b
def test(p):
    return '啥玩意'
~~~





## 请求方式

**请求方式又叫http方法**

* get（获取）
* post（添加）  
* delete  (删除)
* put（修改全部属性）   
* patch(修改部分属性）     



![1568775527276](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568775527276.png)

### 在view里get请求

~~~
@blue.route('/tologin/')
def tologin():
    return  render_template('login.html')


@blue.route('/login/')
def tologin():
    return  '欢迎光临红浪漫'
~~~



### post请求

* 路由默认只支持**get  head  options**请求方式，不支持post  delete  put  patch
* 如果想让路由支持post等等 可以在route方法中添加一个参数
* 参数为method=[]    里面的元素不区分大小写

~~~
@blue.route('/login/',methods=['post','delete'])
def tologin():
    return  '欢迎光临红浪漫'
~~~



### **postman**

针对于postman请求模拟工具

~~~
@blue.route('/topostman/')
def  testpostman():
     return  '你的梦想是什么'
~~~



## 反向解析

应用场景：增加代码灵活度，可以使得重定向的时候，代码不写死。

~~~
from flask import url_for

@blue.route('/reverse/')     ----->正常使用
def reverse():
    return 'teverse'
    
反向解析的语法  url_for(蓝图名.方法名)

@blue.route('/reverse1/')
def reverse1():
    #获取上面一个reverse的请求资源路径
    url_for('blue.reverse')    #得到的是reverse的请求资源路径
    return 'teverse1'
    
 应用场景：
         （1）重定向时候的可以用到 redirect('/index/'),企业里尽量不要使用硬编码，就是把代码写死了
             所以可以用反向解析  redirect(url_for('blue.index'))
         （2）在html中不要写硬编码，form action='/login/'
             可以写成  form action=url_for('blue.login')
~~~



# 视图函数的东西

reques   response  error  cookie  session



## 1.request

~~~
requerst是flask的内置对象。不需要创建就可以使用的对象

method base_url  host_url  url  remote_addr args form  
files  headers  path cookies  session

from flask import requerst

请求属性
@blue.route('/testRequerst/')
def testRequerst():
    print(requert.method)
    return 'testRequest'
    
    
1.method       #获取请求方式/http方法            **前后端分离

2.base_url     #去掉请求参数的路径
3.host_url     #主机的路径，不带请求资源路径
4.url          #完整url的路径，包含请求资源路径，请求参数    **
5.path         #请求资源路径，应用场景：购物车

6.remote_addr  #返回主机地址，可以做反爬虫                 **做反爬虫
7.files        #文件上传，应用场景：文件上传。
8.headers      #请求报文，爬虫的例子
9.cookies      #获取请求的cookies

10.args.get       #获取get的请求 
                    http://127.0.0.1/index/?name=123
                    	request.args.get
                    	request.args.get('name')
                    	
                    如果请求参数有两个，则只会返回第一个。或者用getlist
                    http://127.0.0.1/index/?name=123&age=10&age=11
                  	 	 request.args.get('age')  ——>10
                 		 request.args.getlist('age')  ——>[10,11]


11.form.get       #获取post请求
       name=request.form.get('name')     ——>获取表单的post请求         
       #form的存储结构和args一致
       
       
       
12.session         #不属于request的东西，是flask的一个内置对象

~~~

![1568786900628](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568786900628.png)



![request的args值1](D:\Flask\writeRecord\img\request的args值1.png)

![request的args值2](D:\Flask\writeRecord\img\request的args值2.png)









## Response

就是视图函数的返回值

（1） 字符串  （2）render_template   (3) make_response()    (4)redirect     (5)Response

~~~
1.视图函数返回字符串
@blue.route('/testResponse/')
def testResponse():
    return '百因必有果'
    
2.返回一个模板（html页面）
@blue.route('/Response/')
def Response():
    return render_template('response.html')         ——>返回的也是一个字符串
    return render_template('response.html',name=name)  -->传参数
    
3.返回一个make_response()
@blue.route('/Response/')
def Response():
    return make_response('<p>再见</p>')          ——>导入make_response,值必须是字符串类型的标签
                                                 ——>返回的是response类型
                                                 
4.返回一个redirect
@blue.route('/Response/')
def Response():
    return redircet('/testResponse')             ——>重定向到另一个路由路径
                   (url_for(blue.testResponse))  ——>返回的是response类型

5.返回一个response
@blue.route('/Response/')
def Response():
    return response('你的报应就是我')             ——>参数是字符串
~~~

****

**视图函数返回值有2大类，1.字符串  2.response**

字符串：

* String
* render_template       返回页面（参数是一个html页面）

response:

* make_response         返回的是一个标签（参数是一个带有标签的）
* redirect                       返回的是一个重定向路由路径（参数是一个重定向路径）
* Response                    返回给浏览器的是一个字符串 （参数是一个字符串）





## error异常

抛出异常

~~~
from flask import abort

@blue.route('/Abort/')
def Abort():
    abort（404）           #抛出404异常
    return '错了'          #这个基本不执行


@blue.errorhandler(404)    #对应的404异常
def Abort(Exception):      #参数必须是Exception
    return '系统升级中……'

1.先从页面中抛出异常状态码
2.用errorhandler来捕获对应的异常，如果是对应的抛出异常则执行下面的函数，如果没有，不报错，也不显示
3.解决异常函数，需要带一个参数  Exception
~~~





# 会话技术

1.当浏览器第一次访问服务器，服务器会创建一个session对象，该对象有个session_key属性，值是唯一的。

2.服务器响应时，返回set_cookie消息头，就是session_key,保存在session_id中

3.浏览器第二次以后的请求再次访问服务器的时候，会携带着session_id去服务器寻找如果找到了，就证明已经登陆过了，如果未找到，则需要重新登录

![seesion和cookie](D:\Flask\writeRecord\img\seesion和cookie.jpg)



* 请求过程request开始到response的连接都是短连接

* 延长交互的声明周期，将关键数据记录下来，就是cookie和session

* cookie是保存在浏览器端/客户端的状态管理技术

* Session是服务器端的状态管理技术



### Cookie

**cookie是客户端会话技术，所有数据存储在客户端，以key-value进行数据存储，服务器不做任何存储**

**特性：**

* 支持过时间
  * max_age     毫秒
  * expries      具体日期
* 根据域名进行cookie存储
* 不能夸浏览器
* 自动携带本网站的所有cookie
* cookie是服务器操作客户端的数据，通过response来操作

~~~
cookie登陆使用
	设置cookie    response.set_cookie('username',username)      #cookie是服务器创建的就用response
		                            #设置cookie必须要有response对象，分别是 make_response redirect  Response 
		                            #三种方法，最好用的是redirect
		                            
	获取cookie    username = request.cookies.get('username','游客')   #从浏览器中获取就用request，游客是默认值
		                             #如果为获取到username，则使用默认值‘游客’
	
	删除cookie    response.delete_cookie('username')       #在服务器中删除，就是用response来删除
		        
由于设置cookie和删除cookie都是由服务器来处理
因此，都是由相应response来操作。故而需要有response对象一般选择用redirect来获取。

response = redirect('/index/')     ========>redirect返回值是一个response
~~~



#### cookie的使用

~~~
需求：执行一个视图函数，跳转到一个logincookie.html页面
     输入一个用户名，点击提交，跳转到welcomecookie.html
     该页面内容叫   欢迎xxx 光临red romes
     如果没有经过登录，直接跳转到welcomecookie.html，会显示欢迎游客
     如果已经登录，然后直接跳转到welcome     会显示xxx.html内容，
     还有一个退出按钮，然后退出，调到welcomecookie.html页面
     显示欢迎游客
~~~

使用代码：

init.py

~~~
from flask import Flask

def new_app():
    app = Flask(__name__)
    return app
~~~



manager.py

~~~
from flask_script import manager
from App import new_app
from App.views import blue

app = new_app()
manager=Manager(app=app)

app.register_blueprint(blueprint=bule)
    
if  __name__=='__main__':
    manager.run()
~~~



views.py

~~~
from flask import Blueprint, render_template, request, redirect, url_for

blue = Blueprint('bluecookie',__name__)

@blue.route('/')
def first():
    return render_template('login.html')
    
@blue.route('/login',methods=['post'])
def login():
    name=request.form.get('name')
    response = redirect(url_for('bluecookie.welcome'))
    response.set_cookie('name',name)
    return response
    
@blue.route('/welcome/')
def welcome():
    name = request.cookies.get('name','游客')
    return render_template('welcome.html',name=name)    
    
@blue.route('/loginout')
def loginout():
    response = redirect(url_for('bluecookie.welcome'))
    response.delete_cookie('name')
    return response
~~~



login.html

~~~
<head>
    <meta charset="UTF-8">
    <title>login</title>
</head>
<body>
<form action="/login/" method="post">
    <p>用户名：<input type="text" name="name"></p>
    <input type="submit" value="提交">
</form>
</body>
</html>
~~~



welcome.html

~~~
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>welcome</title>
</head>
<body>
<h1>姑娘们！接客啦！{{name}}来啦！</h1>
<a href="/loginout/">退出</a>
</body>
</html>
~~~





# Session

**是服务器会话技术，所有的数据存储在服务器中，默认存储在服务器的内存中。**

~~~
还是view视图里

session实现登录
import session

@blue.route('/login/',methods=['post'])
def login():
    name = request.form.get('name')
    session['name'] = name
    return redirect(url_for('blue.welcome'))
    
@blue.route('/welcome/')
def welcome():
    name=session.get('name')
    return render_template('welcome.html',name)
    
@blue.route('/logout/')
def logout():
    response = redirect('url_for('blue.welcome')')
    #response.delete_cookie('session')
    session.pop('name')    -->这两种方法都成
    return response
    
单纯的要使用session需要在init中设置secret_key
     app.config['SECRET_KEY'] = '112'
     
~~~

<form action='{{url_for('blue.login')}}' method='post'>
    <input type='text' name='name'> 
    <input type='submit'>
</form>



## session持久化问题

flask-session 可以实现session持久化

缓存在磁盘上，管理磁盘使用lru中，就是最近最少使用原则，lru就是一个算法

~~~
pip install flask-session

1.持久化配置的init位置——>放在redis
   app.config('SESSION_TYPE')=‘redis’
                   如果报No module named ‘redis’ 表示环境没有redis，导入即可
                   session的生命周期是31天   Django是14天
                   注：必须先打开redisserver

   app.config['SESSION_KEY_PREFIX']='python1905'
                   设置前缀
   				
2.初始化session的对象
   1.Session(app=app)
   
3.配置SECRET_KEY='111'


~~~

![session持久更耐用](D:\Flask\writeRecord\img\session持久更耐用.png)



![session持久](D:\Flask\writeRecord\img\session持久.png)





# Template模板

页面接收有传递的参数，么有的参数，是无法传递

页面上写 {{ name }}    render_template（‘ss.html’,name='sss'）

模板的处理过程：加载和渲染

* 其实就是一个html文件，支持特定的模板语法，
* 开发速度快，广泛使用  html设计前后端分离，减少python复杂度，灵活、快速、安全，提供控制，继承等功能

结构标签

基层：base.html

~~~
<head>
    {% block %}
    
    {% endblock %}
</head>
~~~



~~~
{% block ext_css %}   /{% block extCss %}

{% block header %}

{% block content %}

{% block footer %}

{% block ext_js %}

~~~

子模板base1.html

~~~
{% extends ‘base’ %}

{% block footer %}
 什么什么的
{% endblock %}
~~~

![modles框架](D:\Flask\writeRecord\img\modles框架.jpg)



子模板base2.html

~~~
{% extends ‘base1’ %}

{% block header %}
   什么什么的
   {{ super() }} 当子模板和父模板的header一样，则会覆盖父模板，如果想要父模板东西，就可以用这个东西
   
{% endblock %}

{% block conter %}
     {% include ‘base3.html’%}   #调用另一个模板
{% endblock %}
~~~

![继承父模板](D:\Flask\writeRecord\img\继承父模板.png)

<center>
    继承父模板
</center>



![modle插入模板](D:\Flask\writeRecord\img\modle插入模板.png)

<center>
    modle插入模板
</center>



![模板相互导入结果](D:\Flask\writeRecord\img\模板相互导入结果.png)

<center>
    模板相互导入结果





### 3.宏定义

Django是不允许有方法的

宏定义就是在模板中写方法

~~~
@blue.route('/aaaa/')
def aaa():
   return render_template('test.html')
~~~

test.html

~~~
无参数的macro
{% macro say() %}     --->定义一个say方法
  不知道说啥
{% endmacro %}

{{ say() }}          ---->在html中再调用这个方法

{# 注释方法 #}

==============================================================
有参数的macro
{% macro getuser(name,age) %}
   {{name}}的年龄是{{age}}
{% endmacro %}

{{ getuser('zs',18) }}    ----->内部调用

================================================================
调用外部html的文件
{% from ‘test1.html’ import getname %}     ---->直接导入

{{ getname() }}      --->直接调用


另一个html，test1.html
{% macro getname() %}
     什么什么的
{% endmacro %}
~~~

![mecro无参数](D:\Flask\writeRecord\img\mecro无参数.png)

![mecro带参传递](D:\Flask\writeRecord\img\mecro带参传递.png)









循环控制

~~~
模板循环控制语句
@blue.route('/ccc/')
def ccc():
    score_list = [59,67,86,100]
    return render_template('testfor.html',score_list=score_list)

~~~

testfor.html

~~~~
{% for score in score_list %}
   <li>{{ score }}</li>
{% endfor %}

============================================================== 
for+if循环
{% for score in score_list %}
   {% if loop.first %}
    	<li style='color:green'>{{score}} </li>
   {% elif loop.last%}
    	 <li style='color:red'>{{score}} </li>
   {% else %}
         <li style='color:blue'>{{score}} </li>
   {% endif %}
{% endfor %}

===========================================================
{% for score in score_list %}
	{{ loop.index }}    	--->索引从1开始
	{{ loop.index0 }}  	 	--->索引从指定数开始
    {{ loop.revindex }} 	--->倒序索引
    {{ loop.revindex0 }} 	--->倒序到0
{% endfor %}

~~~~



过滤器

~~~
@blue.route('/filter/')
def filter():
    code='abcdfaljfwpr'
    code1=‘abdcl    ’
    code2=‘<h1>sss</h1>’
    return render_template('fliter.html',code=code,code1=code1,code2=code2)

~~~

filter.html

~~~
{{ code|upper }}     -->转大写
{{ code|lower }}

{{ code1|trim }}     -->去空格，只能去前后空格
{{code1|trim|reverse }}   --->翻转，倒着取

{{code2}}               ---><h1>sss</h1>
{{code2|striptags }}    --->去标签
{{code|safe }}          --->标签生效

#过滤可以无限次生效
~~~

