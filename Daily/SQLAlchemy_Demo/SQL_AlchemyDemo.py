from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Define the database
DATABASE_URL = "sqlite:///example.db"
engine = create_engine(DATABASE_URL, echo = True)   
Base = declarative_base()
SessionLocal = sessionmaker(bind = engine)

#define a simple ORM Model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String, nullable = False)
    age = Column(Integer, nullable = False)

#Create the database and tables
Base.metadata.create_all(engine)

#Create a new session
session = SessionLocal()

#Create
new_user = User(name = 'Sam', age = 1000)
session.add(new_user)
session.commit()

#Update
user_to_update = session.query(User).filter_by(name = 'Sam').first()
if(user_to_update):
    user_to_update.age = 50
    session.commit()

#Delete
user_to_update = session.query(User).filter_by(name = 'Sam').first()
if(user_to_update):
    session.delete(user_to_update)
    session.commit()

#Read
users = session.query(User).all()
print("All users")
for user in users:
    print(user.id, user.name, user.age)

session.close()