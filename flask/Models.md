

# Models

是数据交互封装，sqlalchamy

Flask默认没有提供任何数据库的API

Flask中可以自己的选择数据，用原生语句实现功能

* 原生SQL缺点:
  * 代码利用率低，条件复杂代码语句越过长，有很多相似语句
  * 一些SQL是在业务逻辑中拼出来的，修改需要了解业务逻辑
  * 直接写SQL容易忽视SQL问题

用ORM来操作数据库：对象关系映射，表和类对应关系

Flask没有orm所以用sqlAlchemy

**优点**

* 易用性，可以有效减少重复SQ
* 性能损耗少
*  设计灵活，可以轻松实现复杂查询
* 移植性好



一、基本配置

~~~
1.安装
   pip install flask-sqlalchemy
   
2.创建sqlalchemy对象
  db=sqlalchemy(app=app)  -->一般用下面一种方法
  db=SQLAlchemy()         -->在medols中写
  db.init_app(app=app)    -->在inti中写
  
3. 配置
app.config[SQLALCHEMY_DATABASE_URI]='mysql+pymysql://root:123@localhost:3306/mypthon'
   1.能把模型类变成一个表
   2.能对模型做增删改查
   
   init中写 SQLALCHEMY_DATABASE_URI
   #dialect+driver://username:password@host:port/database
   #dialect 方言/语言  driver 驱动
   
4.创建表模型

~~~



​    models.html

~~~
from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()

class Animal(db.Model):
#必须设置主键ID，必须给字段添加长度
    id=db.Column(db.Integer,primary_key=True,auto_increment=True)
	name = db.Column(db.String(32))
	color=db.Column(db.String(32))
	
	__tablename__='animal'     --->在模型创建的时候，可以指定表名，
	                               如果没有表名，则跟模型名一样
~~~

![sqlalchemy报错问题](D:\Flask\writeRecord\img\sqlalchemy报错问题.png)

## 启动mysql数据库

~~~
service mysqld start|stop|restart|reload|status
sudo mysql -h localhost -p3306 -u root -p123
~~~

views.py

~~~
通过模型创建表
@blue.route('/table/')
def create_table():
     db.create_all()     -->创建表
    return '创建成功'
~~~



增删改查

~~~
通过模型删除表
@blue.route('/dropTable/')
def drop_table():
     db.drop_all()    -->删除表
    return '删除表'
    

通过模型添加数据
@blue.route('/addanimal/')
def addnimal():
     a=Animal()
     a.name='hen'
     a.color='yellow'
     db.session.add(a)     -->在表中添加数据
     db.session.commit()   -->数据提交到表中
    return '添加成功'
    
    
通过模型查找数据库的所有数据
@blue.route('/findall/')
def findall():
    animal_list=Animal.query.all()
    
    for animal in animal_list:
        print(animal)
    return '查询成功'
~~~



## 数据库环境

~~~
开发环境    假数据                     develop
测试环境    数据量大一些 假数据          test
演示环境    接近线上环境   实施工程师     show
线上环境    真实数据                   product
~~~





### 作业

![1568883664629](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568883664629.png)



## 项目拆分

```
.
├── App
│   ├── ENV_SH.py    #封装sql配置文件
│   ├── ext_init.py  #封装server配置文件
│   ├── __init__.py  #初始化文件
│   ├── models.py    #模型层
└── migrations       #模型迁移文件夹，执行init产生
|    ├── alembic.ini
|    ├── env.py
|    ├── __pycache__
|    │   └── env.cpython-36.pyc
|    ├── README
|    ├── script.py.mako
|    └── versions    #模型迁移文件夹，执行migrate产生
|        ├── 173a195965c3_.py      #模型迁移文件，执行upgrade产生
|        └── __pycache__
|            └── 173a195965c3_.cpython-36.pyc
│   ├── static         #静态文件
│   ├── templates      #动态文件
│   │   └── login.html
│   └── views.py       #视图层文件
└── manager.py         #主程序文件
```

