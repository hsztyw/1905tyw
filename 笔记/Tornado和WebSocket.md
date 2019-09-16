# Tornado和WebSocket

传统交互模式：用户与服务器单线连接，用户只能发送请求，服务器只能相应请求。

解决模式：

1.短轮询：规定某个时间内来发送一次请求。（时间越短，消耗比较大）

​                  ajax 、jsonp 、Polling

* 优点：短连接、服务器处理简单，支持跨域，浏览器兼容性较好
* 缺点：有一定延迟、服务器压力大，浪费带宽流量，大部分都是无效请求



2.长轮询

在服务器端长时间等待，一直等到客户端发来请求。

优点：相对短轮询，减少轮询次数，低延迟，浏览器兼容性比较好

缺点，超时会报504的错。服务器需要大量的时间保持连接



3.webSockets

![1568601458830](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568601458830.png)

2011inane开始，是HTML开始提供的一种在单个TCP连接上的全双工通讯协议。虽然是TCP为底层，但是基于HTTP协议，还需要报文。

全双工：双向连接，可以随时相互通信，两者互不干涉

半双工：单向连接，按照时间或者频率去协商进行通信



与普通HTTP协议的一同

1.与http协议几乎相同。url是vs：//  或者vss:// 开头的 http是 http://或者https://

2.端口号也不同，不是80还是443

3.请求头不同

~~~
connection:Upqrade
Upqrade:websocket
~~~

![1568634550518](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568634550518.png)



# 通过JS建立一个简单的websocket连接

## js代码

~~~
#可以触发tornado的open函数
war ws = new WebSocket('ws://localhost:8000/msg')  

ws.onopen = function(){……}
#对应连接时的请求

ws.send('ssss')
#触发tornado的on_message()函数

ws.onclose()=function（）{}
#触发tornado的on_close方法

ws.onerror= function(error){}
#对应出错时的方法

ws.onmessage = function(event){    #表示服务器发过来的消息就会写入到event里
   写入DOM内容                      #可以写网页，还可以写其他东西
};

~~~



## python中用tornado中使用websocket

~~~
import tornado.websocket

class websockHandler（tornado.websocket.WebSocketHandler):）
    def open(self):
       '该方法处理建立连接执行的操作'
       pass
       
   def on_close(self):
       '该方法处理断开连接时执行的操作'
       
   def on_message(self,message):
       '客户端发来消息message。做出的事件'
       self.write_message('发送消息的内容')
       #发送的消息，是在控制台显示，需要解决，需要从js中写
   
   def write_message(self,message):
       '给其他人发送消息'
       pass
   
钩子函数：把事件与函数挂钩，当发生一件事，就会触发
~~~

### 简单建立连接

#### js代码

~~~
var ws = new WebSocket("ws://10.0.2.15:8000/msg")

ws.send('这是一条客户端的消息')
~~~



#### python的server端

~~~
import tornado.websocket
import tornado.web
import tornado.ioloop           #调用ioloop和websocket两者代码


#这里继承的则是websocket的Handler
class MsgHandler(tornado.websocket.WebSocketHandler):  
    conn_pool=set()         #创建一个用户池
    def open(self):
        print('客户端建立链接')
        self.conn_pool.add(self)

    def on_message(self,message):
        print('收到客户端消息：%s'%message)
        self.broadcast(message)

    def on_close(self):
        print('客户端断开了链接')
        self.conn_pool.remove(self)

    def broadcast(self,message):
        for conn in self.conn_pool:
            conn.write_message(message)

def make_app():
    return tornado.web.Application({
        (r"/msg",MsgHandler)
    })

if __name__=='__main__':

    app = make_app()

    app.listen(8000,'10.0.2.15')
    loop = tornado.ioloop.IOLoop.current()
    loop.start()
~~~





**logging程序日志输出：**

​        **logging级别debug、info、warning、error、fatal   级别越来越高，如果把级别调到error，前面的debug、info、warning则不会打印出来，一般级别都要调到error级别**

![1568615277654](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568615277654.png)

![1568619656403](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568619656403.png)









<h1>python中的type
</h1>

python中type底层创建类的方法

![1568622759288](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568622759288.png)

type（name，database，dict）

* name：类名

* bases：继承的对象,是个元组

* dict：是个字典属性什么的

~~~
定义方法
def speak（self）：
   print（‘我是%，我今年%s岁’%（self.name,self.age））
   
def run(self):
    print('%s正在奔跑'%self.name)


定义属性attr
attr={
   ‘name’：‘黑’，
   ‘age’：18，
   ‘head’：1，
   ‘body’：1，
   ‘tail’：1，
   ‘legs’：4,
   
   'speak':speak,
   'run':run
}

Dog = type('Dog',(object,),attr)    #组合成一个类

dog=Dog（）
dog.name
dog.head
dog.speak()
~~~





<h1> UUID全局唯一id
</h1>

一般都是用uuid4







