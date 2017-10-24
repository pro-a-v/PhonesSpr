import json
import os.path



class PhoneBookStorageEngine():
    data = dict()
    current_type = 'json'

    def save(self):
        with open('data.json', 'w') as file_:
            json.dump(self.data, file_)
        return self

    def load(self):
        if os.path.isfile('data.json'):
            with open('data.json') as file_:
                self.data = json.load(file_)

    def __init__(self):
        self.load()