**项目拆分就是将每个程序拆分成最基本的执行单元。然后通过调用来组合到manager主执行文件中**

### 项目拆分图解

![Flask项目拆分](D:\Flask\writeRecord\img2\Flask项目拆分.png)



### manager.py

~~~
from flask_migrate import MigrateCommand    #导入flask下的模型迁移文件
from flask_script import Manager            #导入manager控制程序启动模块
from App import app_start                   #导入封装的启动配置文件
from App.views import blue                  #导入蓝图

app=app_start('test')                       #调用启动函数，并传入一个数据库环境名
manager = Manager(app=app)                  #初始化启动方法
app.register_blueprint(blueprint=blue)      #注册蓝图
manager.add_command('db',MigrateCommand)    #模型迁移设置开启状态

if __name__ == '__main__':
    manager.run()                           #启动manager主程序
~~~



### __init\_\_.py

~~~
from flask import Flask            #导入flask包
from App import ENV_SH             #导入配置数据库文件
from App.ext_init import ext_all   #导入配置文件ext_all


def app_start(env):                #含有flask对象及启动环境配置的函数
    app = Flask(__name__)          #创建flask对象
    app.config.from_object(ENV_SH.ENV_NAME.get(env))   #调用数据库环境配置文件
    ext_all(app)                   #调用ext启动配置，这一项和上一项位置不可逆
    return app
~~~



### ext_init.py

~~~
#所有的第三方扩展库放在这里

from flask_migrate import Migrate      #导入数据迁移包
from App.models import db              #导入已经创建好的数据库

def ext_all(app):
    app.config('SECRET_KEY') = '112'       #配置秘钥什么的
    app.config('SESSION_TYPE')='redis'     #配置session的存放位置
    app.config('SESSION_KEY_PREFIX')='TYW' #配置前缀，存放位置可以见到
    Session(app=app)                       #初始化session对象

    db.init_app(app=app)               #数据库配置
    
    migrate=Migrate()                  #创建模型迁移
    migrate.init_app(app=app,db=db)    #模型迁移初始化
~~~



### ENV_SH.py

~~~
数据库配置文件

class Config():           #数据库初始化配置文件
    Test = False
    Debug = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def SQLALCHEMY_DATABASE_URI(DATABASE):            #数据库配置，进入数据的方法
    dialect=DATABASE.get('dialect')
    driver=DATABASE.get('driver')
    username = DATABASE.get('username')
    password = DATABASE.get('password')
    host = DATABASE.get('host')
    port = DATABASE.get('port')
    database = DATABASE.get('database')
    return '{}+{}://{}:{}@{}:{}/{}'.format(dialect,driver,username,password,host,port,database)

class DevelopConfig(Config):             #配置开发环境
    DATABASE={
        'dialect':'mysql',
        'driver':'pymysql',
        'username':'tyw',
        'password':'123',
        'host':'localhost',
        'port':'3306',
        'database':'mypython'
    }
    SQLALCHEMY_DATABASE_URI=SQLALCHEMY_DATABASE_URI(DATABASE)  


class TestConfig(Config):                 #配置测试环境
    DATABASE = {
        'dialect': 'mysql',
        'driver': 'pymysql',
        'username': 'tyw',
        'password': '123',
        'host': 'localhost',
        'port': '3306',
        'database': 'mypython'
    }
    SQLALCHEMY_DATABASE_URI=SQLALCHEMY_DATABASE_URI(DATABASE)


class ShowConfig(Config):              #配置演示环境
    DATABASE = {
        'dialect': 'mysql',
        'driver': 'pymysql',
        'username': 'tyw',
        'password': '123',
        'host': 'localhost',
        'port': '3306',
        'database': 'mypython'
    }
    SQLALCHEMY_DATABASE_URI= SQLALCHEMY_DATABASE_URI(DATABASE)


