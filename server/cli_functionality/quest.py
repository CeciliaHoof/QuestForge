from db_utils import *
from .adventurer import attempt_quest

def view_quest_board():
  print("Welcome to the Quest board!")
  quests = get_all_quests()
  for quest in quests:
    print(f'{quest.id} | {quest.title}\n')
  display_quest_menu()
  
def display_quest_menu():
  print("Quest Menu")
  print("1. View Quest Details")
  print("2. View Quests by Type")
  print("3. View Failed Quests")
  print("4. View Completed Quests")
  print("5. Return to Main Menu")
  handle_quest_choice()

def handle_quest_choice():
  choice = input("What is your choice? (1/2/3/4/5) ")
  if choice == "1":
    view_quest()
  elif choice == "2":
    display_quests_by_type()
  elif choice == "3":
    display_failed_quests()
  elif choice == '4':
    display_completed_quests()
  elif choice == "5":
    return
  else:
    print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
    view_quest_board()

def view_quest():
  quest_id = input("Which quest do you want to see? (1/2/3...) ")
  quest = get_quest_by_id(quest_id)
  if quest == None:
    print("Invalid quest. Please check your input")
  else:
    print(f"\n{quest.title} \n Description: {quest.description} \n Difficulty: {quest.difficulty} \n Adventurer: {quest.adventurer}\n Type: {quest.quest_type} \n Status: {quest.status}")
  display_quest_submenu()

def display_quests_by_type():
  choice = input("Which quests do you want to see? (Magic/Stealth/Strength) ")
  type_display = choice.title()
  quests = get_quests_by_type(choice)
  if quests:
    print(f'\n{type_display} Quests')
    for quest in quests:
        print(f"\n{quest.title} \n Description: {quest.description} \n Difficulty: {quest.difficulty} \n Adventurer: {quest.adventurer}")
  else:
      print("Invalid type. Please check your input")
  display_quest_submenu()

def display_failed_quests():
  quests = [quest for quest in get_all_quests() if quest.status == "Failed"]
  if len(quests) == 0:
    print("\nAll Quests are currently unattempted or completed.")
    display_quest_submenu()
  else:
    print("\nFailed Quests")
    for quest in quests:
      print(f"\n{quest.title} \n Description: {quest.description} \n Difficulty: {quest.difficulty} \n Adventurer: {quest.adventurer}")
    display_questing_menu()

def embark_on_quest():
  quests = [quest for quest in get_all_quests() if quest.status == "Failed"]
  if len(quests) == 0:
    print("\nAll Quests are currently unattempted or completed.")
    display_quest_submenu()
  else:
    for q in quests:
      print(f"\n{q.id} | {q.title}\n Difficulty: {q.difficulty} | Adventurer: {q.adventurer}\n")
    q_id = input("Which Quest do you want to attempt? (Enter the number next to the Quest title) ")
    quest = get_quest_by_id(q_id)
    if quest is None or quest not in quests:
      print("Invalid Quest. Please check your input.")
    else:
      adventurer = get_adventurer_by_id(quest.adventurer_id)
      attempt_quest(adventurer, quest)
    display_questing_menu()

def display_completed_quests():
  quests = [quest for quest in get_all_quests() if quest.status == "Complete"]
  if len(quests) == 0:
    print("\nNo Quests have been completed! Navigate to Tavern to hire Adventurers.")
  else:
    print("\nCompleted Quests")
    for quest in quests:
      print(f"\n{quest.title} \n Description: {quest.description} \n Difficulty: {quest.difficulty} \n Adventurer: {quest.adventurer}\n Type: {quest.quest_type}")
  display_quest_submenu()

def display_quest_submenu():
  print('\n')
  print('1. Return to Quest Board')
  print('2. Return to Main Menu')
  choice = input("Where would you like to go now? (1/2) ")
  handle_quest_submenu(choice)

def handle_quest_submenu(choice):
  if choice == '1':
    view_quest_board()
  elif choice == '2':
    return
  else:
    print("Invalid choice. Please enter 1 or 2.")
    view_quest_board()

def display_questing_menu():
  print('\n')
  print('1. Embark on Quest')
  print('2. Return to Quest Board')
  choice = input("What would you like to do now? (1/2) ")
  handle_questing_menu(choice)

def handle_questing_menu(choice):
  if choice == '1':
    embark_on_quest()
  elif choice == '2':
    view_quest_board()
  else:
    print("Invalid choice. Please enter 1 or 2.")
    view_quest_board()