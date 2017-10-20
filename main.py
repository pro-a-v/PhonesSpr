

from phonebook import PhoneBook
from phonebookstorage import PhoneBookStorage
from phonebookgui import PhoneBookGUI


if __name__ == "__main__":
    #PhoneBook_ = PhoneBook()
    PhoneBookGUI_ = PhoneBookGUI()

    while True:
        PhoneBookGUI_.get_operation()
