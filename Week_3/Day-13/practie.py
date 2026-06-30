from database import engine, SessionLocal, Base
from models import User,Post



db=SessionLocal()

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


user1=User(name='Bavithra',email='b@gmail.com',age=25)
user2=User(name='Keerthi', email= 'K@email.com',age=28)
user3=User(name='Ramya',email='r@gmail.com',age=22)
user4=User(name='Payal',email='p@gmail.com',age=25)


db.add(user1)
db.add(user2)
db.add(user3)
db.add(user4)
db.commit()

post1= Post(user_id=1,product= 'python book')
post2= Post(user_id=2,product= 'Sql Book')
post3=Post(user_id=4,product='postgres book')

db.add(post1)
db.add(post2)
db.add(post3)
db.commit()


users= db.query(User).all()
for user in users:
    print(user)

users= db.query(User.id,User.name).all()
for user in users:
    print(user.id,user.name)


users= db.query(User).order_by(User.age).all()
for user in users:
    print(user)

users= db.query(User).filter(User.age>30).all()
for user in users:
    print(user)

users=db.query(User).filter(User.id==1).first()
if user:
    db.delete(user)
    db.commit()

users = db.query(User).filter_by(email="b@gmail.com").first()
if user:
    user.age = 27
    db.commit()

user=db.query(User).filter(User.name=="Bavithra").first()
print(user)

user=db.query(User).count()
print(count)
