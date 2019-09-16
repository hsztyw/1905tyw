Redis    缓存

MongoDB   nosql的东西

html   HyperText M L    超文本，就是可以用文字图片视频颜色等等加在一起，被称为超文本

http协议：HyperText translation 超文本传输协议

1.为了保证传输的可靠性，底层使用的是tcp协议。

2.http使用的是短连接。是构建在长连接基础之上的短连接协议



* tcp建立连接需要三次握手，断开连接，四次挥手。
* 可靠：会验证数据的完整，保证数据传输的过程中不会丢失，缺损，错误。
* 长连接协议：可以持续不断的连接，就像开视频一样，可以持续连接，像发短信就是短连接，一个包一个包的发



Http server

![1567994922359](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1567994922359.png)

<center>http发送请求的报文

![1567996867426](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1567996867426.png)

<center>响应报文</center>
http/1.1 响应头协议  304  相应状态码    ok成功

服务端发送数据之前需要发送响应报文，否则服务器无法发送

![1567997431692](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1567997431692.png)

<center>打开可重用ip地址和端口</center>
![1567997787889](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1567997787889.png)

<center>get请求

![1567998168674](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1567998168674.png)

<center>取出请求内容

![1567998315872](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1567998315872.png)

<center>获取请求的URL</center>
![1567998745183](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1567998745183.png)

<center> 根据请求来做出不同的响应

![1567999633983](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1567999633983.png)

![1567999784588](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1567999784588.png)



<center>高逼格的占位符

## 简单的服务器搭建

~~~
import socket

sock = socket.socket(socket.AF-INET,socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sock.bind(('127.0.0.1',8000))
sock.listen(128)

temps=‘’‘
HTTP/1.1 200 OK

<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />

        <title>Seamile</title>

        <style>
            h1, p {
                text-align: center;
                font-size: 2.5em;
            }
            .avatar {
                border-radius: 20px;
                box-shadow: 5px 5px 20px grey;
                width: 500px;
                margin: 0 auto;
                display: block;
            }
        </style>
    </head>
    <body>
        <h1>Seamile</h1>
        <div><img class="avatar" src="https://inews.gtimg.com/newsapp_ls/0/10229330043_294195/0" /></div>
        <p>%s</p>
    </body>
</html>
’‘’

def recv_msg(msg):
    url=msg.split('/n')[0].split(' ')[1]
    return url


while True：
     msg_sock,addre=sock.accept()
     msg=msg_sock.recv(1024).decode('utf8')
     urls=recv_msg(msg)
     if urls='/go':
        html_tep=temps%'有点慌'
     elif urls='/bye':
        html_tep=temps%'小场面，不慌'
     else:
        html_tep='hello,welcome shenme shenme'
        
     msg_sock.send(html_tep.encode('utf8'))
     

~~~



WEB框架

**前端动态**

**后端动态**

![1568009605705](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568009605705.png)

Django   Flask  Tornado   Bottle   Web.py   Falcon  Quixote   Sanic

Django 牛逼  适合快速开发  内部耦合比较紧，

Flask  微型框架  极度低耦合，可以按照他的方向可以写很多扩展的东西

Tornado  优势 异步处理，事件驱动，性能最好的  底层用的是协程

bottle   适合初学者看，结构紧凑

web.py   是美国黑客写的  自从作者逝世后就停更了

Falcon    适合做api接口

Quixote   豆瓣使用的这个框架

sanic       16出现的玩意，性能很吊，但是稳定性，底层用的是uvloop



# Tornado 入门

-  /tɔː'neɪdəʊ/     09年被Facebook收购
- 实现了HTTP Server

安装tornado

~~~
pip install tornodo
~~~

查看tornaodo源代码

~~~
pip download tornado  直接下载
~~~

![1568020954047](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568020954047.png)

下载之后，就可以查看里面的内容，通过这个内容就可以看到里面有哪些东西

![1568021076472](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568021076472.png)





![1568011696160](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568011696160.png)



~~~
import tornado.ioloop   本身是异步的，ioloop核心的驱动ioloop，大多数程序都需要用到它
import tornado。web    跟web相关，请求、响应什么的都是在这里。跟web通信的相关都在这里

class MainHandLer( tornado.web.RequestHandler):     主要的首页处理器，继承的是requeshandler类，是一个首页请求处理器
    #首页请求处理器，如果想要处理那种方法，就用哪种方法，比如get、post等
   
    def get( self):                   #get对应的是http请求方法，get、post、put等等
        self. write( "Hello, world")  #如果处理post，就在下面在写一个def post（）
        #write就是给前端返回一个页面，可以是html页面，也可以是简单的东西
        
#产生一个web的运用，web框架就是为了将app跑起来
def make_app():
    return  tornado.web.Application([    #传进去的是一个列表
    (r"/", MainHandler) ,                #r，可以用正则表达式来匹配 '/'是个路由，就是http请求，用来处理MainHandlers请求类
    ])
    
if __name_ ==" __main__":
    app =make_app()
    app.listen(8888, '127. 0.0.1')       #对应的是sock.bind和sock.listen
    loop = tornado . ioloop . IoLoop . current()      #交给底层的ioloop去运行
    Loop. start()                        #是用来驱动协程

~~~

## tornado简单服务器流程

~~~
1.导入两个模块tornado.ioloop和tornado.web模块

2.页面请求类  class MainHandLer(tornado.web.RequestHandLer) 并继承所有的类请求

3.路由处理   是一个函数，通过这个函数来解决MaindHandLer里面的所有请求

4.主程序
   a.处理请求
   b.设置启动参数
   c.ioloop运行
   d.协程驱动
~~~







## 设置启动参数

~~~
外网绑定到0.0.0.0  mysql只能绑定到127.0.0.1内网内
localhost 对应的地址是127.0.0.1
~~~

~~~
from tornado.options import parse_command_line, define, options 
#options 选项
#parse_command_line 解析命令行的参数
#define  定义参数
#option 具体的参数

define("host", default='0.0.0.0', help="主机地址", type=str) 
  #定义主机ip  默认值   --help可以显示出来   type最终转换后的值类型

define("port", default=8888, help="主机端⼝", type=int) 
  #定义端口号

if __name__=='__main__':
    parse_command_line()      #把define定义的结果解析一遍

    print('你传⼊的 host: %s' % options.host)    #调用options的host参数
    print('你传⼊的 port: %s' % options.port)    #调用option的port参数

~~~



## 路由处理

![1568016052377](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568016052377.png)

url：统一资源定位符   

​         访问任何网页，里面内容都叫资源

http：//    baidu.com ：80    /foo/bar/xxx.html           ?q=Tornado&oq= Tornado&aqs= chrome      #top-fdsjl-ww

协议          资源地址      端口号     绝对路径                                  query string  查询字符串                         锚点

[https]                                              如果没有带包根目录               get请求                                                    网页的连接

[ftp]

[socks]

[redis]

[mysql]

~~~
class MainHandler(tornado.web.RequestHandler):      #首页请求或其他请求
    def get(self):
        self.write("Hello, world")


class AifeiHandler(tornado.web.RequestHandler):     #/foo请求
    def get(self):
        self.write("爱妃退下，朕在调戏代码")


class JiangPangpangHandler(tornado.web.RequestHandler):    #/bar请求
    def get(self):
        self.write("姜伟老师没醉过，但求一醉")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/foo", AifeiHandler),
        (r"/bar", JiangPangpangHandler)  #根据不同的请求调用不同的请求类处理
    ])
