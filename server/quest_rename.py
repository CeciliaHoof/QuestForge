from db_utils import *
from rich.console import Console
import os
import time
import random

console = Console()

def view_quest_board():
  os.system('clear')
  console.print(f"\n____________________________________________\n /                                             \ \n|                  Quest Board                  |\n|_______________________________________________|\n|   .---------.    .---------.    .---------.   |\n|  |   QUEST   |  |   QUEST   |  |   QUEST   |  |\n|  |-----------|  |-----------|  |-----------|  |\n|  |  Seeking  |  |   Do you  |  |  Stealth  |  |\n|  | hero with |  |  have the |  |   expert  |  |\n|  |  certain  |  |  strength |  |   needed. |  |\n|  |   magic   |  |   of ten  |  |    TOP    |  |\n|  |  powers.  |  |    men?   |  |  SECRET!  |  |\n|   -----------    -----------    -----------   |\n|                                               |\n|              Discover quests and              |\n|                become a legend!               |\n \_____________________________________________/ \n", justify='center', highlight=False)
  console.print(f"\nWelcome to the Quest Board!\n", justify='center', style='b medium_purple4')
  console.print(f"\nGreetings, brave Adventurers! The Quest Board awaits your courage, offering challenges for heroes seeking glory and legendary tales.\n\nExplore the fliers on the board, each describing a unique quest awaiting a hero with specific skills.\nQuests that are complete have been crossed off, but you can still view their details.", justify='center')
  quests = get_all_quests()
  completed_quests = [q for q in quests if q.status == 'Complete']
  if len(completed_quests) == 12:
    console.print(f'\n\nCongratulations!\n\n', justify='center', style='b medium_purple4')
    console.print(f'Your Adventurers have successfully completed all Quests! You can still explore Quest details.', justify='center')
  console.print(f'\nQuest Fliers\n', style = 'b medium_purple4')
  for quest in quests:
    if quest.status == 'Complete':
      console.print(f'{quest.id} | [s]{quest.title}[/]\n', highlight=False)
    else:
      print(f'{quest.id} | {quest.title}\n')
  display_quest_menu()

def display_quest_menu():
  quests = get_all_quests()
  completed_quests = [q for q in quests if q.status == 'Complete']
  console.print(f"\nQuest Menu\n", style='b medium_purple4')
  if len(completed_quests) == 12:
    print("1. View Quest Details")
    print("2. View Quests by Type")
    print("3. Return to Main Menu")
    choice = console.input("\n\n[b medium_purple4]What is your choice? (1/2/3) [/]")
    if choice == '1' or choice == '2':
      handle_quest_choice(choice)
    elif choice == '3':
      handle_quest_choice('4')
    else:
      print("\nInvalid choice. Please enter 1, 2, or 3.\n")
      time.sleep(2)
      view_quest_board()
  else:  
    print("1. View Quest Details")
    print("2. View Quests by Type")
    print('3. Embark on Quest')
    print("4. Return to Main Menu")
    choice = console.input("\n\n[b medium_purple4]What is your choice? (1/2/3/4) [/]")
    handle_quest_choice(choice)

def handle_quest_choice(choice):
  if choice == "1":
    view_quest()
  elif choice == "2":
    display_quests_by_type()
  elif choice == "3":
    embark_on_quest()
  elif choice == "4":
    return
  else:
    print("\nInvalid choice. Please enter 1, 2, 3, or 4.\n")
    display_quest_submenu()

def display_quest_details(quest):
  console.print(f'{quest.title}', style = 'b')
  print(f"\n Description: {quest.description} \n Difficulty: {quest.difficulty}\n Type: {quest.quest_type} \n Adventurer: {quest.adventurer} \n Status: {quest.status}\n")

