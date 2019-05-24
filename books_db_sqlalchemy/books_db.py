import config
from sqlalchemy.ext.declarative import declarative_base

engine = db.create_engine('postgresql+psycopg2://{}:{}@localhost/Library'.format(config.pg_user,config.pg_pw))
connection = engine.connect()

metadata = db.MetaData()
books = db.Table('books', metadata,
db.Column('Id', db.Integer(), primary_key=True, unique=True),
db.Column('Title', db.String(255), nullable=False))

books.create(engine)

Base = declarative_base()

class Author(Base):
    __tablename__ = 'author'
    Id = db.Column(db.Integer(), primary_key=True, unique=True)
    Title = db.Column(db.String(255), nullable = False)

Base.metadata.create_all(engine)