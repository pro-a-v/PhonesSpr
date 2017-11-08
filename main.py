import phonebookpkg
from GUIWrapper import Wrapper


if __name__ == "__main__":

    PhoneBookGUI_ = Wrapper(phonebookpkg.PhoneBookGUI, 'console')

    while True:
        PhoneBookGUI_.get_operation()
