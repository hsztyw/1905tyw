<h1>GITHUP</h1>
MVC  model  view  ctrl  

**模型层**程序需要操作的数据

**视图层**提供给用户的操作界面，就是web显示层面

**控制层** 负责从视图层输入指令，选取数据层的数据，然后对齐进行相应的操作，产生的结果放到视图层



将代码分成这三个文件（模块）

高内聚  低耦合

对内可以相互调用，对外调用，只能调用接口，不会对内部造成影响

![1568171385434](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568171385434.png)



# 虚拟环境

**解决问题：环境冲突、导致运行出现错乱** **维护多个项目，每个项目使用不同的安装包，使得运行时不会冲突。跟虚拟机差不错，使得不同环境相互隔离，相互共存**

~~~
pip freeze   查看所有安装包的版本
pip list     查看包

pip list |grep torando

pip install tornado==5.0  指定版本的安装包
~~~

**不同的项目使用不同的环境**

~~~
pip install virtualenv   下载虚拟环境
|
v
virtualenv env  #在当前项目（目录）下创建一个虚拟环境，env名字可以随便取

source env/bin/activate   #激活虚拟环境，这里的env是上面的名字
#进入虚拟环境后，一切环境、软件包都没有，需要重新安装

pip install tornado sqlalchemy pymysql ipython  #我们所需的安装包

deactivate    #退出虚拟环境

#共享环境，把自己的环境共享给其他人
pip freeze > requirements.txt     #把软件包版本号重定向到一个txt文件里

pip install -r requirements.txt   #把txt里的安装包都安装下来
#这种办法，txt文件里必须是安装包名字和安装包版本号的集合，其他内容无法识别
~~~

~~~
pip下载目录
	python安装目录/lib/python3.6/site-packages/
   
apt下载目录
   usr/local/share
            /lib
            /……
~~~





# GIT

不同版本，不同的开发者运作时，需要用工具来将代码合并到一起，就可以用到GIT

如果用人力，非常耗费资源

* 追踪全部代码状态

* 检查各个版本差异
* 能够进行版本回滚
* 能够协作多个开发者进行代码合并，如果代码有冲突，需要程序员自己来合并



**CVS**已经挂了，**SVN**还凑合，是一个汇总虚拟化的版本控制工具，时间用久了，空间会非常多   

**GIT** 分布式的版本控制工具，中心服务器不再是必需品，去中心化

**HG** 纯python开发的版本控制工具，使用方式什么的，跟git很像

**Github**依托git而创建的平台，有独立公司来运作  **gitup 代码托管网站**

所有文本类的东西，都可以交给版本控制工具来管理

**Linus Torvalds  芬兰 Linux创始人，git创始人**

 

~~~
git 文件名  文件名  #查看两部分代码，做了哪些修改
~~~

**管理代码**

~~~
clone   克隆
init    初始化

add     增
mv      移
reset   改
rm      删
~~~





#配置文件

~~~
1.配置文件，将自己githup官网的用户名和邮箱名作为全局变量
git config --global user.name ‘用户名’
git config --global user.email ‘hsztyw@163.com’   #配置文件全局范围内，用户名和邮箱


2.在库里（项目文件里）对仓库进行初始化，
touch .gitignore     #创建隐藏文件，这个文件极其重要，不能写错
vim  .gitignore      #将不需要的文件夹或文件写入到这个文件里
git init ，          #初始化git  ——>产生了.git的工作目录，就是本地仓库
git status           #查看git状态，可以查看到未追踪的文件和已经追踪的文件

3.追踪文件/文件夹（将文件/文件夹添加到暂存区）
git add 文件名/文件夹    #追踪文件/文件夹
git add ./             #追踪所有文件和文件夹，.pyc python运行时的临时文件

git reset 文件名        #重置文件在git的状态|将暂存区中的文件取消暂存状态
git diff               #查看文件修改前后的对比
git diff HEAD^  HEAD   #HEAD表示最新版本，^表示上一个版本，再上一个，多加一个^

4.将暂存区的文件提交到git远程仓库里
git commit -m ‘说明：第一个版本’    #从暂存区提交到本地仓库，-m表示注释参数，后面加注释

5.上传至远程仓库
git remote add origin git@github.com:hsztyw/firstgit.git
git push -u origin master

git log   #查看提交历史
~~~



![1568187836375](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568187836375.png)

![1568188065455](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568188065455.png)

<center>查看提交历史</center>
#创建网站

网站新建

![1568188163177](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568188163177.png)

![1568188460522](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568188460522.png)

![1568188658233](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568188658233.png)

![1568188765108](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568188765108.png)

![1568188826968](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568188826968.png)

![1568189153342](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568189153342.png)

