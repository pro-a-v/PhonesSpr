from phonebook import PhoneBook


class PhoneBookGUI(PhoneBook):
    phone_name = None
    phone_number = None

    def __init__(self, PhoneBook_):
        self.phonebook_ = PhoneBook_
        self.operations = {'a': self.phone_add,
                           'd': self.phone_del,
                           'u': self.phone_upd,
                           'g': self.phone_get,
                           'q': self.phones_exit}
        self.print_help()

    def print_help(self):
        print("""
        операция: 
        \t \"a\" to add 
        \t \"d\" to delete 
        \t \"g\" to get 
        \t \"u\" to update 
        \t \"q\" to quit """)

    def get_operation(self):
        input_operation = input()
        self.operation = self.operations.get(input_operation, self.print_help)
        self.operation()

    def phone_add(self):
        self.get_phone_name()
        if self.phonebook_.phone_exist(self.phone_name):
            print("Name Already Exist with value {}".format(self.phonebook_.my_storage.data[self.phone_name]))
            if input("Are you whant to update it? (Yes = \"y\")") == 'y':
                self.get_phone_number()
                self.phonebook_.phone_add_upd(self.phone_name, self.phone_number)
                self.print_help()
        else:
            self.get_phone_number()
            self.phonebook_.phone_add_upd(self.phone_name, self.phone_number)
            self.print_help()

    def phone_get(self):
        self.get_phone_name()
        if self.phonebook_.phone_exist(self.phone_name):
            print(self.phonebook_.phone_get(self.phone_name))
            self.print_help()
        else:
            if input("Sorry no such Name \n Whant to add? (Yes = \"y\")") == 'y':
                self.get_phone_number()
                self.phonebook_.phone_add_upd(self.phone_name, self.phone_number)
                self.print_help()


    def phone_upd(self):
        self.get_phone_name()
        if self.phonebook_.phone_exist(self.phone_name):
            self.get_phone_number()
            self.phonebook_.phone_add_upd(self.phone_name, self.phone_number)
            self.print_help()
        else:
            if input("Sorry no such Name \n Whant to add? (Yes = \"y\")") == 'y':
                self.get_phone_number()
                self.phonebook_.phone_add_upd(self.phone_name, self.phone_number)
                self.print_help()

    def phone_del(self):
        self.get_phone_name()
        self.phonebook_.phone_del(self.phone_name)
        self.print_help()

    def get_phone_name(self):
        self.phone_name = input("Enter Contact Name")

    def get_phone_number(self):
        self.phone_number = input("Enter Contact Phone Number")

    def phones_exit(self):
        exit(0)
