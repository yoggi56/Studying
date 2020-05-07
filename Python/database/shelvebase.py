import shelve
from person import Person, Manager


class PeopleBase:

    def __init__(self):
        self.db = shelve.open('people_base')
        self.record = Person()
        self.key = ''

    def __del__(self):
        self.db.close()

    def fetch_record(self, key):
        try:
            self.record = self.db[key]    # извлечь запись по ключу, отобразить в форме
            self.key = key
        except:
            return False
        else:
            return True

    def update_record(self, key, cur_record):
        self.db[key] = cur_record


# Small self test
if __name__ == '__main__':
    bob = Person('Bob Smith', 44, 35000, 'software')
    sue = Person('Sue Jones', 47, 40000, 'hardware')
    tom = Manager(name='Tom Doe', age=50, pay=50000)

    pb = PeopleBase()
    pb.update_record('bob', bob)
    pb.update_record('tom', tom)
    pb.update_record('sue', sue)

    pb.fetch_record('bob')
    print(pb.key, ' => ', pb.record.name, pb.record.age, pb.record.pay, pb.record.job)
