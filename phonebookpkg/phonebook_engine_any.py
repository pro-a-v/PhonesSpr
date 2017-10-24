from abc import ABCMeta, abstractmethod


class PhoneBookStorageEngineVirt(metaclass=ABCMeta):
    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def save(self):
        pass


