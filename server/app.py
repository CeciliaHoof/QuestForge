from config import app, migrate
from db_utils import *
from models import db

def display_welcome():
  print("Welcome to QuestForge!")

def display_main_menu():
  print("Main Menu")
  print("1. View Quest board")
  print("2. Enter the Tavern to view Adventurers")
  print("3. Exit QuestForge")

def get_main_choice():
  return input("What is your choice (1/2/3)? ")

def display_all_quests():
  print("Welcome to the Quest board! From here you can view all quests or view quests based on difficulty")
  quests = get_all_quests()
  for quest in quests:
    print(f'{quest.title} \n {quest.description} \n Difficulty: {quest.difficulty} \n')

def display_all_adventurers():
  adventurers = get_all_adventurers()
  if len(adventurers) == 0:
    print("There are currently no adventures waiting for a quest! Create some adventurers! \n")
  else:
    for adventurer in adventurers:
      print(f'{adventurer.id} | {adventurer.name} \n')

def enter_tavern():
  print("Welcome to the Tavern, where all of our adventures wait to be hired to a quest. From here you can hire an adventurer to assign them quests, or you can delete an delete an adventurer. \n Here are all of the adventurers: \n")
  display_all_adventurers()
  display_adventurer_menu()

def display_adventurer_menu():
  if len(get_all_adventurers()) == 0:
    print("Adventure Menu")
    print("1. Create an Adventurer")
    print("2. Return to Main Menu")
    adventurer_choice = input("What is your choice (1/2)? ")
  else:
    print("Adventure Menu")
    print("1. Create an Adventurer")
    print("2. Hire an Adventurer")
    print("3. View Adventurer Details")
    print("4. Fire an Adventurer")
    print("5. Return to Main Menu")
    adventurer_choice = input("What is your choice (1/2/3/4/5)? ")
  handle_adventurer_choice(adventurer_choice)

def handle_adventurer_choice(choice):
  if choice == "1":
    create_adventurer()
    enter_tavern()
  elif choice == "2":
    hire_adventurer()
  elif choice == "3":
    adventurer = input("Which adventurer do you want to see? ")
    view_adventurer(adventurer)
  elif choice == "4":
    delete_adventurer()
    enter_tavern()
  elif choice == "5":
    return
  else:
    print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

def view_adventurer(adventurer):
  get_adventurer_details(adventurer)
  print('1. Return to Tavern')
  print('2. Return to Main Menu')
  choice = input("Where would you like to go now? (1/2)? ")
  if choice == '1':
    enter_tavern()
  elif choice == '2':
    return
  else:
    print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

def hire_adventurer():
  print("Here are your adventurers:\n")
  display_all_adventurers()
  adventurer = input("Which Adventure would you like to hire (1/2/3...)?")
  print("Here are the quests that still need an adventurer:")
  quests = get_unassigned_quests()
  for quest in quests:
    print(f'{quest.id}: {quest.title} \n Difficulty: {quest.difficulty} \n')
  quest_hire = input("Which quest is this adventurer going to tackle? (1/2/3...)")
  assign_adventurer_to_quest(adventurer, quest_hire)
  display_hire_menu()
  

def display_hire_menu():
  print("Hire Menu")
  print("1. Keep Hiring Adventurers")
  print("2. Return to Tavern")
  hire_choice = input("What is your choice (1/2)? ")
  handle_hire_choice(hire_choice)

def handle_hire_choice(choice):
  if choice == "1":
    hire_adventurer()
  elif choice == "2":
    enter_tavern()
  else:
    print("Invalid input, please enter 1 or 2.")
  
if __name__ == "__main__":
  with app.app_context():
    migrate.init_app(app, db)
    display_welcome()
    while True:
      display_main_menu()
      choice = get_main_choice()
      if choice == "1":
        display_all_quests()
      elif choice == "2":
        enter_tavern()
      elif choice == '3':
        print("Thanks for playing QuestForge")
        break
      else:
        print("Invalid choice. Please inter 1, 2, or 3.")
