from . import phonebookstorage


class PhoneBook():

    def __init__(self):
        self.my_storage = phonebookstorage.PhoneBookStorage()

    def phone_add_upd(self, phone_name, phone_number):
        self.my_storage.data[phone_name] = phone_number
        self.my_storage.save()

    def phone_get(self, phone_name=None):
        return self.my_storage.data[phone_name]

    def phone_exist(self, phone_name):
        if phone_name in self.my_storage.data:
            return True
        else:
            return False

    def phone_del(self, phone_name=None):
        if phone_name in self.storage_.phones:
            del self.my_storage.data[phone_name]
            self.my_storage.save()