~~~
ssh 协议，需要通过公钥秘钥来与远程服务器建立连接
ssh-keygen  #远程秘钥，直接回车，回车，回车
密钥所在的文件夹:/home/tyw/.ssh/      id_rsa为密钥   id_rsa.pup为公钥
~~~

![1568189484405](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568189484405.png)

在该目录下

![1568189642128](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568189642128.png)



上传公钥

![1568189668174](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568189668174.png)

发送成功后



![1568189799009](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568189799009.png)

![1568190098807](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568190098807.png)



将代码下载到本地

一般都是用SSH协议

![1568190332813](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568190332813.png)

~~~
git clone git@github.com:seamile/xxx.git   #从远程下载到本地

git add  inint.py     #任何文件的增删查改都要添加到暂存区

git commit -m  ‘一个py文件’   #提交到本地

git push             #二次增删改查，直接回车,上传到git服务器
~~~



**把远程多的文件，拉到本地**

~~~
git pull   #可以把远程更新的文件，可以直接下载本地没有的文件

pull和clone
clone是首次获取远程所有文件
pull下载的远程更新的文件，根据本地提交记录和远程提交记录来下载
~~~





### checkout

切换分支、代码还原、代码回滚

回滚到之前某一次的提交。

1.先查看所有的提交记录

2.git  checkout  记录的id      #回滚到为id的记录时，如果id前面没有冲突，少写几位也可以识别

3.git  checkout  master        #撤销回滚记录，所有提交的代码都不会丢失，会留在当前文件夹中的 .git中

**还原代码**

4.git diff   前后不同的记录

5.get checkout  代码文件名    #还原更改的文件，还原的文件都必须是还没有add的文件，更没有提交到commit

6.如果是提交上去了，无法撤回，git reset 还原文件名，再从这里还原代码

~~~
git diff  旧id 新id      #查看两个版本的差异
git diff  HEAD^ HEAD    #这个也可以

git checkout id 		 #回滚到记录位置

git checkout 文件名  	   #还原已改文件或代码

git checkout master 	 #撤销回滚记录

git reset       		 #可以撤回添加到暂存器

git rm --cached 文件名    #当文件添加到暂存区时，可以用这个方法撤回
~~~



## blame

查看最后一次是谁修改的

1.git blame  文件名       #查看该文件最后是谁修改的

![1568194629701](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568194629701.png)





# 分支管理

1.如果多个人同时对一个文件进行修改，会造成冲突

2.如果别人已经推送到git时，会报错，无法修改，需要先git pull，再去推送自己push

3.下载之后，两个代码就会被合并。最后B才能提交push

4.git log --graph   就可以查看到两条线，在中间的某个位置，出现了分叉

**这个分叉就是分支**

如果两个人同时修改同一个文件会出现冲突，修改的是同一个文件，同一行。这样的冲突，会出错

get fetch     表示下载后，不合并，文件之后是单独的。

产生冲突之后，文件会改变

![1568253036060](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568253036060.png)

**出现这种冲突，需要与对方协商使用谁的代码，然后更改代码，最后再删除标记**

~~~
git push    #发现与别人修改的代码有冲突
git pull    #将线上代码，拉取到本地
git status  #找到冲突文件都有哪些，冲突文件的状态是 both modifide

1.逐一打开冲突文件，逐行解决冲突
冲突代码解决后，将代码冲突的标记删除
git add ./ 
git commit -m‘解决冲突，进行了一次合并’
git push

~~~

如果人数过多，更是无法插入。

解决为问题

稳定版与测试版的内容，没有经过测试，测试版是最新的版本，测试版就低了很多层次

在开发中的状态，可以相互隔离，不会相互合并。直到提交后才进行合并



**同源的不同开发者同时提交发生的冲突**

~~~
1。创建分支
git branch 开发者1     #创建分支 四个开发者创建四个不同的分支
git checkout 自己的分支名  #切换到自己分支下

git checkout -b ‘分支名’  #如果分支不存在，将会创建并切换至该分支

2.各自分支进行代码更新和提交到本地仓库，此时还没有冲突

3.在发送的时候，会报错，因为这是本地的分支，需要在上游上也要创建一个分支，否则是无法知道推送到哪里

4.get push --set-upstream origin  各自分支名

5.成功推送，此时推送的是四条分支，并没有在主分支中
~~~

![1568257448538](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568257448538.png)

![1568257504630](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1568257504630.png)



**合并分支**

~~~
git checkout  master    #1.先回到master主文件中
git pull                #2.先把远程的仓库拉下来，开发的时候，合并之前，最好先更新一下。
git merge 分支名         #3.把分支与当前主分支合并
git push                #4.提交到远程仓库master总库


必须先pull更新，再push上传
git checkout -          #切换到之前的分支
~~~

