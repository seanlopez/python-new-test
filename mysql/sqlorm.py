from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://tianqi:Tq19950822.@192.168.223.22/Test", encoding='utf-8', echo=True)    #mysql+pymysql://username:password@databse ip/DB_name
# echo = True，可以打印sqlalchemy对数据库的操作

Base = declarative_base()     #创建ORM基类

class User(Base):    #继承基类，并且可以创建表
    __tablename__='new_user'
    id = Column(Integer,primary_key = True)
    name = Column(String(32))
    password = Column(String(64))

Base.metadata.create_all(engine)   #根据User这个类，创建表结构，这个函数的归根结底的功能就是执行通过Base基类衍生出来的其他的类中的操作。

Session_class = sessionmaker(bind=engine)
Session = Session_class()
user_obj1 = User(name="new_user1", password="cisco123")
user_obj2 = User(name="new_user2", password = "cisco456")
Session.add(user_obj1)
Session.add(user_obj2)
Session.commit()

print(user_obj1.id, user_obj2.id)
