import redis
from phonebookpkg.phonebook_engine_any import PhoneBookStorageEngineVirt

r = redis.Redis(host='localhost', port=6379, db=0)


class DictMixer(dict):
    def __init__(self, *arg, **kw):
        super(DictMixer, self).__init__(*arg, **kw)

    def __getitem__(self, item):
        return r.get(item)
    def __setitem__(self, key, value):
        r.set(key, value)
    def __delitem__(self, item):
        r.delete(item)
    def __contains__(self, item):
        result = r.get(item)
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



