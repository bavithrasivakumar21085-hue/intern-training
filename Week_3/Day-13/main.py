from database import engine, Session, Base
from models import User,Post

Base.metadata.create_all(bind=engine)
session=Session()

user1=User(name='Bavithra',email='b@gmail.com',age=25)
user2=User(name='Keerthi', email= 'K@email.com',age=28)
user3=User(name='Ramya',email='r@gmail.com',age=22)
user4=User(name='Payal',email='p@gmail.com',age=25)


session.add(user1)
session.add(user2)
session.add(user3)
session.add(user4)
session.commit()

post1= Post(user_id=1,product= 'python book')
post2= Post(user_id=2,product= 'Sql Book')
post3=Post(user_id=4,product='postgres book')

session.add(post1)
session.add(post2)
session.add(post3)
session.commit()


users= session.query(User).all()
for user in users:
    print(user)

user= session.query(User.id,User.name).all()
for user in users():
    print(user.id,user.name)


user= session.query(User).order_by(User.age).all()
for user in users:
    print(user)
    
user= session.query(User).filter(User.age>30).all()
for user in users:
    print(user)

user=session.query(user).filter(User.id==1).first()
session.delete(user)
session.commit()

user = session.query(User).filter_by(email="b@gmail.com").first()

if user:
    user.age = 27
    session.commit()


