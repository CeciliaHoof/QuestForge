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

def view_quest_board():
  print("Welcome to the Quest board!")
  quests = get_all_quests()
  for quest in quests:
    print(f'{quest.id} | {quest.title}')
  print('\n')
  display_quest_menu()
  
def display_quest_menu():
  print("Quest Menu")
  print("1. View Quest Details")
  print("2. View Quests by Difficulty")
  print("3. Return to Main Menu")
  quest_choice = input("What is your choice (1/2/3)? ")
  handle_quest_choice(quest_choice)

def handle_quest_choice(choice):
  if choice == "1":
    quest_id = input("Which quest do you want to see? ")
    view_quest(quest_id)
  elif choice == "2":
    choice = input("Which quests do you want to see (Easy/Medium/Hard)? ")
    get_quests_by_difficulty(choice)
    display_quest_submenu()
  elif choice == "3":
    return
  else:
    print("Invalid choice. Please enter 1, 2, or 3.")
    view_quest_board()

def view_quest(quest):
  get_quest_details(quest)
  display_quest_submenu()

def display_quest_submenu():
  print('\n')
  print('1. Return to Quest Board')
  print('2. Return to Main Menu')
  choice = input("Where would you like to go now? (1/2)? ")
  handle_quest_submenu(choice)

def handle_quest_submenu(choice):
  if choice == '1':
    view_quest_board()
  elif choice == '2':
    return
  else:
    print("Invalid choice. Please enter 1 or 2.")

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
    print("Adventurer Menu")
    print("1. Create an Adventurer")
    print("2. Return to Main Menu")
    choice = input("What is your choice (1/2)? ")
    if choice == "1":
      handle_adventurer_choice(choice)
    elif choice == "2":
      return
    else:
      print("Invalid choice. Please enter 1 or 2.")
  else:
    print("Adventurer Menu")
    print("1. Create an Adventurer")
    print("2. Hire an Adventurer")
    print("3. View Adventurer Details")
    print("4. Fire an Adventurer")
    print("5. Return to Main Menu")
    adventurer_choice = input("What is your choice (1/2/3/4/5)? ")
    handle_adventurer_choice(adventurer_choice)

def handle_adventurer_choice(choice):
  if choice == "1":
    name = input("Enter the name of the adventurer: ")
    adventurer_class = input("Enter the class of the adventurer (warrior, mage, rogue): ")
    create_adventurer(name, adventurer_class)
    enter_tavern()
  elif choice == "2":
    hire_adventurer()
  elif choice == "3":
    adventurer = input("Which adventurer do you want to see? ")
    view_adventurer(adventurer)
  elif choice == "4":
    id = input("Which adventurer would you like to fire (1/2/3...)? ")
    delete_adventurer(id)
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
  adventurer = input("Which Adventure would you like to hire (1/2/3...)? ")
  print("Here are the quests that still need an adventurer:")
  quests = get_unassigned_quests()
  for quest in quests:
    print(f'{quest.id}: {quest.title} \n Difficulty: {quest.difficulty} \n')
  quest_hire = input("Which quest is this adventurer going to tackle? (1/2/3...)? ")
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
        view_quest_board()
      elif choice == "2":
        enter_tavern()
      elif choice == '3':
        print("Thanks for playing QuestForge")
        break
      else:
        print("Invalid choice. Please inter 1, 2, or 3.")
