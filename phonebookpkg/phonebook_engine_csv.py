import csv
import os.path

class PhoneBookStorageEngine():
    data = dict()

    def save(self):
        with open('data.csv', 'w') as file_:
            writer = csv.writer(file_, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
            for k in self.data.items():
                writer.writerow(k)
        return self

    def load(self):
        if os.path.isfile('data.csv'):
            with open('data.csv', 'r+') as file_:
                reader = csv.reader(file_, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
                for row in reader:
                    self.data[row[0]] = row[1]

    def __init__(self):
        self.load()

