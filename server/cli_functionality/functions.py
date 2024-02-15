def embark_on_quest():
  display_all_adventurers()

  adventurer_choice = input("Which Adventurer do you quest with? (1/2/3...) ")
  adventurer = get_adventurer_by_id(adventurer_choice)
  if adventurer == None:
    print("Invalid adventure. Please check your input.")
  else:
    quests = [quest for quest in adventurer.quests if quest.status == 'Incomplete']
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

# def questing_menu():
#   print("Questing Menu")
#   print("1. Keep Questing")
#   print("2. Return to Tavern")
#   choice = input("What would you like to do? (1/2) ")
#   handle_questing_menu(choice)

# def handle_questing_menu(choice):
#   if choice == "1":
#     embark_on_quest()
#   elif choice == "2":
#     enter_tavern()
#   else:
#     print("Invalid Input. Please input 1 or 2.")
#     enter_tavern()