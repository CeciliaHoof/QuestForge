from db_utils import *
import random

def enter_tavern():
  print("Welcome to the Tavern, where all of your Adventurers wait to be hired to a quest. From here you can hire an adventurer to assign them quests, or you can delete an adventurer.")
  ad = display_all_adventurers()
  if len(ad) == 0:
    print("Adventurer Menu")
    print("1. Create an Adventurer")
    print("2. Return to Main Menu")
    choice = input("What would you like to do? (1/2) ")
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
    print("\nThere are currently no Adventurers waiting for a quest! Create some Adventurers!\n")
  else:
    print(f'\nHere are all your Adventurers:\n')
    for adventurer in adventurers:
      print(f'{adventurer.id} | {adventurer.name}\n')
  return adventurers

def display_adventurer_menu():
  print("Adventurer Menu")
  print("1. Create an Adventurer")
  print("2. Hire an Adventurer")
  print("3. View Adventurer Details")
  print("4. Fire an Adventurer")
  print("5. Return to Main Menu")
  user_choice = input("What is your choice? (1/2/3/4/5) ")
  handle_adventurer_choice(user_choice)

def handle_adventurer_choice(choice):
  if choice == "1":
    new_adventurer()
  elif choice == "2":
    hire_adventurer()
  elif choice == "3":
    view_adventurer()
  elif choice == "4":
    fire_adventurer()
  elif choice == "5":
    return
  else:
    print("\nInvalid choice. Please enter 1, 2, 3, 4, or 5.\n")
    enter_tavern()

def new_adventurer():
  name = input("Enter the name of the adventurer: ")
  adventurer_class = input("Enter the class of the adventurer (warrior, mage, rogue): ").title()
  valid_classes = ['Mage', 'Warrior', 'Rogue']
  if adventurer_class in valid_classes:
    new_adventurer = create_adventurer(name, adventurer_class)
    print(f'\nAdventurer {new_adventurer.name} successfully created!\n')
  else:
    print(f"\nInvalid Adventure class. Please try again.\n")
  enter_tavern()

def view_adventurer():
  a_id = input("Which adventurer do you want to see? (1/2/3...) ")
  adventurer = get_adventurer_by_id(a_id)
  if adventurer:
    quests = adventurer.quests
    quest_display = ''
    if len(quests) == 0:
        quest_display = f"{adventurer.name} has not been hired for any quests"
    for quest in quests:
        quest_display += f'<{quest.title}>'
    print(f"\n{adventurer.name} \n Class: {adventurer.adventurer_class} \n Level: {adventurer.level} \n Experience: {adventurer.experience} \n Quests: {quest_display}\n")
  else:
    print("\nInvalid adventurer. Please check your input.\n")
  display_adventurer_submenu()

def hire_adventurer():
  quests = get_unassigned_quests()
  if len(quests) == 0:
    print("\nAll Quests are currently claimed. Time to embark on a quest!\n")
  else:
    display_all_adventurers()
    a_id = input("Which Adventure would you like to hire? (1/2/3...) ")
    print("Here are the quests that still need an adventurer:")
    for q in quests:
      print(f'{q.id} | {q.title} \n Difficulty: {q.difficulty} \n Type: {q.quest_type} \n')
    q_id = input("Which quest is this adventurer going to tackle? (1/2/3...) ")
    quest_check = get_quest_by_id(q_id)
    if quest_check.adventurer:
      print(f"\nAn Adventurer has already been hired to complete that Quest.\n")
    else:
      adventurer, quest = assign_adventurer_to_quest(a_id, q_id)
      print(f"\nAdventurer {adventurer.name} hired to {quest.title}! Lets see if they succeed...\n")
      attempt_quest(adventurer, quest)
  display_hire_menu()

def attempt_quest(adventurer, quest):
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

  if roll >= success_threshold:
    experience_gained = experience_multiplier.get(quest.difficulty)
    print(f"{adventurer.name} successfully completed the quest {quest.title}. {experience_gained} XP gained.\n")
    complete_quest(adventurer, experience_gained, quest, 'Complete')
  else:
    print(f"{adventurer.name} failed the quest {quest.title}. To reattempt this quest, visit the Quest Board and view incomplete Quests.\n\nTime for a death roll...\n")
    
    death_roll =  random.randint(1, 20)
    if death_roll > 10:
      print(f"{adventurer.name} was {quest.death}... RIP\n")
      delete_adventurer(adventurer.id)
    else:
      print(f"Phew! {adventurer.name} survived\n")
      complete_quest(adventurer, experience_gained, quest, 'Failed')
  

def fire_adventurer():
  print(f'Firing an Adventure will remove them from their quests, and any successfully completed quests will be reset to incomplete.')
  print('1. Yes, I still want to fire an Adventurer.')
  print("2. No, I guess I'll keep them.")
  choice = input("What do is your choice? (1/2) ")
  handle_fire_choice(choice)

def handle_fire_choice(choice):
  if choice == '1':
    id = input("Which adventurer would you like to fire? (1/2/3...) ")
    adventurer = get_adventurer_by_id(id)
    deleted = delete_adventurer(id)
    if deleted:
      print(f"\n{adventurer.name} fired successfully!\n")
    else:
      print(f"\nInvalid adventurer. Check your input.\n")
    enter_tavern()
  elif choice == '2':
    enter_tavern()
  else:
    print('\nInvalid choice. Please enter 1 or 2.\n')
    fire_adventurer()

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

def display_hire_menu():
  print("Hire Menu")
  print("1. Keep Hiring Adventurers")
  print("2. Return to Tavern")
  hire_choice = input("What is your choice? (1/2) ")
  handle_hire_choice(hire_choice)

def handle_hire_choice(choice):
  if choice == "1":
    hire_adventurer()
  elif choice == "2":
    enter_tavern()
  else:
    print("Invalid input, please enter 1 or 2.")