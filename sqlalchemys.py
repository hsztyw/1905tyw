import pymysql
import datetime

from pymysql import Date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column,String,Integer,Enum,Date
from sqlalchemy.ext.declarative import declarative_base
import tornado.ioloop
import tornado.web

engin=create_engine('mysql+pymysql://tyw:123@localhost:3306/mystudent?charset=utf8mb4')
base=declarative_base(bind=engin)
Session=sessionmaker(bind=engin)

class student(base):
    __tablename__='studente'
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(20))
    birthday=Column(Date)
    sex=Column(Enum('男','女'))
    city=Column(String(10))

base.metadata.create_all(checkfirst=True)
session=Session()

lb=student(name='刘邦',birthday=datetime.date(1990,3,21),sex='男',city='北京')
cqe=student(name='陈乔恩',birthday=datetime.date(1993,1,21),sex='女',city='南京')
zgr=student(name='张国荣',birthday=datetime.date(1995,5,21),sex='男',city='广东')
zly=student(name='赵丽颖',birthday=datetime.date(1996,4,21),sex='女',city='河南')
wbq=student(name='王宝强',birthday=datetime.date(1994,7,21),sex='男',city='山东')
zxy=student(name='张学友',birthday=datetime.date(1992,5,21),sex='男',city='广东')
wj=student(name='王晶',birthday=datetime.date(1999,2,21),sex='男',city='北京')

# session.add_all([zly,cqe,wbq,zxy,wj,lb,zgr])
# session.commit()

arr=[wj.id,wj.name,wj.birthday,wj.sex,wj.city]
names={'刘邦':lb,'张国荣':zgr,'王晶':wj,'赵丽颖':zly,'王宝强':wbq,'张学友':zxy}



class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('ORMtest1.html',studtble=arr)

class SelectHandler(tornado.web.RequestHandler):
    def post(self):
        namer = self.get_argument('name')
        print(namer)
        q = session.query(student)
        resurl = q.filter_by(name=namer).first()
        student_sth=[resurl.id,resurl.name,resurl.birthday,resurl.sex,resurl.city]
        self.render('ORMtest1.html',studtble=student_sth)

class UpdaHandler(tornado.web.RequestHandler):
    def post(self):
        id_name = self.get_argument('id_name')
        idorname = self.get_argument('idorname')
        file_name = self.get_argument('file_name')
        test_txt = self.get_argument('test_txt')
        if id_name==1:
            q =session.query(student)
            result = q.filter_by(id=idorname).exists()
            p = session.query(result).scalar()
            if p:
                q.filter(student.id == idorname).update({file_name:test_txt}, synchronize_session=False)
                session.commit()
                self.render('updatescess.html')
            self.render('updateful.html')
        else:
            q =session.query(student)
            result = q.filter_by(name=idorname).exists()
            p = session.query(result).scalar()
            if p:
                q.filter(student.name == idorname).update({file_name:test_txt}, synchronize_session=False)
                session.commit()
                self.render('updatescess.html')
            self.render('updateful.html')



def make_app():
    rose = [(r'/',MainHandler),(r'/select',SelectHandler),(r'/update_info',UpdaHandler)]
    return tornado.web.Application(rose,
                                   template_path='temples',
                                   static_path='statics')

if __name__=='__main__':
    app=make_app()
    app.listen(8000,'127.0.0.1')
    loop=tornado.ioloop.IOLoop.current()
    loop.start()
    print(111)
