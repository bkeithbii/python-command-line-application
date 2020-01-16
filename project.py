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
 

welcome = input("To create a new note please press c. To Search for an existing note press s. To update a note press u. To delete an existing note press s.")

# Create
if welcome == "c"
    new_note = Notes.get(title = " ", date =(), body = " " )
    new_note.save()

# Read 
if welcome is == "s"
    