class ProductConfig(Config):           #配置线上环境
    DATABASE = {
        'dialect': 'mysql',
        'driver': 'pymysql',
        'username': 'tyw',
        'password': '123',
        'host': 'localhost',
        'port': '3306',
        'database': 'mypython'
    }
    SQLALCHEMY_DATABASE_URI=SQLALCHEMY_DATABASE_URI(DATABASE)

ENV_NAME={
    'develop':DevelopConfig,
    'test':TestConfig,
    'show':ShowConfig,
    'product':ProductConfig,
}                                  #封装整个配置数据库环境
~~~



### Models.py

~~~
from flask_sqlalchemy import SQLAlchemy    #导入数据库

db=SQLAlchemy()    #创建数据库对象
 

class StaffInfo(db.Model):          #创建数据库模型
    __tablename__='staffinfo'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(20))
    gendar=db.Column(db.String(10))
    age=db.Column(db.Integer)

~~~



### views.py

~~~
from flask import Blueprint             #导入蓝图
from App.models import db, StaffInfo    #导入数据库模型和数据库对象

blue = Blueprint('blue',__name__)       #蓝图初始化

@blue.route('/')                        #路由路径
def hello_world():
    db.create_all()
    return 'Hello World!'

@blue.route('/addstaff/')
def addstaff():
    staff=StaffInfo()
    staff.name='tom'
    staff.gendar='male'
    staff.age='26'
    db.session.add(staff)
    db.session.commit()
    return '添加成功'

@blue.route('/delstaff/')
def delstaff():
    staff=StaffInfo.query.filter(StaffInfo.id==4).first()
    print(type(staff))
    print(staff.name)
    # db.session.delete(staff)
    # db.session.commit()
    return '删除成功'

@blue.route('/upstaff/')
def upstaff():
    staff=StaffInfo.query.filter(StaffInfo.name=='Bernice').one()
    staff.name='Benchi'
    db.session.commit()
    return '修改成功'
~~~



### 动态html

~~~
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<style>
    {% block css %}
    body{
        width: 800px;
        height: 300px;
        margin: auto;
    }
    #header{
        width:800px;
        height: 50px;
        background-color: #146f05;
    }

    #foot{
        width:800px;
        height: 50px;
        background-color: #47ce48;
    }
    table,tr,th,td {
        border: 1px solid black;
        border-collapse: collapse;
    }
    table{
        width: 800px;
    }
    input{
        width: auto;
    }
    {% endblock %}
</style>
<body>
{% block header %}
<div id="header"></div>
{% endblock %}
{% block content %}
<div>
    <form action="/login/" method="post">
    <table>
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Grendar</th>
            <th>Age</th>
            <th>提交</th>
        </tr>
            {% for info in staffinfo %}
                <tr>
                  <td>{{ info.ID }}</td>
                  <td>{{ info.Name }}</td>
                  <td>{{ info.Gendar }}</td>
                  <td>{{ info.Age }}</td>
                    <td> <a class="deldata" href="#" >删除</a>
                        <a class="updata" href="#"  >修改</a> </td>>
                </tr>
            {% endfor %}
    </table>

</form>
</div>
<hr style="height: 30px;margin: 0px">
<div id="content">
    <form action="/adddata/" method="post">
        <table>
            <tr>
                <th>Name</th>
                <th>Gendar</th>
                <th>Age</th>
                <th>提交</th>
            </tr>
            <tr>
                <td><input type="text" name="Name"></td>
                <td><input type="text" name="Gendar"></td>
                <td><input type="text" name="Age"></td>
                <td><input type="submit" value="添加数据"></td>
            </tr>
        </table>

    </form>
</div>
{% endblock %}
{% block foot %}
   <div id="foot"></div>
{% endblock %}
</body>
    <script src="../static/jquery-1.8.3.min.js"></script>
    <script>
			$(function(){
				$('.updata').click(function(){
					var ams= $(this).parent().siblings().first().text();
					$(this).attr('href','/update/?id='+ams);
				});
                $('.deldata').click(function(){
					var ams= $(this).parent().siblings().first().text();
					$(this).attr('href','/deldata/?id='+ams);
				})
			})
    </script>
