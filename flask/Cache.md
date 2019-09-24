Cache

缓存的目的

数据库缓存，

前端样式缓存：.xxxx.css.map，谷歌部分支持样式缓存，下次打开，可以直接开，不需要重复去访问

缓存目的：

​        缓存优化加载，减少数据库的IO操作

实现方案：

​        缓存存储的位置，可以放在另一个数据库，文件、内存、内存中redis

数据库不怎么样，多此一举，文件，访问也比较长，内存不太好，redis最优秀

实现流程

​       1.从路由函数进入程序

​		2.路由函数到视图函数

​		3.视图函数去缓存中查找

​		4.缓存中找到，直接进行数据返回

​		5.如果没有找到，取数据库中查找

​		6.查找之后，添加到缓存中

​		7.返回页面	

## flask-cache方法

~~~
安装  pip install flask-cache
ext.py指定缓存方案
from flask_cache import Cache
   cache = Cache(confi={'CACHE_TYPE':'redis'})    -->配置缓存方案
   cache.init_app(app=pp)          ——>初始化
  
========================================================================
   如果cache在方法内，导包是不可以的，需要将这个变量放在方法外，也就是ext的函数外面
@cache.cached(timeout=30)
def hellCache():
    print('how are you')
    return 'helloCache'

如果报错 ImportError： No module named 'flask.ext'
解决方法：
      site-package ——> flask_cache ——> jinja2ext.py
      把33行的 from flask.ext.cache import make_template_fragment_key
      修改为 from flask_cache import make_template_fragment_key

还会报错No Find viewfunction  没有视图函数
@cache.cached(timeout=30)
@blue.route('/chached/')
def hellCache():
    print('how are you')
    return 'helloCache'
装饰器放在路由函数之下和之上都可以，但是放在之上没有什么卵用
============================================================================
redis开启

sudo redis-server /usr/local/etc/redis.conf
redis-cli

=============================================================================
正确写法
@blue.route('/chached/')
@cache.cached(timeout=30)
def hellCache():
    print('how are you')
    return 'halloword'
~~~

![1569251809701](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1569251809701.png)



## cache的原生

~~~
需求：如果是第一次访问，显示欢迎光临
     如果第二次访问，显示爬虫撤退
     
cache.set('id',id)   -->设置缓存变量
cache.get('id')      -->获取缓存中的id变量

@blue.route('/chached/')
def hellCache():
    id = cache.get('ip')
    if id:
       print '爬虫走开'
    else
        ip=request.remote_addr   -->获取id
        cache.set('ip',ip)       -->把id放进缓存中
        print ‘欢迎光临’
    return 'helloCache'
~~~



# 钩子

定义：在代码执行的过程中，添加了另一个方法的执行，所谓的aop

AOP：面向切面编程

优点：

​        1.减少代码量：如果每个方法中添加了##print('连接数据库')，代码量过于冗余，如果每个方法用函数调用，则依赖性很强。必须每个视图函数都要加调用的函数

​        2.耦合度低：解耦合。

~~~
@blue.before_request
def beforeRequest():
    print('连接数据库')

=============================================================================
@blue.route('/add/')
def add（）：
   #print('连接数据库')
   return  "add"
   
@blue.route('/delete/')
def delete():
   #print('连接数据库')
   return  "delete"
   
@blue.route('/update/')
def update():
   #print('连接数据库')
   return  "update"

@blue.route('/find/')
def finde():
   #print('连接数据库')
   return  "find"

执行结果：
   连接数据库
============================================================================
和调用函数的区别
~~~



# 四大内置对象request     session    config    g

## config

~~~
模板中的config  
@blue.route('/testTemconfig/')
def testTemconfig():
    return  render_template('testTenmConfig.html')

---------html页面-------------------
{% for c in config %}              |
<li>{{c}}</li>                     |
{% endfor %}                       |
------------------------------------
=====================================================================
python中的config
@blue.route('/testPythonconfig/')
def testpythonconfig():
    for c in current_app.config:
        print(c)
    return  'python中的config'
~~~

## g

