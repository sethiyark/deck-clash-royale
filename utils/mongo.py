from pymongo import MongoClient


class MongoUtils:
    def __init__(self, db_name):
        self.__client = MongoClient()
        self.__db_name = self.__client[db_name]

    def insert(self, collection, document):
        if type(document).__name__ == 'dict':
            self.__db_name[collection].insert(document)
        else:
            print('Can insert only one document')

    def insert_many(self, collection, documents):
        try:
            self.__db_name[collection].insert_many(documents)
        except Exception as e:
            print(e, 'While Inserting')
