# ORM对象关系映射

![1568079715132](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568079715132.png)

python类和SQL表一一对应。

通过对对象的增删改查来与控制sql

DJANGO-ORM   SQLAlchemy，Peenwee

Peenwee 日常使用，表达优美，代码简单等优势



## sqlalchemy  

![1568079928769](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568079928769.png)

十多年的历史，技术很成熟

原理：使用类的属性和方法来访问sql。

~~~
class Pysql(object):
   def __init__(self)
      self.id=''
      self.name=''
      ……
      
   def insert(self,*args):
       sql_template = 'insert into %s values (%……)'%(self.id,self.name……)
       pymysql...execute(sql)
   def delete()
       pass
   def update()
       pass
~~~

**就是用python类来封装mysql语句**



![1568083664981](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568083664981.png)



~~~
第一步：导入 连接数据库 模块
           与数据持续会话 模块
           需要创建的数据表字段信息 模块
           数据模型基类 模块
import datet ime
from sqlalchemy import create_engine   与数据库连接的引擎
from sqlalchemy.orm import sessionmaker   与数据库持续回话
from sqlalchemy import Column, String, Integer, Float, Date
#column 列   String等，需要使用的数据类型
from sqlalchemy.ext.declarative import declarative_ base   #创建数据模型的基类


第二步：建立跟mysql与数据库的连接
       实例化模型基类
       与数据库建立连接
engine = create_ engine ( ' mysql+pymysql//seamile: 54188@localhost:3306/ttt')
#这个字符串是url   mysql+pymysql是pymysql与mysql对接的协议。
#seamile: 54188  是用户名和密码
#localhost:3306  主机名和端口号
#/ttt            数据库名称

Base = declarative_ base( bind=engine) # 创建模型的基础类
#1.所有的模型都在base里面基础的类
Session = sessionmaker (bind=engine )   #这两步都需要绑定引擎，与数据连接
#创建会话类，需要产生一个实例


第三步：创建类本身对应的数据库的表结构
      实例化这个表
      并mysql建立会话
class User (Base):
'''类本身对应数据库里的表结构'''
    __tablename__ = 'user' # 该模型对应的表名，是sql什么的自己定义的

    id = Column(Integer, primary_ key=True) #定义 id字段 类属性
    #使用column创建一个列（字段field） 内容的数据类和相关描述 

    name = Column(String(20)， unique=True) # 定义姓名字段 类属性

    birthday = Column(Date) 
    #定义生日字段

    money = Column(Float, default=0.0)
    #定义金钱字段

Base.metadata.create_ all (checkfirst=True) #创建表
#metadata 元数据，就是表的基本信息，把__tablename__的表创建出来

session = session()  
#定义与数据库的会话，表示与数据库持续连接，可以通过这个连接来与数据库进行数据交换



