__all__ = ['PhoneBookGUI']

from . import phonebook


class PhoneBookGUI():
    phone_name = None
    phone_number = None
    operation_text = """
        операция: 
        \t \"a\" to add 
        \t \"d\" to delete 
        \t \"g\" to get 
        \t \"u\" to update 
        \t \"q\" to quit 
        
        """


    def __init__(self):
        self.phonebook_ = phonebook.PhoneBook()
        self.operations = {'a': self.phone_add,
                           'd': self.phone_del,
                           'u': self.phone_upd,
                           'g': self.phone_get,
                           'q': self.phones_exit}


    def print_help(self):
        self.print(self.operation_text)

    def print(self,text):
        print(text)

    def input(self,text):
        return input(text)

    def get_operation(self):
        self.print_help()
        input_operation = self.input('enter your choice:').strip()
        self.operation = self.operations.get(input_operation, self.print_help)
        self.operation()

    def phone_add(self):
        self.get_phone_name()
        if self.phonebook_.phone_exist(self.phone_name):
            self.print("Name Already Exist with value {}".format(self.phonebook_.my_storage.data[self.phone_name]))
            self.print_help()
        else:
            self.get_phone_number()
            self.phonebook_.phone_add_upd(self.phone_name, self.phone_number)
            self.print_help()

    def phone_get(self):
        self.get_phone_name()
        if self.phonebook_.phone_exist(self.phone_name):
            self.print(self.phonebook_.phone_get(self.phone_name))
            self.print_help()
        else:
            self.print("Sorry no such Name ")


    def phone_upd(self):
        self.get_phone_name()
        if self.phonebook_.phone_exist(self.phone_name):
            self.get_phone_number()
            self.phonebook_.phone_add_upd(self.phone_name, self.phone_number)
            self.print_help()
        else:
            self.print("Sorry no such Name ")
            self.print_help()

    def phone_del(self):
        self.get_phone_name()
        self.phonebook_.phone_del(self.phone_name)
        self.print_help()

    def get_phone_name(self):
        self.phone_name = self.input("Enter Contact Name")

    def get_phone_number(self):
        self.phone_number = self.input("Enter Contact Phone Number")

    @staticmethod
    def phones_exit():
        exit(0)
