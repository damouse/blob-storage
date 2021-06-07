import pymongo


class MongoTest:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client['test_db']

    def test(self):
        print(self.client.list_database_names())
        mycol = self.db["customers"]
        print(mycol)

    def seed(self):
        x = {"name": "John", "address": "Highway 37"}
        ret = self.db['users'].insert_one(x)
        print('Done, ret', ret.inserted_id)


def query(tester):
    x = tester.db['users'].find({'name': 'John'})

    for u in x:
        print(u)


if __name__ == '__main__':
    print('Hello, World!')
    # tester = MongoTest()
    # tester.seed()

    # query(tester)

    # TODO: create an index
    # Play with joins? That's a thing, right?
