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
  elif welcome == "s":
    search()
  elif welcome == "u":
    update()

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

# Read
def search():
  input_title = input("Please enter the title note you are searching for: ")
  search_note = Notes.select().where(Notes.title == input_title)
  for note in search_note:
    print(note.title)
    print(note.date)
    print(note.body)
  more_options = input("Would you like to search for another note? [y/n]")
  if more_options == "y":
    search()
  elif more_options == "n":
    return
    
# Update
def update():
  update = input("If you would like to update a title, please type 'update-title', if you would like to update the date of a note please type 'update-date'")
  if update == "update-title":
    search_title = input("Please enter the title of the note you are attempting to update: ")
    edit_title = input("Please enter the new title of your note: ")
    print(f'edit_title: {edit_title}')
    update_title = Notes.get(Notes.title == search_title)
    print(f'update_title: {update_title}')
    update_title.title = edit_title
    update_title.save()
    print(f"Your title has been updated from {search_title} to {edit_title}")
  elif update == "update-date":
    search_date = input("Please enter the title of the note you are trying to update in order to edit the date: ")
    edit_date = input("Please enter the new date of your note: ")
    update_date = Notes.select(Notes.date == edit_date)
    update_date = edit_date
    update_date.save()
    print(f"Your date has been updated from {search_date} to {update_date}")
    more_updates = input("Would you like to update another note? [y/n] ")
    if more_updates == "y":
      update()
    elif more_updates == "n":
      return 

welcome()
