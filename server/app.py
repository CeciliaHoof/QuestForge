from config import app, migrate
from db_utils import *
from models import db
from cli_functionality.quest import *
from cli_functionality.adventurer import *

def display_welcome():
  print("Welcome to QuestForge!")

def display_main_menu():
  print("Main Menu")
  print("1. View Quest Board")
  print("2. Enter Tavern")
  print("3. Exit QuestForge")

def get_main_choice():
  return input("What is your choice? (1/2/3) ")
  
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
