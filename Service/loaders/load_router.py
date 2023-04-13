from abc import ABC, abstractmethod

class Loader(ABC):

    @abstractmethod
    def load(self, data, table_name, index=None):
        pass

    @abstractmethod
    def update(self, data, table_name, index=None):
        pass