def view_quest():
  quest_id = input("\nWhich quest do you want to see? (1/2/3...) ")
  quest = get_quest_by_id(quest_id)
  if quest == None:
    print(f"\nInvalid Quest. Please check your input.\n")
    time.sleep(1)
  else:
    os.system('clear')
    console.print(f"\nQuest Details\n", justify='center', style='b medium_purple4')
    display_quest_details(quest)
  display_quest_submenu()

def display_quests_by_type():
  choice = input("\nWhich Quests do you want to see? (Magic/Stealth/Strength) ")
  type_display = choice.title()
  quests = get_quests_by_type(choice)
  if quests:
    os.system('clear')
    console.print(f'\n{type_display} Quests\n', justify='center', style='b medium_purple4')
    for quest in quests:
        display_quest_details(quest)
  else:
      print("\nInvalid type. Please check your input\n")
  display_quest_submenu()

def embark_on_quest():
  os.system('clear')
  console.print(f'\nEmbark on a Quest\n', justify='center', style = 'b medium_purple4')
  console.print(f"\nThis is where you need to make strategic decisions.\nSelect a Quest from the list below and entrust it to one of your skilled adventurers.\n\nChoose wisely, and may your heroes return victorious!\n", justify='center')
  quests = get_all_quests()
  console.print(f'\nQuest Fliers\n', style = 'b medium_purple4')
  for quest in quests:
    if quest.status == 'Complete':
      console.print(f'{quest.id} | [s]{quest.title} | {quest.difficulty}[/]\n', highlight=False)
    else:
      print(f'{quest.id} | {quest.title} | {quest.difficulty}\n')
  q_id = input(f"\nWhich Quest do you want to attempt? (1/2/3...) ")
  q_choice = get_quest_by_id(q_id)
  party = get_all_adventurers()
  if q_choice == None:
    print(f"\nInvalid Quest. Please check your input.\n")
  else:
    os.system('clear')
    console.print(f'\nQuest Details\n', style = 'b medium_purple4')
    display_quest_details(q_choice)
    if q_choice.status == 'Complete':
      print(f'{q_choice.title} is already complete!')
    elif q_choice.adventurer:
      print(f"\n{q_choice.adventurer} has already been assigned to complete that Quest. Would you like to assign a different Adventurer?\n")
      print("1. Assign a different Adventurer.")
      print("2. Keep current Adventurer.")
      reassign_choice = console.input(f"\n[b medium_purple4]What do you want to do? (1/2)[/] ")
      if reassign_choice == '1':
        other_a = [a for a in party if a is not q_choice.adventurer]
        if len(other_a) == 0:
          console.print("\nThere are currently no other Adventurers in your party.\nReturn to Main Menu and enter Tavern to hire some!\n", justify="center", style="b")
        else:
          console.print(f'\nOther Adventurers in your party:\n', style='b')
          for adventurer in other_a:
            print(f'{adventurer.id} | {adventurer.name} the {adventurer.adventurer_class}\n')
          a_id = input(f"\nWhich Adventurer do you want to embark on a Quest? (1/2/3...) ")
          a_choice = get_adventurer_by_id(a_id)
          if a_choice == None:
            print(f"\nInvalid Adventurer. Please check your input.\n")
          else:
            attempt_quest(a_choice, q_choice)
      if reassign_choice == '2':
        attempt_quest(q_choice.adventurer, q_choice)
    else:
      if len(party) == 0:
        console.print("There are currently no Adventurers in your party. You need to go to the Tavern and hire some Adventurers before you can attempt a Quest!")
      else:
        console.print(f'\nAdventurers in your party:\n', style='b medium_purple4')
        for a in party:
          print(f'{a.id} | {a.name} the {a.adventurer_class}\n')
        a_id = input(f"\nWhich Adventurer do you want to embark on a Quest? (1/2/3...) ")
        a_choice = get_adventurer_by_id(a_id)
        if a_choice == None:
          print(f"\nInvalid Adventurer. Please check your input.\n")
        else:
          console.print(f'\n{a_choice.name} is attempting {q_choice.title}!\n', style = 'b')
          attempt_quest(a_choice, q_choice)

  display_quest_submenu()    