第五步：增删改查
#创建一堆的结构，定义的每一个对象，对应数据库的一行数据
bob = User (name= bob'，birthday=datet ime .date(1990，3, 21)，money=234)

tom = User (name='tom', birthday=datetime . date(1995， 9，12))

lucy = User(name='lucy' ，birthday-datetime. date(1998，5, 14)，money=300)

ella = User (name='ella', birthday=datetime . date(1999，5, 26)， money=394)


#增加数据，把bob，tom，lucy这个实例对象传给数据库
session.add_all([bob,tom,lucy,jam])       #add表示添加一条，add_all 添加多条 
session.commit()                          # 提交到数据库中，在数据表中添加数据,每做一次增删改查都需要提交一次

# 删除数据 
session.delete(jam)    # 删除jam操作  delete后面跟着的是where后面的条件
session.commit()       # 提交到数据库中执⾏

#改数据
bob.money = '100'      #改数据只要改变类属性值就可以
session.commit()       #提交到数据库

#查询数据
q = session.query(User)
q.filter(User.id==5)     #指明对象，查询id=5的值
q.fiter_by(id=1)         #与filter的区别就是条件不同，取到的都是一个查询对象

#判断结果是否存在
result = q.filter_by(name='tyw').exists()  
session.query（result）.scalar()          #返回值为True或者False


result = q.filter(User.id==5).first（）    #查询的第一条记录的结果
result.name，result。birthday              #查询多个字段

result.all()         #查询所有满足条件的结果  返回值是一个列表
result.first()        #查询第一条
result.one()         #查询第一条，与上一条一样

result.q.filter(User.id>5).order_by('birthday')    #按照birthday进行排序
result.q.linit(3).offset(4)                        #跳过前4个，向下取3个

#既更新又查询
q.filter(User.id==1).update({'birthday':'1994-12-11'},synchronize_session=False)
#synchroize_session  是否同步更新，一般为false
session.commit()           #提交数据

#计数
q.filter(User.id==5).count（）


~~~

ORM 一般是懒加载查询模式 |惰性加载  ——>惰性求值。

迭代器和生成器就是这样的，需要的时候，才会计算值。

![1568095326116](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568095326116.png)

这一步的时候，ORM只是在拼接query，他得到的只是一个query对象，并没有访问sql，

只有在用的时候，才会去访问数据库并取出数据

![1568095487982](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568095487982.png)





### 查询数据

![1568086233789](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568086233789.png)





### 查询结果的操作

![img](file:///C:\Users\ASUS\AppData\Roaming\Tencent\Users\455224995\QQ\WinTemp\RichOle\WW{H$Q$G65[{3GLT}{Y`BIE.png)









# tornado模板

jinjia2 网页模板，跟Django模板差不多

模板里有自己的语法，什么for循环的~

## 模板配置：

~~~
app = Application( 
    templates_path = 'templates',    # 模版路径 
    static_path = 'statics'          # 静态⽂件路径
)

或
tornado.web.Application(路由，模板路径 template_path='',静态文件 static_path='')

需要两个文件夹，在文件夹里分别放模板文件（html） 静态文件（图片、视频、音频）。
如果该文件夹下嵌套的文件夹过多，需要用绝对路径来

#查看当前文件的绝对路径
print（os.path.abspath(__file__)  
#查看项目工程文件的绝对路径文件夹
base_dir = os.path.dirname(os.path.abspath(__file__))
通过base_dir就可以取到项目文件的绝对路径，再通过这个文件夹来查找该文件


#获取模板目录和静态文件目录的绝对路径
base_ dir= Os.path.dirname( Os.path abspath(_ _file__)
template_ dir = os.path.join(base_ dir, 'templates' )
static_ dir= os.path.join(base_ dir,'statics')

return tornado.web.Application( routes ,
    template_path='tempLates'
    static_path='statics' 
)


所以根据请求作出的方法该这样做
class Ai feiHandler tornado. web. Reques tHandLer:
    def get(self):
    	self.render（’xxx.html‘）    ——>会到模板路径里查找xxx.html文件并返回到浏览器页面中
                                    ——>render  渲染的意思，是由这个函数来讲网页发送出去
    def get（self）
        self.render（'xxx.html',data='你好'）   ——>如果传参的话，在路径后面加参数数据
        
    def get（self）:
        abc = self.get_argument('arg')
        self.render('xxx.html',data=abc)        ——>获取url的参数，再由参数传给页面中的变量
        
        self.redirect(‘要跳转的页面’)             ——>重定向，页面跳转
   以上对应 1.传递参数
   ————————————————————————————————————————————————————————————————————————————————
   
~~~



### xxx.html模板的动态数据

~~~
1.传递参数
<body>
    <h1 style=" text-align: center; "> Seamile</h1>
    <p>{{ data}}</p>                  #用两个大括号，作为参数（变量）
</body>

2.{{}} 内加表达式，须为python的表达式
<body>
    <div>猜一猜，3 x 2等于几? </div>
    <div>我就不告诉你等于{{ 3*2 }}</div>
    <div>我就不告诉你等于{{[x for x in range(10)]}}</div>
</body>
~~~



## if……else……语句

需要用%……%来包裹以{% end %} 结尾

~~~
class MainHandLer( tornado. web. Reques tHandler): 
    def get(self:
    	sex = self. get_ argument( ’name'，‘adim’ )
        sex = self. get_ argument( ’sex'，‘保密’ )      ——>后面给一个值，表示默认值
                                         #如果ulr中没有这个参数，则给一个默认值
        self. render('index.html',name=name，sex=sex)    

~~~

页面模板

~~~
<body>	
    {% if sex = '男' %}
         <div>你好{{name}}，欢迎回来，先生！ </div>
    {% if sex = '女' %}
         <div>你好{{name}}，欢迎回来，女士！ </div>
    {% if sex = '保密' %}
         <div>你好{{name}}，欢迎回来，大哥！ </div>
    {% end %}
</body>	
~~~



## for循环

也是需要用{% …… %}来扩起来 以{% end %}结尾

~~~
class MainHandLer( tornado. web. Reques tHandler): 
    def get(self):
    	sex = self. get_ argument( ’name'，‘adim’ )
        sex = self. get_ argument( ’sex'，‘保密’ )      ——>后面的值是默认值
        menu=[‘红烧肉’，‘水果沙拉’，‘糖醋排骨’。‘牛排’，’波土顿龙虾‘，’三文鱼刺身‘]
        self. render('index.html',menu)               ——>传递一个列表
~~~



网页模板

~~~
<body>	
    本店菜单：
    <ol>
   		{% for item in menu%}
        <li> {{item}}</li>
        {% end %}
    </ol>
</body>	
~~~



# for循环和if条件判断整合版

**python代码**

~~~
import tornado.ioloop
import tornado.web

class MainHandLer(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument('name')   #这是get请求，在浏览器上需要输入参数
        print(name)
        menu = ['红烧肉','水果沙拉','糖醋排骨','牛排','波土顿龙虾','三文鱼刺身']
        self.render('index.html',name=name,menu =menu)    #传入的是变量，不需要用引号

def make_app():
    rose = [(r"/", MainHandLer), (r"/name", MainHandLer)]   
    return tornado.web.Application(rose,
                                   template_path ='temples',   #html模板文件夹是template_path
                                   static_path='statics',      #静态文件夹static_path
                                   )

if __name__ == "__main__":
    app = make_app()
    app.listen(8000,'127.0.0.1') 
    loop = tornado.ioloop.IOLoop.current() 
    loop.start()
~~~



**html代码**

~~~
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
      <ol>
          {% for item in menu %}       #for循环与python一样，就是需要{% for循环 %}
           <li>{{item}}</li>           #变量需要用两个大括号{{}}
          {% end %}
      </ol>
      <img src="/static/0.jpg" alt="没找到">      #图片文件是静态文件，格式必须要以static开头
      <div>
          {% if name=='tom' %}
          <p>欢迎光临</p>
          {% elif name=='tonny' %}
          <p>你好！再见！</p>
          {% else %}
          <p>再您妈的见</p>
          {% end %}             #if语句必须是if……elif……else……end
      </div>
</body>
</html>
~~~



# 模板的继承

**1.先写好一个基础模板**

* 把整体页面的布局捣腾出来
* 





![1568100777602](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568100777602.png)

![1568100871284](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568100871284.png)



![1568100916100](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568100916100.png)

~~~
<style>
    body{
       width:900px;
       margin:0 auto;   #居中
    }
    
    .content{
       float:left;
       width:700px;
    }
    
    .sidebar{
        float:left;
        width:200px
    }
</style>

#导航区域
<div class='navbar'>导航栏</div>
     <a href='#'>要闻</a>
     <a href='#'>财经</a>
     <a href='#'>体育</a>
     <a href='#'>娱乐</a>
     <a href='#'>时尚</a>
     
#内容区域
<h1>春啥<h1>
<p>ssssssssssss<br/>
sssssssssss<br/>
sssssssssss<br>
sssssssssss</p>
<hr/>
<p></p>
<div class='content'>
   {% block container%}这里可以填入内容，是默认内容{% end %}     #重点在这里，把这个区域扣出来。
   #声明在这个区域要放入动态数据  再创建一个扣出来的区域子模板 见一下个html
   #block 是模板关键字  container可以自己改
</div>

#边栏区域
<div class='sidebar'>
	<ul>
        <1i/>
        <a>科点性身系罩长业雖甲亚郜司 鞋话身“新發申雄Y早三印要</a>
        </li>
        <1i/>
        <a>科点性身系罩长业雖甲亚郜司 鞋话身“新發申雄Y早三印要</a>
        </li>
        <1i/>
        <a>科点性身系罩长业雖甲亚郜司 鞋话身“新發申雄Y早三印要</a>
        </li>
        <1i/>
        <a>科点性身系罩长业雖甲亚郜司 鞋话身“新發申雄Y早三印要</a>
        </li>
	</ul>
</div>
~~~



**2.子模板数据**

~~~
{% extends '上一个模板的名字' %}                #继承畅易阁模板  extends 不可以变是关键字

#再找到上个扣出来的区域，block是关键字，不可变
{% block container %}   #名字要和上一个html一样
<h1>{{title}} </h1>     #向程序获取数据
<p>{{ content }}</p>    #向程序获取数据
{% end %}               
~~~



**3.python**

~~~
class BLockHandlerc tornado. web. Reques tHandler):
    def get(self）:
        title = self. get_ argument('title',‘什么东西’)
        content = self. get_argument(‘content’，‘哦豁’）
        self. render( '子模板名’ .title=title，content=‘content’ )
~~~





## 静态文件

转成静态文件时，需要把图片或者其他转换成网址

所有的图片url前缀都必须是static开始，静态文件

![1568103909786](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568103909786.png)

![1568104223438](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568104223438.png)





~~~

~~~

