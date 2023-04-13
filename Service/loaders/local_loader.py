from Load_router import Loader

class local_loader(Loader):

    def __init__(self, connection_string):
        self.connection_string = connection_string

    def load(self, connection_string):
        pass

    def update(self, connection_string):
        pass