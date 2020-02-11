from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean, Date, DateTime, func, exists
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# engine = create_engine('postgresql://gestaoprocesso:gestaoprocesso123@localhost:5432/gestaoprocesso', convert_unicode=True)
engine = create_engine('sqlite:///banco.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    nome = Column(String(255))

    def __repr__(self):
        return self.nome

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()