就是把视图函数中的变量，变成全局变量

~~~
@blue.route('/g/')
def g():
    #ip = request.remote_addr
    g.ip = request.remote_addr
    return 'g'
    
@blue.route('/testG/')
def testG():
    #print(ip)
    print(g.ip)
    return 'testG'
~~~





# 路径

~~~
OS模块
获取当前文件的目录
os.path.abspath(__file__)
_______________________________________________
获取当前路径的上一级路径
os.path.dirname(os.path.abspath(__file__))
~~~



~~~
templates和static路径问题
@blue.route('/index/')
def index():
    return render_template('index.html')

​~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
默认情况下，路由函数中调用静态文件和动态页面都是在当前文件夹的templates和static文件夹查找。
但很多时候，一个项目分为很多模块，每个模块相互独立的同时又会继承同一个html模板
因此在项目文件夹中也必须有一个templates和static文件
因此要查找模块以外的项目文件夹下的静态文件夹，则需要重新设置默认路径
解决方法：
————————————————————————————————————————————————————————————————————————————————————————
在__init__.py文件夹中,先获取项目文件夹的templates和static路径template_folder和static_folder

template_folder =os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'templates')
static_folder =os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"static")

def create_app():
    app = Flask(__name__,template_folder=template_folder,static_folder=static_folder)
~~~



# 前后端分离

~~~
就是前后端请求和发送的数据都是json数据
~~~



REST

是一种软件架构风格、设计风格，只是提供了一组设计原则和约束条件，主要是用户客户端和服务器交互类的软件

基于这个风格设计的软件可以更加简洁，更有层次，更易于实现缓存机制

2000年Roy Thomas Fielding 创建的  Fielding是http协议（1.0/1.1版本），是Apache服务器软件的作者之一，是Apache基金会到第一人主席

REST全称：Representational State  Transfer —— 表征性状态转移

~~~
saveUse r
表征性状态转移
http://127.0.0.1/user/query/1 GET根据用户 id查询用户数据
http://127.0.0.1/user/save POST新增用户
http://127.0.0.1/user/update POST 修改用户信息
http://127.0.0.1/user/delete GET/POST 删除用户信息

http://127.0.0.1/user/      根据请求方式的不同那么执行不同的函数
                            如果是get请求,那么执行的就是查询
                            如果是post请求,那么执行的就是添加
                            如果是put请求,那么执行的就是修改
                            如果是delete请求,那么执行的就是删除

~~~



**视图函数可不可以返回JSON数据**

