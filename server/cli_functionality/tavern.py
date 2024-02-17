from db_utils import *
from .quest_board import view_quest_board
import time
import os
from rich.console import Console

console = Console()

def enter_tavern():
  os.system('clear')
  console.print("""
      /\                                  ) (
     /\/\                               ) ( )
    /\/\/\                             _(_)_.     
   /\/\/\/\                           |     |
  /\/\/\/\/\                          |     |
 /\/\/\/\/\/\                         |     |
/\/\/\/\/\/\/\                        |     |
|~~~~~~~~~~~~|________________________|_____|
|  /\    /\  |/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|
|  \/    \/  |\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|
|   TAVERN   |/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|
|     __     |\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|
|    /  \    |  /\    /\    /\    /\    /\  |
|   |    |   | |  |  |  |  |  |  |  |  |  | |
|   |-   |   | |__|  |__|  |__|  |__|  |__| |
|___|____|___|______________________________|
                """, style= 'orange4', justify='center', highlight=False)
  console.print(f"\nWelcome to the Tavern!\n\n", style = "b orange4", justify='center')
  console.print(f"Where all of your Adventurers will await their Quest assignments once hired.\n\nIf the Tavern is empty, hire an Adventurer, and they'll come in.\n\nIf you hire an Adventurer and aren't happy with their performance, you can fire them.\nBut be careful, this will undo any Quests they successfully completed.\n\nOnce your party is complete, head to the Quest Board to start sending Adventurers on Quests!", justify="center")
  ad = display_all_adventurers()
  if len(ad) == 0:
    console.print("Adventurer Menu\n", style = 'b orange4')
    print("1. Hire an Adventurer")
    print("2. Return to Main Menu")
    choice = console.input("\n[b orange4]What would you like to do? (1/2) [/]")
    if choice == "1":
      handle_adventurer_choice(choice)
    elif choice == "2":
      return
    else:
      print("Invalid choice. Please enter 1 or 2.")
      enter_tavern()
  else:
    display_adventurer_menu()

def display_all_adventurers():
  adventurers = get_all_adventurers()
  if len(adventurers) == 0:
    console.print("\n\nThere are currently no Adventurers in the Tavern.\nHire some Adventurers to bring them in!\n\n", justify="center", style="b")
  else:
    console.print(f'\nAdventurers in your party:\n', style='b')
    for adventurer in adventurers:
      print(f'{adventurer.id} | {adventurer.name} the {adventurer.adventurer_class}\n')
  return adventurers

def display_adventurer_menu():
  console.print("\nAdventurer Menu\n", style = 'b orange4')
  print("1. Hire an Adventurer")
  print("2. View Adventurer Details")
  print("3. Fire an Adventurer")
  print("4. View Quest Board")
  print("5. Return to Main Menu")
  user_choice = console.input("\n[b orange4]What is your choice? (1/2/3/4/5) [/]")
  handle_adventurer_choice(user_choice)

def handle_adventurer_choice(choice):
  if choice == "1":
    new_adventurer()
  elif choice == "2":
    view_adventurer()
  elif choice == "3":
    fire_adventurer()
  elif choice == "4":
    view_quest_board()
  elif choice == "5":
    return
  else:
    print("\nInvalid choice. Please enter 1, 2, 3, 4, or 5.\n")
    time.sleep(3)
    enter_tavern()

def new_adventurer():
  os.system('clear')
  console.print(f'\n Hiring an Adventurer', justify="center", style='b orange4')
  print(f"""
                                                                          .------------------------------------------------------.
                                                                          |                                                      | 
                                                                          |   Dear Adventurer,                                   |
                                                                          |                                                      |
                                                                          |   I am pleased to offer you an exciting              |
                                                                          |   opportunity to embark on heroic Quests as part.    |
                                                                          |   of my Adventurer party.                            |
                                                                          |                                                      |
                                                                          |   Join us at the Tavern to accept epic quests!       |
                                                                          |                                                      |
                                                                          |   Sincerely,                                         |
                                                                          |   Party Leader                                       |
                                                                          '______________________________________________________'""")
  console.print(f"\n\nEnter the name and class of the Adventurer you want to hire, and the letter will be sent!", justify='center', style='b')
  name = input(f"\nEnter the name of the Adventurer: ")
  adventurer_class = input(f"\nEnter the class of the Adventurer (warrior, mage, rogue): ").title()
  valid_classes = ['Mage', 'Warrior', 'Rogue']
  if adventurer_class in valid_classes:
    new_adventurer = create_adventurer(name, adventurer_class)
    console.print(f'\nThe letter has been sent to {new_adventurer.name}. Hopefully, you will hear back soon!')
    time.sleep(2)
    console.print(f'\n{new_adventurer.name} has entered the tavern and accepted the position in your party!')
    time.sleep(3)
  else:
    print(f"\nInvalid Adventure class. Please try again.\n")
    time.sleep(2)
  enter_tavern()

def view_adventurer():
  a_id = input("\nWhich adventurer do you want to see? (1/2/3...) ")
  adventurer = get_adventurer_by_id(a_id)
  if adventurer:
    os.system('clear')
    console.print(f"\nAdventurer Details\n", justify='center', style='b orange4')
    quests = adventurer.quests
    quest_display = ''
    if len(quests) == 0:
        quest_display = f"{adventurer.name} has not been given any Quests."
    for quest in quests:
        quest_display += f'<{quest.title}>'
    console.print(f"\n{adventurer.name}", style = "b")
    print(f"\n Class: {adventurer.adventurer_class} \n Level: {adventurer.level} \n Experience: {adventurer.experience} \n Quests: {quest_display}\n")
  else:
    print("\nInvalid adventurer. Please check your input.\n")
  display_adventurer_submenu()
  
def fire_adventurer():
  os.system('clear')
  console.print(f"\nFire an Adventurer\n", justify='center', style='b orange4')
  print(f'Firing an Adventure will greatly offend them, so they will leave the Tavern.\nThey will abandon all of their assigned Quests, and out of spite, they will undo any Quests they have successfully completed.\n')
  print('1. Yes, I still want to fire an Adventurer.')
  print("2. No, I guess I'll keep them.")
  choice = console.input(f"\n[b orange4]What do is your choice? (1/2)[/] ")
  handle_fire_choice(choice)

def handle_fire_choice(choice):
  if choice == '1':
    display_all_adventurers()
    id = console.input(f"\n[b orange4]Which adventurer would you like to fire? (1/2/3...) [/]")
    adventurer = get_adventurer_by_id(id)
    deleted = delete_adventurer(id)
    if deleted:
      print(f"\nYou fired {adventurer.name}! They stormed from the Tavern and vowed never to return again!\n")
    else:
      print(f"\nInvalid adventurer. Check your input.\n")
    time.sleep(4)
    enter_tavern()
  elif choice == '2':
    enter_tavern()
  else:
    print('\nInvalid choice. Please enter 1 or 2.\n')
    fire_adventurer()

def display_adventurer_submenu():
  console.print("\nAdventurer Menu\n", style = 'b orange4')
  print('1. Return to Tavern')
  print('2. Return to Main Menu')
  choice = console.input(f"\n[b orange4]Where would you like to go now? (1/2)?[/] ")
  handle_adventurer_submenu(choice)

def handle_adventurer_submenu(choice):
  if choice == '1':
    enter_tavern()
  elif choice == '2':
    return
  else:
    print("Invalid choice. Please enter 1 or 2.")