</html>
~~~







# 模型迁移

~~~
pip install flask-migrate
模型变成表，就叫模型迁移


创建migrate
migrate=Migrate()                   -->创建
 migrate=init_app(app=app,db=db)    -->初始化
                                    -->ext.py
 
第三步：
结合flask-script来
    manager.add_command('dbsss',MigrateCommand)   -->连接到启动项 
                                                  -->manager.py
 
使用
class EMP（db.Model）:
    pass                      -->medols.py


① python mangager.py dbss  init      -->生成一个MIGRATEIONS (第一步)，
② python mangager.py dbss  migrate   -->生成一个py迁移文件 （第二步）
③ python mangager.py dbss  upgrade   -->生成一个EMP表   （第三步）
④ python mangager.py dbss  dowgrade  -->撤销刚刚生成的表 （第四步）
              
a.如果没有如果之前migrations文件夹，必须init,如果没有，就不需要init
b.第二步生成文件，在init生成文件夹之后：
 （1）模型定义完成从未调用无法生成迁移文件   -->模型定义已经完成，但是没有调用，就会提示无法操作
 （2）数据库已经有模型记录无法生成迁移文件,指的是之前已经创建过的表，尽量要在创建之前创建。
 解决办法，删除库里所有表，所有init生成的迁移文件，重新开始。
 
c.第二步中插入一个条命令
   python manager.py dbss migrate --message '创建一个表'
   #使生成的py文件名后面有个备注
   
 
~~~

![migate执行init](D:\Flask\writeRecord\img\migate执行init.png)

![migrate生成一个迁移文件](D:\Flask\writeRecord\img\migrate生成一个迁移文件.png)

![upgrate创建一个表](D:\Flask\writeRecord\img\upgrate创建一个表.png)



![down撤回一个表](D:\Flask\writeRecord\img\down撤回一个表.png)



### 第二次init

![二次init](D:\Flask\writeRecord\img\二次init.png)

![1568980081470](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568980081470.png)

![第三次删除操作](D:\Flask\writeRecord\img\第三次删除操作.png)





# DML

**DDL ：数据定义语言，针对表操作，create  alter drop**

**DML：数据操纵语言，针对数据操作   insert  delete  update**

**DQL：数据查询语言，select**

**TCL：事务    commit  rollback** 

~~~
增
方法命名规则：动作+模块  addstudent
db.session.add(s)  -->添加一个
db.session.add_all(list())   -->添加多个，多个放在列表中

删 -->建立在查询的基础之上
s=表名.query.first()
db.session.delete(s)
db.session,commit()    -->先删除后提交

改 -->建立在查询之上
s = 表名.query.first()
s.name='ls'         -->这里修改
db.session.add(s)   -->直接保存即可
db.session.commit

~~~

~~~
增例题

添加一条：
@blue.route('/addstaff/')
def addstaff():
    staff=StaffInfo()
    staff.name='tom'
    staff.gendar='male'
    staff.age='26'
    db.session.add(staff)
    db.session.commit()
    return '添加成功'
    
添加多条：
@blue.route('/addmany/')
def addmany():

    a=StaffInfo(name='Artemis',gendar='male',age=23)
    b=StaffInfo(name='Chloe',gendar='famale',age=21)
    c=StaffInfo(name='Flora',gendar='male',age=23)
    d=StaffInfo(name='Hazel',gendar='famale',age=22)
    e=StaffInfo(name='Bernice',gendar='male',age=20)
    db.session.add_all([a,b,c,d,e])
    db.session.commit()
    return '群体添加成功'
~~~

