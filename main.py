
import configparser
from phonebook import PhoneBook
from phonebookstorage import PhoneBookStorage
from phonebookgui import PhoneBookGUI





if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config.ini')
    storage_ = PhoneBookStorage(config['GLOBAL']['storage_engine'])
    del config

    PhoneBook_ = PhoneBook(storage_)
    PhoneBookGUI_ = PhoneBookGUI(PhoneBook_)

    while True:

        PhoneBookGUI_.get_operation()
