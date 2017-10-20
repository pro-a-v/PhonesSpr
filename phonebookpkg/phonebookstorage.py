import json
import csv
import os.path
import configparser

class PhoneBookStorage():
    data = dict()
    current_type = 'json'

    def save_json(self):
        with open('data.json', 'w') as file_:
            json.dump(self.data, file_)
        return self

    def load_json(self):
        if os.path.isfile('data.json'):
            with open('data.json') as file_:
                self.data = json.load(file_)

    def save_csv(self):
        with open('data.csv', 'w') as file_:
            writer = csv.writer(file_, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
            for k in self.data.items():
                writer.writerow( k )
        return self

    def load_csv(self):
        if os.path.isfile('data.csv'):
            with open('data.csv', 'r+') as file_:
                reader = csv.reader(file_, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
                for row in reader:
                    self.data[row[0]]=row[1]

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        type_ = config['GLOBAL']['storage_engine']
        del config
        if type_ == 'csv':
            self.current_type = 'cvs'
            self.save = self.save_csv
            self.load_csv()
        else:
            self.save = self.save_json
            self.load_json()
