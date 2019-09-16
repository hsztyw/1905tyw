import logging
#全局唯一id
import uuid
import datetime
from base64 import urlsafe_b64encode as b64encode
from base64 import urlsafe_b64decode as b64decode
#base64.encodebytes(s)    编码
#base64.decodebytes(s)    解码 ，解码后再用decode转回来
#处理图形图像、url请求都需要用base64编码，只是编码和解码系统
#base64.urlsafe_b64decode(s)    可以把/n去掉

import tornado.escape
import tornado.websocket

from logics import MsgHistory


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('home.html', isusname=False)    #——>登录界面

    def post(self):
        username = self.get_argument('username').strip()    #一般情况下都会去空格 strip
        if not username:
            self.redirect('/',isusname=True)     #——>如果没有输入用户名，重定向到首页,并提示

        b64_username = b64encode(username.encode('utf8'))
        self.set_cookie('username', b64_username)    #网页端缓存，记录username，只能记录ascll码，中文无法记录
                                    #用base64编码来把中文转化成ASCII码，某些程度也可以压缩，如果没有，则会报错
        #见附录1
        self.render(
            "chat.html",
            messages=ChatSocketHandler.history.all(),
            clients=ChatSocketHandler.members,
            username=username
        )                                   #聊天页面


class ChatSocketHandler(tornado.websocket.WebSocketHandler):
    #历史记录，用redis做
    members = set()    #所有成员的连接池
    history = MsgHistory()    #历史消息对象
    client_id = 0    #客户端计数器

    #对传给html时进行压缩
    def get_compression_options(self):
        # Non-None enables compression with default options.
        return {}

    #建立连接时的事件处理
    def open(self):
        #客户端id自增
        ChatSocketHandler.client_id += 1
        self.client_id = ChatSocketHandler.client_id

        #保存当前用户名称，把用户名称保存到网页cookie中，登录时，会从网页端调到服务器端
        b64_name = self.get_cookie('username')
        #检查能不能取到这个名称
        if not b64_name:
            #如果为空，则给一个游客身份
            self.username = "游客%d" % self.client_id
        else:
            #将cookie中的名称base64编码的姓名进行解码，然后赋值
            self.username = b64decode(b64_name).decode('utf8')
        #将用户连接添加到连接池
        ChatSocketHandler.members.add(self)

        #定义登录消息，并向其他用户进行广播
        message = {
            "id": str(uuid.uuid4()),    #唯一的id，标记消息的id
            "type": "online",           #看是否是在线还是离线
            "client_id": self.client_id,
            "username": self.username,
            "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        ChatSocketHandler.broadcast(message)   #用户消息广播出去

    def on_close(self):
        '''断开连接的处理'''
        #删除自身的连接
        ChatSocketHandler.members.remove(self)

        #向所有用户广播离开的消息
        message = {
            "id": str(uuid.uuid4()),
            "type": "offline",
            "client_id": self.client_id,
            "username": self.username,
            "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        #再把消息广播出去
        ChatSocketHandler.broadcast(message)

    @classmethod
    def broadcast(cls, message):
        logging.info("sending message to %d members", len(cls.members))
        #对连接池做一个循环，
        for member in cls.members:
            try:
                member.write_message(message)
            except:
                logging.error("Error sending message", exc_info=True)

    #相应消息内容
    def on_message(self, message):
        #消息都是json格式
        logging.info("got message %r", message)
        #在tornado里对json_decode解码问题
        parsed = tornado.escape.json_decode(message)

        #组装消息结构
        self.username = parsed["username"]
        # 拼接消息
        message = {
            "id": str(uuid.uuid4()),
            "body": parsed["body"],
            "type": "message",
            "client_id": self.client_id,
            "username": self.username,
            "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        #to_basestring是tornado的
        message["html"] = tornado.escape.to_basestring(
            self.render_string("message.html", message=message)
        )

        # 把消息加入到历史消息
        ChatSocketHandler.history.add(message)
        #把消息广播出去
        ChatSocketHandler.broadcast(message)
