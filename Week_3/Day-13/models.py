from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users_orm'
    id    = Column(Integer, primary_key= True)
    name  = Column(String(100), nullable=False)
    email = Column(String(100),unique=True)
    age   = Column(Integer)
   

    posts=relationship("Post",back_populates="author")
    
    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}', age={self.age})"

class Post(Base):
    __tablename__= 'posts_orm'
    id= Column(Integer,primary_key=True)
    user_id= Column(Integer,ForeignKey('users_orm.id'))
    product= Column(String)

    author= relationship(User,back_populates= "posts")

    def __repr__(self):
        return f"Post(id={self.id}, product='{self.product}', user_id={self.user_id})"
    

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title= Column (String(200), nullable=False)
    completed= Column(Boolean, default=False)

def __repr__(self):
    return f"Post(id={self.id}, title='{self.title}', completed={self.completed})"



