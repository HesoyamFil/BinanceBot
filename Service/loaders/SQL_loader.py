from Load_router import Loader

class SQL_Loader(Loader):

    def __init__(self, bucket_name):
        self.bucket_name = bucket_name

    def load(self, bucket_name):
        pass

    def update(self, bucket_name):
        pass