~~~
删案例
@blue.route('/delstaff/')
def delstaff():
    staff=StaffInfo.query.filter_by(id=3).first()
    print(type(staff))
    print(staff.name)
    db.session.delete(staff)
    db.session.commit()
    return '删除成功'
~~~

~~~
改案列
@blue.route('/upstaff/')
def upstaff():
    staff=StaffInfo.query.filter(StaffInfo.name=='Bernice').one()
    staff.name='Benchi'
    db.session.commit()
    return '修改成功'
~~~





# 查

~~~
1.获取单个数据
  @blue.route('/getone/')
  def getone():
      s=表名.query.first()     -->查询第一个
      print（tpye(s)）         --><class app.models.Student>
      
      s1=表名.query.get(2)     
      print（type（s1））       -->和上面一样，返回的数据类型是一个模型类
      
      
      return '查询成功'
      
2.获取结果集
 (1)xxx.query.all            -->返回的是一个列表
 (2)xxx.query.filter_by      -->返回一个是BaseQuery
              filter_by后面加查询条件。tornado返回的是一个是query，django返回的是queryset
              
 (3)xxx.query.filter         -->返回是BaseQuery
    xxx.query.filter(xxx.name.startwith('小'))     以小字开头的人
    xxx.query.filter(xxx.name.contains('小'))      包含小字
    xxx.query.filter(xxx.age.in([1,2,3]))          是否在一个列表中
    



filter_by 和 filter区别
     filter_by和filter对主键的查询是相同的。id = 0 / id==0
     非主键时
           a.filter的条件必须要 表名.字段名 == 值
           b.filter_by的条件必须要  字段名=值
           
 条件查找
    字段.__ge__(值)  大于
    字段.__lt__(值)  小于
           
           
~~~





### 数据筛选

~~~
(1)排序order_by
   xxx.query.order_by('age')    -->按照年龄进行（升序排序）排序
   xxx.query.order_by(db.desc(xxx.age))   -->降序排序
   

(2)分页问题limit
   xxx.query.limit(3)     -->取前三条
   
   xxx.query.offset(3)    -->偏移3条数据
   
   limit是取前n个数据
   offset是去除前n个数据
   
 注：limit和offset无论谁先写，都是offset先写
 
 
 ****************************************
 先分页再排序   order_by无论是语法还是执行顺序都是先执行 
 xxx.query.limit(2).offset(2).order_by('age')  -->必须先排序再分页
 xxx.query.order_by('age').limit(2).offset(2)
 
 
~~~



## 查询的逻辑运算

~~~
from sqlalchemy import ande

@blue.route('/getLogic/')
def getLogic():
   student = Student.ruery.filter(and_(Student.id==1,Student.name=='安其拉'))
--->与运算   返回的是Basequery
   
   student = Student.ruery.filter(or_(Student.id==1,Student.name=='李白'))
 --->或运算   返回的是Basequery 
   
   student = Student.ruery.filter(not_(Student.id==3))
--->非运算   要导入sqlalchemy的包
   
   student = Student.ruery.filter(Student.id,in_([1,2,3,4,5]))
   for s in Student:
      print(s.name)
--->in运算   表示存在

   return '查找成功'

python默认是短路运算，其他语言的…&& 或 ||

~~~



# 数据定义

## 字段类型

Integer    整型

String      字符串   长度最好是2的倍数

Date        日期

Boolena   布尔



## 约束

primary_key     主键

autoincrment   自增长

unique               唯一

default               默认值

index                  索引

not null              非空

ForeignKey        外键

~~~
外键约束问题
db.Column(db.Integer,db.ForeignKey(主表.id))

主表使用 relationship方法 实现级联数据获取
       -‘table’       第一个参数声明级联的数据库
       -backref=‘table’    实现反向获取数据
       -lazy=True          实现懒加载
~~~



# 模型关系

## 一对多

**查询效率    select  >  子查询  >    级联查询**

## relationship用法