~~~
@blue.route('/json/)
def json():
    data={
       'msg':'ok',
       'status':200
    }
    print(type(data))  ----->dict类型
    ----------------------------------
    data = jsonify(data)
    print(type(tada))  ----->flask.wrappers.Response类型
    return data
可以返回，但是需要加jsonify()
~~~



## **原生前后端分离**

~~~
前端查询
#前后端分离源码的时候，是不可以直接传输对象的

查看一条
@blue.route('/getdata/)
def getData():
    data=Data.query.first()
    data_respon = {
         'msg':'ok'，
         ‘status’：200,
         'data':data.to_dcit()    --->调用对象的方法，不能是对象本身
    } 
    return data

=======================================================================
查看多条
@blue.route('/getdata/)
def getData():
    data_list=Data.query.all()
    datasql = []
    for data in data_list
        datasql.append(data.to_dict())    --->查看多条，用for循环搞出来
    data_respon = {
         'msg':'ok'，
         ‘status’：200,
         'data_D':datasql              --->调用对象的方法，不能是对象本身
    } 
    #return data
    return jsonify(data)             -->直接写return和jsonify差不多
    
------------------------------------------
数据库对象加一个方法
def to_dict(self):
    return{ 'id':self.id,'name':self.name}
    
===========================================================================
html前端页面 
getJson能做的是发送请求并且相应数据，接收的数据在页面中进行渲染

getJSON的参数格式
     url 请求资源路径                          
     data 请求参数   参数是字典类型，可以不写     
     function（data）{}  返回值     

变量加$ 表示是jquery对象

---------------------------------------------------------------------
<script type='text/javascript' src='jquery.js'></script>
<script type='text/javascript'>
    $(function(){
       $('button').click(function(){

           $.getJSON(
                "/getdata/",                   
                function(data){            		 	--->data就是后端传来的参数
                   var datas = data['data_D'];   	-->接收的参数,参数必须是json对象的key
                   var $ul = $('ul')       			-->获取jquery对象
                   
                   for(var i=0;i<datas.length;i++){
                     var $li = $('<li></li>');     -->创建li标签
                     $li.html = (datas[i].name;)   --->获取字典的json对象
                     $ul.append($li);              --->往列表中添加元素
                   }
               })
       })
    })
</script>

<body>
   <button>数据</button>
   <ul> </ul>
</body>
~~~



~~~
jquery

​     封装了js的一个框架

​    入口    $(function(){  事件驱动  })

​    事件驱动：click   blur(失去焦点)  change(当元素的值发生改变时事件)  keyup 

​    $('选择器').事件驱动(function(){    })
        eg:    $('#name').click(function(){   })
     --->js原生代码
          onclik=aaa();
          function aaa(){ …… }
=============================================================================
综合起来
$(function(){
   $('div').click(funciton(){
        pass
   })
})
~~~



### 添加

前后端分离就没有form了

~~~
后端
​~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@blue.route('/toregister/')
def toregister():
    return render_template('register.html')

@blue.route('/register/')
def register():
    name = request.args.get('name')
    data = Database()
    data.name = name
    db.session.add(data)
    db.session.commit()    ----->获取数据并添加数据库
    
    datas = {
       'msg':'ok'
       'status':200
       'data':data.to_dict
    }                      ----->返回数据
    return jsonify(datas)

@blue.route('/index/')
def index():
    return '什么什么'

前端
​~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
name:<input type='text' id='name'>
<button>提交</button>

<script type='text/javascript' src='jquery.js'></script>
<script type='text/javascript'>
   $(function(){
      $('button').clik(funticon(){
          var name =$(#name).val();
          $.get('/register/',
              {'name':$name},      ---->传递参数是字典格式
              funtion(data){
                  window.open('/index/')；   --->跳转/打开新页面里显示
                  window.open('/index/',target='_self')  --->在本窗口进行跳转
                  window.location.href = '/index/'       --->在本窗口页面显示
              })
      })
   })
</script>
~~~



### 修改

put和patch来传递数据

put 修改全部数据   patch修改的是部分数据

~~~
后端
@blue.route('/toPut/',methods=['put'])   --->修改这里
def toPut():
    data = Database.query.first()
    data.name = 'python'
    db.session.add(data)
    db.session.commit()
    
    datas={
       'msg':'ok'
       'status':200
    }
    
    return jsonify(datas)
~~~



### 删除

~~~
@blue.route('/todelete/')
def todelete():
    data = Database.query.fisrt()
    
    db.session.delete(data)
    db.session.commit()
------------------------------
    datas={                  |
       'msg':'ok',           |
       'status':200          |
    }                        |
    return jsonify(datas)    |
不管是啥，都要写这玩意           |
~~~



### 综合

~~~
请求方式必须大写
@blue.route('/torequest/',methods=['put','get','put','pacth','delete'])
def torequest():
    if request.mothod = 'GET'
        datas={                  
           'msg':'get',           
           'status':200          
        }                        
        return jsonify(datas)
	if request.mothod = 'POST'
        datas={                  
        'msg':'post',           
        'status':200          
        }                        
        return jsonify(datas)
	if request.mothod = 'PUT'
        datas={                  
        'msg':'put',           
        'status':200          
        }                        
        return jsonify(datas)
	if request.mothod = 'delete'
        datas={                  
        'msg':'delete',           
        'status':200          
        }                        
        return jsonify(datas)
	if request.mothod = 'PACTH'
        datas={                  
        'msg':'pacth',           
        'status':200          
        }                        
        return jsonify(datas)
~~~





# flask-restful封装restful

**restful将不再需要蓝图，也不需要views，需要创建urls文件**

~~~
安装   pip install  flask-restful

初始化  再app中创建urls.py文件
	   from flask_restful import Api
       api =Api()      -->创建api对象
       
       def init_urls(app)
           api.init_api(app = app)   -->初始化,需要在__init__.py中调用这个函数，一定要

	   api.add_resource(catResource，'/cat/')     
	       需要一个继承了Resource类的对象，和路由
	       
创建apis文件夹
       1.创建catapis.py |即创建模型Apis文件
       2.在该文件中书写   class 模型名(Resource)
       2.from flask_restful import Resource
       class catResource（Resource）
         	    def get(self):           --->get请求
                    data={
                        'msg':'get',
                        'status':200,
                    }
                    return data

                def put(self):         --->put请求
                    data={
                        'msg':'put',
                        'status':200
                    }
                    return data

                def patch(self):      --->patch请求
                    data={
                        'msg':'patch',
                        'status':200
                    }
                    return data

                def delete(self):     --->delete请求
                    data={
                        'msg':'delete',
                        'status':200
                    }
                    return data

                def post(self):      --->post请求
                    data={
                        'msg':'post',
                        'status':200
                    }
                    return data	

乱码问题：init中app.config.update(RESTFUL_JSON=dict(ensure_ascii = False))  忽略编码问题

~~~







### 结构化输出

在apis中输入 

#### marshal_with装饰器

~~~
from flask_restful import Resource, marshal_with

r1Fileds = {        ------->预定义结构字段
   'msg':fields.String,
   'status':fields.Integer
}

@marshal_with(r1Fileds)  ----->返回的数据
def get(self):
    data = {
       'msg':'ok',
       'status':200
    }

===============================================================================
marshal_with装饰器特性
			        - 默认返回的数据如果在预定义结构中不存在，数据会被自动过滤
        	        - 如果返回的数据在预定义的结构中存在，数据会正常返回
                    - 如果返回的数据比预定义结构中的字段少，预定义的字段会呈现一个默认值
                        -如果类型是Integer  那么默认值是  0
                        -如果类型是String  那么默认值是null
                    - fields后面的类型 可以加（） 可以不加（）
~~~



1.fields中的类型约束

 	String    字符串

​	Integer   字符串

​    Nested   嵌套，即类对象。

​    List          列表

2.fields的约束

​    （1）.attribute（指定连接对应名字）

​           attribute=名字

​     （ 2）default（默认值）

​               default=404

~~~
from flask_restful import Resource, marshal_with

r1Fileds = {        ------->预定义结构字段
   'msg':fields.String,
   'status':fields.Integer,
   'attribute':fields.String(attribute='aaa'),
   'defff':fields.Integer(defaul=404)
}

@marshal_with(r1Fileds)  ----->返回的数据
def get(self):
    data = {
       'msg':'ok',
       'status':200,
       'aaa':"1000"
    }

~~~

![flask-restful-marshal_with](D:\Flask\writeRecord\img2\flask-restful-marshal_with.png)



#### mashl函数

~~~
from flask_restful import Resource, fields, marshal


class SingResource(Resource):
    r1Fileds = {
        'msg': fields.String,
        'status': fields.Integer,
        'attribute': fields.String(attribute='aaa'),
        'defff': fields.Integer(default=400)
    }

    def get(self):
        data={
            'msg':'get',
            'status':200,
            'aaa':1000
        }
        return marshal(data=data,fields=SingResource.r1Fileds)

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
在装饰器中，将@marshl_with 换成marshl的函数
marshl的参数
          - data   传递的参数
          - fields 字段约束
~~~



 **Nested   嵌套，即类对象。**

 **List          列表**

~~~
form flask_restful import Resource,marshal,fields




~~~



set 底层有两个条件实现无序和不重复，一个事echo和哈希来控制，字典就是用

~~~

requerstparse = reqparse.RequestParser()

parser.add_argument(name='name',type=str)   name是接收的参数，tpye参数类型 required  help('提示信息')




===================================================
def barse.get('name')
    parse = parser.parse_args()
    name = parse,get('name')



~~~









