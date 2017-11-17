import pymongo
from phonebookpkg.phonebook_engine_any import PhoneBookStorageEngineVirt

m = pymongo.MongoClient()


class DictMixer(dict):
    def __init__(self, *arg, **kw):
        super(DictMixer, self).__init__(*arg, **kw)

    def __getitem__(self, item):
        result = m.test.phone.find_one({'name':item})
        if result:
            return result['phone']
        else:
            return None
    def __setitem__(self, key, value):
        m.test.phone.insert_one({'name': key, 'phone': value})
    def __delitem__(self, item):
        m.test.phone.delete_one({'name': item})
    def __contains__(self, item):
        result = m.test.phone.find_one({'name':item})
        if result:
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