def attempt_quest(adventurer, quest):
  os.system('clear')
  console.print(f'\n{adventurer.name} is attempting {quest.title}!\n', style = 'b')
  difficulty_multiplier = {'Easy': 10, 'Medium': 14, 'Hard': 17}
  experience_multiplier = {'Easy': 3, 'Medium': 5, 'Hard': 7}
  matching_classes = {('Stealth', 'Rogue'), ('Magic', 'Mage'), ('Stealth', 'Rogue')}

  if (quest.quest_type, adventurer.adventurer_class) in matching_classes:
    for value in difficulty_multiplier:
      difficulty_multiplier[value] -= 4

  level = adventurer.level
  if level > 1:
    for value in difficulty_multiplier:
      difficulty_multiplier[value] -= level

  success_threshold = difficulty_multiplier.get(quest.difficulty)
  roll = random.randint(1, 20)
  
  experience_gained = 0
  print("\n      ,'. \n    ,' | `.\n  ,'18 | 4 `. \n,' `.  |  .' `.   \n\    `.|.'    /\n \  2 / \ 14 /\n  \  / 20\  /\n   \/_____\/\n")
  time.sleep(1)
  console.print(f'\nYou rolled a...\n', style='b medium_purple4', highlight=False)
  print(f'{roll}!\n')

  if roll >= success_threshold:
    experience_gained = experience_multiplier.get(quest.difficulty)
    print(f"{adventurer.name} successfully completed the quest {quest.title}. {experience_gained} XP gained.\n")
    complete_quest(adventurer, experience_gained, quest, 'Complete')
  else:
    print(f"{adventurer.name} failed the quest {quest.title}.\n\n")
    time.sleep(1)
    print(f"Time for a death roll...\n")
    
    death_roll =  random.randint(1, 20)
    print("\n      ,'. \n    ,' | `.\n  ,'18 | 4 `. \n,' `.  |  .' `.   \n\    `.|.'    /\n \  2 / \ 14 /\n  \  / 20\  /\n   \/_____\/")
    time.sleep(1)
    console.print(f'\nYou rolled a...\n', style='b medium_purple4', highlight=False)
    print(f'{death_roll}!\n')
    if death_roll == 1:
      print(f"{adventurer.name} was {quest.death}... RIP {adventurer}. They will be missed.\n")
      delete_adventurer(adventurer.id)
    else:
      print(f"Phew! {adventurer.name} survived\n")
      complete_quest(adventurer, experience_gained, quest, 'Failed')

def display_completed_quests():
  os.system('clear')
  quests = [quest for quest in get_all_quests() if quest.status == "Complete"]
  console.print("\nCompleted Quests\n", justify='center', style='b medium_purple4')
  if len(quests) == 0:
    console.print("\nNo Quests have been completed!\nIf your party is ready to tackle Quests, navigate back to Quest board, or go to the Tavern to hire more Adventurers.\n", justify='center')
  else:
    for quest in quests:
      console.print(f'{quest.title}', style = 'b')
      print(f"\n Description: {quest.description} \n Difficulty: {quest.difficulty}\n Type: {quest.quest_type} \n Adventurer: {quest.adventurer} \n Status: {quest.status}\n")
  display_quest_submenu()

def display_quest_submenu():
  console.print(f"\nQuest Menu\n", style='b medium_purple4')
  print('1. Return to Quest Board')
  print('2. Return to Main Menu')
  choice = console.input(f"\n[b medium_purple4]Where would you like to go now? (1/2) [/]")
  handle_quest_submenu(choice)

def handle_quest_submenu(choice):
  if choice == '1':
    view_quest_board()
  elif choice == '2':
    return
  else:
    print("Invalid choice. Please enter 1 or 2.")
    view_quest_board()