~~~
class  A（）：
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(30),unique=True)
    b_table=db.relationship('B',backref='PARENT',lazy=True)
    
class  B（）：
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(30),unique=True)
    A_id=db.Column(db.Integer,db.ForeignKey('a.id'))

relationship    
      用来关联外键的表。
      -backref 参数
           在parent类上声明新属性的简单方法，之后可以在子表来获取这个对像
           
      -lazy 参数
           -select 默认值
                   sqlalchemy使用select语句
           -joined  
                   使用外连接和内连接的
           -subquery
                   使用子查询，嵌套查询
           -dynamic
                   懒加载，返回一个查询对象，需要时候再调用
    
    懒加载
       默认情况下，使用user.query.get（）中的get方法时，就发送了sql语句
       
       如果我们使用了dynamic，就代表是用懒加载，或者叫做延迟加载
       在不适用对象的属性或者方法的时候就不发送sql语句
                   
       user.query.all()    默认的情况下也会发送sql语句
       如果使用dynamic，就可以在遍历的时候发送sql
       
       什么时候发送sql语句？
       1.在遍历的时候，2.在使用其属性的时候
       

~~~



添加数据

~~~
class  A()：
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(30),unique=True)
    b_table=db.relationship('B',backref='a',lazy=True)
    
class  B()：
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(30),unique=True)
    a_id=db.Column(db.Integer,db.ForeignKey('a.id'))

表A是主表，表B是从表

@blue.route('/adddata/')
def adddata():
   a = A()
   a.name = '张三'      #创建主表数据a
   
   b = B()
   b.name = '张小凡'     #创建从表数据b
   c = B（）
   c.name='张大帅'       #创建从表数据c
   
   b_list=[b,c]         #把这两条数据全都放到一个列表中
   a.b_table = b_list   #把从表的两条数据放进a表的b_table的属性中去
   
   db.session.add(a)    #添加a表数据
   db.session.commit()  #提交
   
   return  '添加成功'
~~~

![Flask数据一对多添加数据](D:\Flask\writeRecord\img2\Flask数据一对多添加数据.png)



## 主从查询

**主查从和从查主主要是相对于查询条件来说的**

### 主查从

~~~
class  A()：
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    address=db.Column(db.String(30),unique=True)
    b_table=db.relationship('B',backref='a',lazy=True)
    
class  B()：
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(30),unique=True)
    a_id=db.Column(db.Integer,db.ForeignKey('a.id'))
    
主查从    给一个主表 然后查找子表的数据

@blue.route('/getb/')
def getb():
    b = A.query.filter(id ==1)[0]    #a.id -->db.ForeignKey('a.id')就是外键
    c=b.b_table                      #通过b_table来查找子表数据
    for i in c；
      print(i,name)
    return '查找成功'


~~~

**主查从时， b_table=db.relationship('B',backref='PARENT',lazy=True)中的backref可有可无**

![Flask一对多通过主表主键查询子表](D:\Flask\writeRecord\img2\Flask一对多通过主表主键查询子表.png)



### 从查主

~~~
从查主  给一个子表，查询主表数据
class  A()：
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    address=db.Column(db.String(30),unique=True)
    b_table=db.relationship('B',backref='a_biao',lazy=True)
    
class  B()：
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(30),unique=True)
    a_id=db.Column(db.Integer,db.ForeignKey('a.id'))

@blue.route('/getParent/')
def getParent():
    b = B.query.filter(B.id==4)[0]    #先查从表的数据
    print(b.a_biao.address)           #根据从表反查主表数据
    return  ‘好的’
~~~

![Flask一对多从表查主表](D:\Flask\writeRecord\img2\Flask一对多从表查主表.png)



## relationship参数区别

~~~
class  A()：
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    address=db.Column(db.String(30),unique=True)
    b_table=db.relationship('B',backref='a',lazy=True)
    
class  B()：
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(30),unique=True)
    a_id=db.Column(db.Integer,db.ForeignKey('a.id'))



