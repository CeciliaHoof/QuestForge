from db_utils import *
import random

def enter_tavern():
  print("Welcome to the Tavern, where all of your Adventurers wait to be hired to a quest. From here you can hire an adventurer to assign them quests, or you can delete an delete an adventurer. \n Here are all of the adventurers: \n")
  display_all_adventurers()
  display_adventurer_menu()

def display_all_adventurers():
  adventurers = get_all_adventurers()
  if len(adventurers) == 0:
    print("There are currently no Adventurers waiting for a quest! Create some Adventurers! \n")
  else:
    for adventurer in adventurers:
      print(f'{adventurer.id} | {adventurer.name} \n')

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
      enter_tavern()
  else:
    print("Adventurer Menu")
    print("1. Create an Adventurer")
    print("2. Hire an Adventurer")
    print("3. View Adventurer Details")
    print("4. Fire an Adventurer")
    print("5. Return to Main Menu")
    adventurer_choice = input("What is your choice? (1/2/3/4/5) ")
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
    fire_adventurer()
    enter_tavern()
  elif choice == "5":
    return
  else:
    print("Invalid choice. Please enter 1, 2, or 3.")

def view_adventurer(adventurer_id):
  adventurer = get_adventurer_by_id(adventurer_id)
  if adventurer:
    quests = adventurer.quests
    quest_display = ''
    if len(quests) == 0:
        quest_display = f"{adventurer.name} has not been hired for any quests"
    for quest in quests:
        quest_display += f'<{quest.title}>'
    print(f"\n{adventurer.name} \n Class: {adventurer.adventurer_class} \n Level: {adventurer.level} \n Experience: {adventurer.experience} \n Quests: {quest_display}")
  else:
    print("Invalid adventurer. Please check your input.")
  display_adventurer_submenu()
  
def display_adventurer_submenu():
  print('1. Return to Tavern')
  print('2. Return to Main Menu')
  choice = input("Where would you like to go now? (1/2)? ")
  handle_adventurer_submenu(choice)

def handle_adventurer_submenu(choice):
  if choice == '1':
    enter_tavern()
  elif choice == '2':
    return
  else:
    print("Invalid choice. Please enter 1 or 2.")

def hire_adventurer():
  quests = get_unassigned_quests()
  if len(quests) == 0:
    print("All Quests are currently claimed. Time to embark on a quest!")
  else:
    print("Here are your adventurers:\n")
    display_all_adventurers()
    adventurer = input("Which Adventure would you like to hire? (1/2/3...) ")
    print("Here are the quests that still need an adventurer:")
    for quest in quests:
      print(f'{quest.id}: {quest.title} \n Difficulty: {quest.difficulty} \n')
    quest_hire = input("Which quest is this adventurer going to tackle? (1/2/3...) ")
    assign_adventurer_to_quest(adventurer, quest_hire)
  display_hire_menu()
  
def display_hire_menu():
  print("Hire Menu")
  print("1. Keep Hiring Adventurers")
  print("2. Embark on Quest")
  print("3. Return to Tavern")
  hire_choice = input("What is your choice? (1/2/3) ")
  handle_hire_choice(hire_choice)

def handle_hire_choice(choice):
  if choice == "1":
    hire_adventurer()
  elif choice == "2":
    embark_on_quest()
  elif choice == "3":
    enter_tavern()
  else:
    print("Invalid input, please enter 1 or 2.")

def embark_on_quest():
  display_all_adventurers()

  adventurer_choice = input("Which Adventurer do you quest with? (1/2/3...) ")
  adventurer = get_adventurer_by_id(adventurer_choice)
  if adventurer == None:
    print("Invalid adventure. Please check your input.")
  else:
    quests = [quest for quest in adventurer.quests if quest.status == 'incomplete']
    if len(quests) == 0:
      print("This Adventurer has no incomplete quests. Pick another Adventurer or return to tavern to hire them to more quests.")
    else:
      for quest in quests:
        print(f'{quest.id} | {quest.title} | {quest.difficulty}')
      quest_choice = input("Which Quest do you want to tackle first? (1/2/3...) ")
      quest = get_quest_by_id(quest_choice)
      if quest in quests:
        attempt_quest(adventurer, quest)
      else:
        print("This adventurer has not been hired for that quest or has already completed it. Try again.")

  questing_menu()

def attempt_quest(adventurer, quest):
  level = adventurer.level
  difficulty_multiplier = {'Easy': 5, 'Medium': 10, 'Hard': 15}
  if level > 1:
    for value in difficulty_multiplier:
      difficulty_multiplier[value] -= level
  experience_multiplier = {'Easy': 3, 'Medium': 5, 'Hard': 7}
  success_threshold = difficulty_multiplier.get(quest.difficulty)
  roll = random.randint(1, 20)

  if roll >= success_threshold:
    print(f"{adventurer.name} successfully completed the quest {quest.title}")
    experience_gained = experience_multiplier.get(quest.difficulty)
    complete_quest(adventurer, experience_gained, quest)
  else:
    print(f"{adventurer.name} failed the quest {quest.title}. Better luck next time!")

def questing_menu():
  print("Questing Menu")
  print("1. Keep Questing")
  print("2. Return to Tavern")
  choice = input("What would you like to do? (1/2) ")
  handle_questing_menu(choice)

def handle_questing_menu(choice):
  if choice == "1":
    embark_on_quest()
  elif choice == "2":
    enter_tavern()
  else:
    print("Invalid Input. Please input 1 or 2.")
    enter_tavern()

def fire_adventurer():
  print(f'Firing an Adventure will remove them from their quests, and any successfully completed quests will be reset to incomplete.')
  print('1. Yes, I still want to fire an Adventurer.')
  print("2. No, I guess I'll keep them.")
  choice = input("What do is your choice? (1/2) ")
  handle_fire_choice(choice)

def handle_fire_choice(choice):
  if choice == '1':
    id = input("Which adventurer would you like to fire? (1/2/3...) ")
    delete_adventurer(id)
  elif choice == '2':
    enter_tavern()
  else:
    print('Invalid choice. Please enter 1 or 2.')
    fire_adventurer()