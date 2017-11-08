from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from phonebookpkg.phonebook_engine_any import PhoneBookStorageEngineVirt

Base = declarative_base()
engine = create_engine("mysql+pymysql://root@localhost/test?charset=utf8mb4", isolation_level="AUTOCOMMIT")
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
conn = Session()

class Person(Base):
    __tablename__ = 'students'
    query = Session.query_property()
    name = Column(String(25), primary_key=True)
    phone = Column(String(25), nullable=False)


class DictMixer(dict):
    def __init__(self, *arg, **kw):
        super(DictMixer, self).__init__(*arg, **kw)

    def __getitem__(self, item):
        return conn.execute(text('select phone from students where name like :name'), {'name': item}).fetchone()[0]
    def __setitem__(self, key, value):
        result = conn.execute(text('select 1 from students where name like :key'), {'key': key}).fetchone()
        if result is not None:
            conn.execute(text('update students set phone = :value where name like :key'),{'key': key, 'value': value})
        else:
            conn.execute(text('insert into students (name,phone) values(:key , :value)'),{'key': key, 'value': value})
    def __delitem__(self, item):
        conn.execute(text('delete from students where name like :name'), {'name': item})
    def __contains__(self, item):
        result = conn.execute(text('select 1 from students where name like :name'), {'name': item}).fetchone()
        if result is not None:
            return True
        else:
            return False







class PhoneBookStorageEngine(PhoneBookStorageEngineVirt):
    data = DictMixer()

    def save(self):
        pass

    def load(self):
        pass

    def __init__(self):
        self.load()