没有relathionship的主查从A表查B表
@blue.route('/norela/')
def norela():
   a = A.query.filter(A.id==1)[0]
   b=B.query.filter(B.a_id == a.id)
   ——>base类型，这里简写
   print（b.name）
   return '查询成功'
   
   
有relathionship和从表B参数查找A
@blue.route('/havela/')
def noref():
   b = B.query.filter(B.id==1)[0]
   a = A.query.fliter(b.id==a_id)[0]
   print(A.address)
~~~

![Flask的relationship用法](D:\Flask\writeRecord\img2\Flask的relationship用法.png)



## 一对一

* uselist = Fale 是在模型执行的时候，会验证从表中是否有重复的数据，跟一对多都差不多,效率不行

![Flask一对一关系](D:\Flask\writeRecord\img2\Flask一对一关系.png)





## 多对多关系

~~~
 class User(db.Model):   #用户表
         id = db.Column(db.Integer,primary_key=True,autoincrement=True)
         name = db.Column(db.String(32))
         age = db.Column(db.Integer,default=18)

class Movie(db.Model):   #电影表
        id = db.Column(db.Integer,primary_key=True,autoincrement=True)
        name = db.Column(db.String(32))

多对多会维护第三张表  订单表
第三张表应该有个id，并有两个外键分别与user和movie关联，还有一个数量
用户和电影联合为一，用户不唯一，电影不唯一。
class Collection(db.Model):   #订单表
        id = db.Column(db.Integer,primary_key=True,autoincrement=True)
        num=db.Column(db.Integer,deful=1)
        u_id = db.Column(db.Integer,db.ForeignKey(User.id))   
        m_id = db.Column(db.Integer,db.ForeignKey(Movie.id))
        #因为没有一对多的relationship，所以这里的外键引用就是原表的id，而不能不传字符串
~~~



~~~s
多对多，第一次插入到数据库，第二次会在原来的基础之后数据加1

@blue.route('/addcollection/')
def addCollection()
    #接收用户id和商品id   即购买者id，电影id
    u_id = int(request.args.get('u_id'))
    m_id = int(request.args('m_id'))
    #查询表中的数据是否有u_id和m_id
    collections=collection.query.filter(collection.u_id).filter(collection.m_id=m_id)
    链式查询：
    
    #如果有，就修改，没有就删除。
    #不能直接用collection是一个Besaquery对象，无论有没有都是True
    #所以count()  获取basequery的元素长度。 如果大于零，表示有，
    if collection.count() > 0:
        collection = collections[0]         #给查询到的BasQuery的对象取成一个数据对象
        collection.num =collection.num +1   #这种方法比+=效率高
     else：
        collection = Collection()           #实例化一个订单对象
        collection.u_id = u_id
        collection.m_id = m_id              #并将订单id和电影id赋给订单对象
        
    db.session.add(collection)
    db.session.commit()
   
    return  '购物车添加成功'
~~~

应用场景：

![Flask多对多关系的订单](D:\Flask\writeRecord\img2\Flask多对多关系的订单.jpg)

![Flask多对多的模型](D:\Flask\writeRecord\img2\Flask多对多的模型.jpg)



## 分页器的方法paginate



    真分页：先分页再取数据
    假分页：先取数据再分页
    
    原生代码
    一页都几条数据（pagersize ），第几页（page）
    page=requerst.args.get('page')
    pagersize = request.args.get('pagesize')
    xxx.query.limit(pagesize).offset((page-1)*pagesize)
    
    封装代码
    @blue.route('/getPageFZ/')
    def getPageFz():
        pagination=sth.query.paginate(page=1,per_page=5).items  返回一个pagination对象
    for p in pagination
        print(pagination)
    
    return '分页成功'
    
    分页器
    	模型.query.paginate()    --->返回一个pagination对象
    		page            #页数
    		per_page        #一页多少条数据
    		False           #
    	Pagination对象属性
    		items          （每个页面的所有数据）
    		pages         （获取总页数）
    		prev_num      （上一页的页码）
    		has_prev      （是否有上一页）
    		next_num      （下一个页码）
    		has_next	  （是否有下一页）
    		iter_pages    （上一页和下一页的页码）
    
    也就是BaseQuery.paginate()在后端
    pagination参数在前端



