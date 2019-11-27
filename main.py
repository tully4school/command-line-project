from peewee imoport *
from datetime import date
import sys

db = PostgresqlDatabase('people', user='postgres',
                        password='', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


class Person(BaseModel):
    name = CharField()
    birthday = DateField()
    phone = CharField()


db.connect()

res = input("would you like to create a new contact? (y / n)")
if res == 'y':
    new_name = input("add a name: ")
    new_year = int(input("what year were they born? "))
    new_month = int(input("what month were they born? "))
    new_day = int(input("what day were they born? "))
    new_phone = int(input("what is their phone number? "))
    new_contact = Person(name=new_name, birthday=date(new_year, new_month, new_day) phone=new_phone)
    new_contact.save()  # new person is stored in the db
    else:
        pass

res = input("would you like to search by name? (y / n)")
if res == y:
    search = input("search by name: ")
    output = Person.select().where(Person.name == search).get()
    print(output.name)
    print(output.phone)
    print(output.birthday)
    else:
        pass
