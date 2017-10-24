import configparser
from pydoc import locate

class PhoneBookStorage():
    current_type = 'json'

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        type_ = config['GLOBAL']['storage_engine']
        del config
        self.engine = locate('phonebookpkg.phonebook_engine_' + type_ + '.PhoneBookStorageEngine')()




