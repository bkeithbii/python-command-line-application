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
  print("Please enter your new note: ")
  new_title = input("Enter Title: ")
  new_date = input("Please enter date - year,month,date: ")
  new_body = input("Please enter your note: ") 
    
  new_note = Notes(title = new_title, date = new_date, body= new_body)
  new_note.save()
  print(f"Success! Your new note titled {new_note.title} was created!")
  success = input("Would you like to add another note? [y/n]")
  if success == "y":
    create()
  elif success == "n":
    return
    
welcome()

# Read 

# if welcome == "s"