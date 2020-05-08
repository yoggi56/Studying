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

    def delete_record(self, key):
        self.db.pop(key)

    def clear_base(self):
        self.db.clear()


# Small self test
if __name__ == '__main__':
    bob = Person('Bob Smith', 44, 35000, 'software')
    sue = Person('Sue Jones', 47, 40000, 'hardware')
    tom = Manager(name='Tom Doe', age=50, pay=50000)

    pb = PeopleBase()
    pb.clear_base()
    pb.update_record('bob', bob)
    pb.update_record('tom', tom)
    pb.update_record('sue', sue)

    print("Finding sue:")
    pb.fetch_record('sue')
    print(pb.key, ' => ', pb.record.name, pb.record.age, pb.record.pay, pb.record.job)

    print("Database after deleting sue:")
    pb.delete_record('sue')
    for key in pb.db:
        pb.fetch_record(key)
        print(key, '=>', pb.record.name)
