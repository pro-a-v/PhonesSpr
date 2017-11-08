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
    def __setitem__(self, k, v):
        return super(DictMixer, self).__setitem__(k, v)
    def __delitem__(self, k):
        return super(DictMixer, self).__delitem__(k)
    def __contains__(self, item):
        result = conn.execute(text('select 1 from students where name like :name'), {'name': item}).fetchone()
        if result[0] == 1:
            return True
        else:
            return False
    def update(self, mapping=(), **kwargs):
        super(DictMixer, self).update(self._process_args(mapping, **kwargs))






class PhoneBookStorageEngine(PhoneBookStorageEngineVirt):
    data = DictMixer()

    def save(self):
        pass

    def load(self):
        pass

    def __init__(self):
        self.load()



