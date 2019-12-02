from peewee import Model, CharField, DateField, PostgresqlDatabase
from datetime import date
import sys

db = PostgresqlDatabase('blackbook', user='postgres',
                        password='', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


class Person(BaseModel):
    name = CharField()
    birthday = DateField()
    phone = CharField()


db.connect()
db.create_tables([Person])

res = input(f"\n\nwould you like to create a new contact? (y / n) ")
if res == 'y':
    new_name = input("add a name: ")
    new_year = int(input("what year were they born? "))
    new_month = int(input("what month were they born? "))
    new_day = int(input("what day were they born? "))
    new_phone = int(input("what is their phone number? "))
    new_contact = Person(name=new_name, birthday=date(
        new_year, new_month, new_day), phone=new_phone)
    new_contact.save()  # new person is stored in the db
    print(
        f"\n\n\nYOUR NEW CONTACT HAS BEEN SAVED!\n{new_contact.name}\n{new_contact.birthday}\n{new_contact.phone}\n\n\n")
else:
    pass
res = input(f"\n\nwould you like to search by name? (y / n) ")
if res == 'y':
    search = input(f"\n\nsearch by name: ")
    output = Person.select().where(Person.name.contains(search)).get()
    print(f"\n{output.name}\n{output.phone}\n{output.birthday}\n")
else:
    pass
res = input(f"\n\nWould you like to view all of your contacts? (y / n) ")
if res == 'y':
    for person in Person.select():
        print(f"{person.name}\n{person.phone}\n{person.birthday}\n\n\n")
else:
    print(f"\n\nThank you for using your Little Black Book \n \n")
