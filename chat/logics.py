import json

from redis import Redis

rds = Redis()
#从redis里写入json


#创建一个历史消息
class MsgHistory:

    #把消息存到key里
    key = 'chat_history'
    size = 100    #保存的长度

    @classmethod
    def add(cls, msg):
        #记录一条历史消息
        json_msg = json.dumps(msg)    #把消息转换成json格式
        rds.rpush(cls.key, json_msg)  #rpush：将转换成的消息加入redis的list中
        rds.ltrim(cls.key, -cls.size,-1)  #当达到100条就删了列表的前面一条，

    @classmethod
    def all(cls):
        #取出所有的历史消息
        all_msg = []
        for json_msg in rds.lrange(cls.key, -cls.size,-1):
            msg = json.loads(json_msg)     #解码
            all_msg.append(msg)            #添加到列表
        return all_msg                     #返回
