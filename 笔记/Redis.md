# Redis  MongoDB

mysql 关系型，表结构类型的

## NoSQL

因为mysql类型太死板，有时候不能应用。近十年发展比较快速

**Redis和MongoDB就是一个NoSQL类型的数据库**

**按列存取：HBase（大数据领域、数据分析领域用的比较多）    Cassandra  Hypertabl**e

​        mysql按行存取，

**文档类数据库：MongoDB    couchDB   ElasticSearch**（弹性搜索，最流行的开源的搜索引擎，一般都是用这个）

​         主要是存取JSON格式的数据

**KV数据库：DynamoDB  Redis   LevelDB**

​         key  values  键值对存取

​         最大的特点就是快。O1的存取数据

**图数据库：Neo4J    FlockDB  JanusGraph**

​         使用图结构进行语义查询的数据库

**对象数据库： db4o   versant**

​        通过类似面向对象语言的语法操作数据库



## Redis

redis —— remote dictionary sever  远程的字典服务器

* 开源
* 读写性能极高，经常用缓存，它所有的数据在运行的状态，都直接保存在内存里，当需要的时候，才保存在硬盘上。一切都是从性能方面出发。对内存要求大
* 支持两种数据方式  RDB和AOF
* 支持多种数据类型   string hash  list  set  zset  bitmap(位图)  hyperloglog



## Redis安装

~~~
在linux安装
一、下载安装包
sudo apt install -s redis           #1.尝试安装，不是真实的安装，下载的不是最新版本，需要从官网下载
wget http://download.redis.io/……    #2.官网redis.io  复制downdraft it 第一个连接

二、解压安装包并编译和安装
tar -xzf redis-5.0.5.tar.gz         #下载的是源代码，src文件夹中都是c语言，
                                    # .c是c语言源代码，.h是c语言头文件，c语言需要编译

make  makefile                      # makefile 自动化批处理的脚本，写好的编译内容。用make来直接编译
                                    #编译结果得到一个二进制文件，这个文件可以直接执行

cd src/                             #在该文件夹下 redis.serves,是最终的执行文件
make install                        #安装到系统cd /usr/local/bin,
                                    #可以用make && sudo make install 直接完成以上两步

cd  usr/local/bin                   #里面有文件，redis

三、配置redis
vim  redis.conf                     #在源代码包里 /home/py/redis-5.0.5 有个redis.conf的redis配置文件
    bind 127.0.0.1         #不能设置到0.0.0.0
    port 6379              #默认端口号，不用改
    daemonize  no          #守护进程，在后台默默运行，要改成yes
    loglevel notice        #日志级别，如果低级别，写入的东西会非常多，改为warning  只有遇到问题才会打印
    logfile                #记录日志文件的路径，默认在/dev/null 不记录，改为/tmp/redis.log,temp临时目录
    detabases 16           #数据的数量，mysql数据库用指令创建，redis则是1、2、3编号，默认启动是16个数据库。轻量级的数据库，没有表
    alays-show-logo yes    #启动显示logo 无所谓
    save 900 1         #900秒内如果对任何一个key发生修改，就会写入到硬盘
    save 300 10        #300秒内，10个key发生修改，就会写入到硬盘
    save 60  10000     #60秒内，10000个key发生修改，就会写入到硬盘
    dbfilename dump.rdb     #dump.rdb,写入数据库的文件名，内存数据写入到硬盘就是这个名字
    dir ./                  #rdb保存的位置，一般放到/var/  还可以写在tmp，每次重启都会丢失，或者写入 home文件夹下
    
四、运行数据库 
    sudo cp redis.conf /usr/local/etc/            #自己安装的文件，最好把配置文件放在这里
    sudo redis-server /usr/local/etc/redis.conf   #运行redis
    ps aux |grep redis                            #查看redis进程是否启动
    
五、使用redis
    redis-cli                #可以设置用户名和密码，但redis一般运行在内网中，所以不需要用用户密码

六、存取数据
    set  key  value          #存入key 和 value 数据
    get  key                 #获取value
             #redis只有一个字段，只有一个key和一个value
~~~



## 数据类型

redisdoc.com    详细记录了redis命令什么东西

### 字符串：常用于缓存

​              数据库存取是以 毫秒为单位，redis的存取速度，最快能达到1秒能执行11万次，mysql最快几千次。

​             可以把mysql的数据取出到内存，再放到缓存中，进行存取。

~~~
set 和 get 只支持字符串，其他的数据类型无法识别，最能当做字符串传出来

set xxx  123 EX 10   #设置过期时间。表示10秒后数据将会销毁
get xxx              #只能在十秒内获取到xxx对应的values，过期就成了nil 空值
ttl xxx              #查看剩余的秒数

set aaa  123
incr aaa             #自增操作，每执行一次就会增加1
~~~

![1568452660689](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568452660689.png)

![1568452846906](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568452846906.png)



### 哈希表 

做对象存储

