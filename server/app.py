from config import app, migrate
from db_utils import *
from models import db

#Tasks:
# Create Adventurer ✅
# Delete Adventurer (remove from db) ✅
#

def display_welcome():
  print("Welcome to QuestForge!")
  print("Ready to create your first adventurer and start questing?")

def display_main_menu():
  print("Main Menu")
  print("1. View Quest board")
  print("2. Enter the Tavern to view Adventurers")
  print("3. Exit QuestForge")

def get_main_choice():
  return input("What is your choice (1/2/3)?")

def display_all_quests():
  print("Welcome to the Quest board! From here you can view all quests or view quests based on difficulty")
  quests = get_all_quests()
  for quest in quests:
    print(f'{quest.title} \n {quest.description} \n Difficulty: {quest.difficulty} \n')

def display_all_adventurers():
  print("Welcome to the Tavern, where all of our adventures wait to be hired to a quest. From here you can hire an adventurer to assign them quests, or you can delete an delete an adventurer. \n Here are all of the adventurers:")
  adventurers = get_all_adventurers()
  if len(adventurers) == 0:
    print("Create some adventurers!")
  else:
    for adventurer in adventurers:
      print(f'{adventurer.name} \n Class: {adventurer.adventurer_class} \n Level: {adventurer.level} \n')
  adventurer_menu()
  adventurer_choice = get_adventurer_choice()
  if adventurer_choice == "1":
    hire_adventurer()
  elif adventurer_choice == "2":
    create_adventurer()
  elif adventurer_choice == "3":
    delete_adventurer()
  else:
    print("Invalid choice. Please inter 1, 2, or 3.")

def adventurer_menu():
  print("Adventure Menu")
  print("1. Hire an Adventurer (assign them to a quest)")
  print("2. Create a new Adventurer")
  print("3. Fire an Adventurer")

def get_adventurer_choice():
  return input("What is your choice (1/2/3)?")

def hire_adventurer():
  print("Here are your adventurers:")
  adventurers = get_all_adventurers()
  for adventure in adventurers:
    print(f'{adventure.id}: {adventure.name} \n')
  adventurer = input("Which Adventure would you like to hire (1/2/3...)?")
  print("Here are the quests that still need an adventurer:")
  quests = get_unassigned_quests()
  for quest in quests:
    print(f'{quest.id}: {quest.title} \n Difficulty: {quest.difficulty} \n')
  quest_hire = input("Which quest is this adventurer going to tackle? (1/2/3...)")
  assign_adventurer_to_quest(adventurer, quest_hire)

if __name__ == "__main__":
  with app.app_context():
    migrate.init_app(app, db)
    display_welcome()
    create_adventurer()
    while True:
      display_main_menu()
      choice = get_main_choice()
      if choice == "1":
        display_all_quests()
      elif choice == "2":
        display_all_adventurers()
      elif choice == '3':
        print("Thanks for playing QuestForge")
        break
      else:
        print("Invalid choice. Please inter 1, 2, or 3.")
    #create_adventurer()

    # remove pass and write your cli logic