### views.py

~~~
@blue.route('/info/')
def info():
-->获取前端返回的页码
    page = int( request.args.get('page',1))    
——>获取前端返回给的每页条数，可默认
    per_page = request.args.get('per_page',5)   
——>可用查询的方式获取页码，表名.query.paginate
    pagination = Movies.query.paginate(page=page,per_page=per_page)
——>把分页器对象传到前端即可
    return render_template('staffinfo.html',pagination=pagination)
~~~



## html页

~~~

    <div >
        <table class="table" width="200px" height="150px">
                <tr align="center">
                  <td class="active">电影</td>
                  <td class="success">导演</td>
                  <td class="warning">主演</td>
                  <td class="danger">时间</td>
                  <td class="info">简介</td>
                  <td class="active">时长</td>
                </tr>
            {% for movie in pagination.items %}        --->用分页的条目来控制页面大小
                <tr align="center">
                  <td class="active">{{ movie.name }}</td>
                  <td class="success">{{movie.doyan}}</td>
                  <td class="warning">{{movie.starring}}</td>
                  <td class="danger">{{movie.showtime}}</td>
                  <td class="info">{{movie.mesage}}</td>
                  <td class="active">{{movie.evaluate}}</td>
                </tr>
            {% endfor %}
        </table>
    </div>


    <div style="width: 1000px;margin: auto">
    {% if pagination.has_prev %}                
         ——>判断是否有上一页，如果有 则返回给服务器下一页的页码  pagination.prev_num
        <a href="{{url_for('blue.info')}}?page={{ pagination.prev_num}}">上一页</a>
    {% else %}
    <a href="#">上一页</a>
    {% endif %}


    ——>根据pagination.pages的总页数设置页码
    {% for p in range(1,pagination.pages + 1 ) %}
        <a href="{{url_for('blue.info')}}?page={{ p}}">{{ p }}</a>
    {% endfor %}
    
    ——>判断是否有下一页  pagination.has_next
    {% if pagination.has_next %}
        ——>如果有下一页，则给服务器返回下一页的页码  pagination.next_num
        <a href="{{ url_for('blue.info') }}?page={{ pagination.next_num }}">下一页</a>
        {% else %}
        <a href="#">下一页</a>
    {% endif %}
    </div>
~~~








**BOOTSTRAP**

pip  install flask-bootstrap    创建

Bootstap（app=app）在ext页面里初始化

Externall Lbraries   ——>  site-packages  ——>  flask_bootstrap  ——> bootstrap  ——>base.html

~~~
flask-bootstrap
<head>
     head
         title
         metas
         styles
</head>
================================================
<body> 
      body
          navbar   -->导航
          content
          script
</body>
~~~



**bootstrapDemo.html模板**

~~~
{% extends ‘bootstrap/base.html’ %}    
                              -->继承bootstrap模板
{% block navbar %}     #导航
    {{ suber() }}
{% endblock%}
~~~

refmancode







**flask-debugtoolbar** 调试工具

~~~
pip install flask-debugtoolbar

在ext.py中
from flask_debugtoolbar import DebugToolbarExtension

app.debug = True
app.config['SECRET_KEY']='110'        -->如果没有设置session的SECRET_KEY则必须要设置
debugtoolbar = DebugToolbarExtension()  ——>初始化
debugtoolbar.init_app(app=app)         ——>注册

~~~

versions  版本

httpheaders   请求头

request vars   请求内容

config  配置

templates   模板

SQLAlchemy  数据库时间     --->做性能优化

Route  list   路由列表

profliler   不知道