~~~







## 处理get和post请求

### get请求

![1568017190970](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568017190970.png)

![1568017207070](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568017207070.png)



### post请求



![1568018492619](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568018492619.png)



![1568019210689](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568019210689.png)

~~~
class TestPostHandler(tornado.web.RequestHandler):   #含有两个请求，get和post请求
    def get(self):
        html = '''
            <form action="/test/post" method="POST">   #get请求会返回一个页面
            姓名: <input type="text" name="name">
            <br>
            城市: <input type="text" name="city">
            <input type="submit">
            </form>
        '''
        self.write(html)

    def post(self):    #post请求返回一个字符串
        name = self.get_argument('name') 
        city = self.get_argument('city')
        self.write('%s 生活在 %s' % (name, city))

def make_app():
    return tornado.web.Application([
        (r"/test/get", TestGetHandler),
        (r"/test/post", TestPostHandler),    #在TestPostHandler中返回两个请求。
    ])

~~~





# 练习

1. 在 MySQL 中建⽴ user 表, 包含字段: id, name, age, sex, city 等, 并插⼊若⼲数据 
2.  开发接⼝，并根据⽤户传⼊的 id 显示对应的⽤户信息 
3. 开发接⼝，并根据⽤户传⼊的数值修改⽤户数据

~~~
import tornado.ioloop
import tornado.web
import pymysql

db=pymysql.connect(
    host='localhost',
    user='tyw',
    password='123',
    db='mystudent',
    charset='utf8'
)

#增删改查
def selects():
    cursors = db.cursor()
    selct="select * from `starstu`"
    cursors.execute(selct)
    resule = cursors.fetchall()
    print(resule)
    smm = ''
    for x in range(len(resule)):
        sam=''
        for y in range(len(resule[x])):
            sam += '<td>'+str(resule[x][y])+'</td>'
        smm += '<tr>'+sam+'</tr>'
    print(smm)
    return smm

def selecid(id):
    cursors = db.cursor()
    selct="select * from `starstu` where id=%s"
    cursors.execute(selct,(id,))
    resule = cursors.fetchall()
    print(resule)
    smm = ''
    for x in range(len(resule)):
        sam=''
        for y in range(len(resule[x])):
            sam += '<td>'+str(resule[x][y])+'</td>'
        smm += '<tr>'+sam+'</tr>'
    print(smm)
    return smm

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        select = selects()

        html='''
         <table border='1px' rules='all'>
             <tr>
                 <th>id</th>
                 <th>name</th>
                 <th>sex</th>
                 <th>city</th>
                 <th>description</th>
                 <th>birthday</th>
                 <th>only_chald</th>
             </tr>
             %s
         </table>
        ''' % select
        
        self.write(html)

class Selectzd(tornado.web.RequestHandler):
    def get(self):
        html='''
        <form action="/select" method="post">
           <p>选择您需要查询的字段：<input type="text" name="zd"><input type="submit"></p>
        </form>
        '''
        self.write(html)
        
    def post(self):
        id = self.get_argument('zd')
        selid = selecid(id)
        html = '''
             <table border='1px' rules='all' >
             <tr>
                 <th>id</th>
                 <th>name</th>
                 <th>sex</th>
                 <th>city</th>
                 <th>description</th>
                 <th>birthday</th>
                 <th>only_chald</th>
             </tr>
             %s
         </table>
        ''' % selid
        self.write(html)

def make_app():
    return tornado.web.Application([
        ('/',MainHandler),
        ('/select',Selectzd)
    ])

if __name__=="__main__":
    selecid(1)
    app=make_app()
    app.listen(8000,'127.0.0.1')
    loop=tornado.ioloop.IOLoop.current().start()
~~~



注：

1.从mysql中获取数据

2.用服务器传入网页

3.用表单进行数据的传输与发送

