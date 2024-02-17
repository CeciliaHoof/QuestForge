from config import app, migrate
from db_utils import *
from models import db
from cli_functionality.quest_board import view_quest_board
from cli_functionality.tavern import enter_tavern
from rich.console import Console
import os
import time

console = Console()

logo = '''
_______           _______  _______ _________ _______  _______  _______  _______  _______ 
(  ___  )|\     /|(  ____ \(  ____ \\__   __ /(  ____ \(  ___  )(  ____ )(  ____ \(  ____ \ 
| (   ) || )   ( || (    \/| (    \/   ) (   | (    \/| (   ) || (    )|| (    \/| (    \/
| |   | || |   | || (__    | (_____    | |   | (__    | |   | || (____)|| |      | (__   . 
| |   | || |   | ||  __)   (_____  )   | |   |  __)   | |   | ||     __)| | ____ |  __)  . 
| | /\| || |   | || (            ) |   | |   | (      | |   | || (\ (   | | \_  )| (     . 
| (_\ \ || (___) || (____/\/\____) |   | |   | )      | (___) || ) \ \__| (___) || (____/\ 
(____\/_)(_______)(_______/\_______)   )_(   |/       (_______)|/   \__/(_______)(_______/
'''

def display_welcome():
  console.print(logo, justify="center", style='bright_black', highlight=False)
  console.print(f"\n[bright_black]Welcome to QuestForge![/]\n\nStep into a world of fantasy and adventure. In QuestForge, face mythical challenges and forge your legacy as a legendary hero.\n\nTo start playing, visit the Tavern to hire your party of Adventures. Then head to the Quest Board to see which Quests you should assign to each Adventurer.\nKeep in mind, each Quest may only be tackled by one Adventurer.\n\nMay your Quests be daring, your victories legendary, and your Adventurers unforgettable.\n", justify="center")

def display_main_menu():
  console.print(f"\nMain Menu\n", style = 'b grey37')
  print("1. Enter Tavern")
  print("2. View Quest Board")
  print("3. Exit QuestForge")

def get_main_choice():
  return console.input(f"\n[b grey37]What is your choice? (1/2/3) [/]")

def display_exit_message():
  os.system('clear')
  console.print(logo, justify="center", style='bright_black', highlight=False)
  console.print('Thank you for playing QuestForge!\n\n', justify='center', style='b grey37')
  console.print('As you exit the mystical realms of QuestForge, remember the triumphs and challenges that shaped your Quests. May your legacy echo through the ages, and your Adventurers be forever remembered in the tales of fantasy. Until our paths cross again, farewell!\n\n\n\n', justify='center')

if __name__ == "__main__":
  with app.app_context():
    migrate.init_app(app, db)
    while True:
      os.system('clear')
      display_welcome()
      display_main_menu()
      choice = get_main_choice()
      if choice == "1":
        enter_tavern()
      elif choice == "2":
        view_quest_board()
      elif choice == '3':
        console.print(f"\n\nExiting QuestForge will delete all your Adventures and any progress you made on Quests. Are you sure you're ready to leave?\n\n", justify="center")
        print("1. Yes, it's time to leave.")
        print("2. No, I'll keep playing\n")
        exit_choice = console.input(f"\n[b grey37]What is your choice? (1/2) [/]")
        if exit_choice == '1':
          quests = get_all_quests()
          display_exit_message()
          exit_game(quests)
          break
        elif exit_choice == '2':
          display_main_menu()
        else:
          print("Invalid choice. Please enter 1 or 2. Returning to Main Menu.")
          time.sleep(2)
      else:
        print("Invalid choice. Please enter 1, 2, or 3.")