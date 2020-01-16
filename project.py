from peewee import *
from datetime import date

db = PostgresqlDatabase('notes', user='postgres', password='', host='localhost', port='5432')

class BaseModel(Model):
  class Meta:
        database = db

class Notes(BaseModel):
  title = CharField()
  date = DateField()
  body = CharField()


db.connect()
 
def welcome():
  welcome = input("To create a new note please press [c]. To Search for an existing note press [s]. To update a note press [u]. To delete an existing note press [d].")
  if welcome == "c":
    create()
  # elif welcome == "s":
  #   search()

# Create
def create():
  # if welcome == "c":
    new_note = Notes(title = "New note", date =date(2019, 1, 16), body = "this is my new notes" )
    new_note.save()
    print(f"Success! Your new note titled {new_note.title} was created!")
  # elif welcome():
welcome()



# Read 
# if welcome == "s"