~~~
典型的键值对。
hset xxx  a 123 b456 c 789   #表示在redis 存了一个xxx字典
hgetall xxx                  #取出所有值
hget xxx  b                  #在xxx字典里取b的值
~~~

![1568453042632](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568453042632.png)

![1568453084074](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568453084074.png)



### 列表

更类似于队列，适合存放消息

~~~~
双端数组，更类似于队列，适合存放消息
rpush mm 1                  #在mm数组的右边存放一个值
rpush mm 3
rpush mm 5
lrange mm 0 -1              #查看全部数据，结果为1,3,5

lpush mm 2                  #在mm数组的左边存放一个值
lpush mm 4                  
lrange mm 0 -1               #查看所有元素 4 2 1 3 5

lpop mm                     #从左边弹出一个数据，就是删除，返回值就是被删除的数据
rpop mm                     #从右边删除一个数据
~~~~

![1568453222101](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568453222101.png)

![1568453282554](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568453282554.png)

![1568453343391](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568453343391.png)



![1568625633976](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568625633976.png)









### 集合

做去重

~~~
去重、求交集、差集
sadd  sss 11 22 33          #在redis里添加了一个sss的集合有三个值11 22 33
sadd  fff 33 44 55
sinter sss  fff             #取两个集合的交集
sunion  sss  fff             #取并集
sdiff  sss  fff             #取差集
~~~

![1568453387670](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568453387670.png)

![1568453444929](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568453444929.png)

![1568453479127](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568453479127.png)



### 有序集合

~~~
适合做排行榜
zadd rank 99 za2 22 za3 76 za4 45 za5 56 za6 82 za1  #创建一个无序集合rank
zrange rank 0 -1               #取出rank里的所有数据，只有key
zrange rank 0 -1 withscores    #取出名字的时候带数字，key values都有
zrevrange rank 0 -1 withscores #反序排序
zincrby rank 1 za2             #给za2增加1,
~~~

![1568456285249](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568456285249.png)

![1568456310787](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568456310787.png)



## python连接redis

~~~
1.安装redis包
pip install redis

2.在ipthon中
import redis                #导入redis
r = redis.Redis([host=127.0.0.1……])           #都是默认值，一般不需要写host
r.keys()                    #查看redis存了多少key
r.sinter（'sss','fff'）      #取交集，返回一个集合类型
r.type('xxx')               #查看xxx是什么类型的数据
r.hgetall('xxx')            #取出xxx哈希表，返回值是字典
r.set('abc',12345)          #存入一个字符串
r.get('abc')                #取出abc字符串
~~~

取出的东西，都是二进制，byte类型

![1568456986666](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568456986666.png)



# MondgoDB

在爬虫的时候会用，通过爬虫抓取的数据不规范，存取速度要求高，数据灵活度高，因而需要用MongoDB。

MongoDB是json类型，不需要建立表

## **MondgoDB安装和配置**

~~~
1.下载社区版
sudo apt install -s mongodb   #尝试下载，最好不要用http网页下载
ps aux | grep mogo            #查找这个软件
pip install pymongo           #在python环境中下载mondgodb
~~~

~~~
2.连接Mondgodb     #不需要从终端操作，因为终端都是json文件，很麻烦
import pymongo
cli = pymongo.MongoClient(
        host=None,
        port=None,
        document_class=<class 'dict'>,
        tz_aware=None,
        connet=None,
        type_registry=None,
        **kwargs,
        )                                   #可以不写，默认端口号是27017
                                            或者可以写成：
                                            pymong.MongoClient('mongodb://127.0.0.1:27017')

2.创建数据库、数据集、一条数据                  #这些东西不需要创建，可以直接写
cli.sh1905.student.insert({                #直接创建一个sh1905数据库，student数据集，还有一条数据
                           'aaa':78,
                           'bbb':88,
                           'ccc':66,
                           'ddd':77
                           })              ==>ObjectID('3ld3jsf9fds2ds')
                                           #返回的值是刚刚插入的数据的id
cli.sh1905.student.insert({
                           'eee':[1,2,3],
                           'fff':'fslfdsls'
                           })              #数据类型可以随意改变，完全不受约束
#以上的插入数据方式已经不建议使用，可以使用insert_one,或者insert_many
cli.sh1905.student.insert({
                           'ggg':[6,6,6],
                           'hhh':'fslfdsls'
                           })

3.查看所有数据
for i in cli.sh1905.student.find()  
    print(i)
#结果：

cli.sh1905.student.find().count_documents({'ggg':[6,6,6]})      #查找条件为ggg的值为[6,6,6]数据的条数

cli.sh1905.student.find('aaa':78)                               #这种也是条件查找

cli.sh1905.student.find_one('aaa':78)                           #查找满足条件的第一条数据

cli.sh1905.student.find_one('aaa':78).limit(2)                  #查找满足条件，并且限制只取两条

list(cli.sh1905.student.find_one('aaa':78).limit(2))            #作为列表查找

cli.sh1905.student.find_one('aaa':78).count()                   #查看列表的数量
~~~

