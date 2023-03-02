from sqlalchemy import create_engine, Column, Integer, Double, String
from sqlalchemy.orm import sessionmaker, declarative_base

sqlite_filepath = r'alchemy.db'
db_path = f"sqlite:///{sqlite_filepath}"
print(db_path)

# Create engine and session
engine = create_engine(db_path)
Session = sessionmaker(engine)
session = Session()


Base = declarative_base()  # creates the Base class, which is what all models inherit from and how they get SQLAlchemy ORM functionality


class User(Base):

    __tablename__ = 'Users'

    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    salary = Column(Double)

    def __str__(self):
        return f"User: {self.name}\nage: {self.age}\nsalary: {self.salary}"

    def __repr__(self):
        return f"User(name={self.name}, age={self.age}, salary={self.salary})"


Base.metadata.create_all(engine)


# results = session.query(User).all()
# print(results)

# users = [User(name='John Smith', age=34, salary=534.23),
#          User(name='Anna Smith', age=23, salary=3434.23),
#          User(name='Andrew Gimli', age=21, salary=4534.23),
#          User(name='Aragorn Aratornovich', age=54, salary=4574.3),
#          ]
# session.add_all(users)
#
# # for user in users:
# #     session.add(user)
# session.commit()

# results = session.query(User).all()
# print(results)
# u = results[0]
# print(u.name)
# print()
#
#
#
#
from sqlalchemy import select
# stmt = select(User).where(User.name == "John Smith")
# result = session.execute(stmt)
# print(result.fetchall())
#
# print()
# stmt = select(User).where(User.name == "John Smith").limit(1)
# result = session.execute(stmt)
# print(result.fetchall())
#
# print()
# stmt = select(User).where(User.name == "John Smith").order_by(User.age)
# result = session.execute(stmt)
# print(result.fetchall())
#
# print()
stmt = select(User.name).limit(3)
result = session.execute(stmt)
print(result.fetchall())
