from models import *

def get_all_quests():
    return db.session.query(Quest).all()

def get_all_adventurers():
    return db.session.query(Adventurer).all()

def get_unassigned_quests():
    return db.session.query(Quest).filter(Quest.adventurer_id.is_(None))

def create_adventurer():
    #Get input from the user:
    name = input("Enter the name of the adventurer: ")
    adventurer_class = input("Enter the class of the adventurer (warrior, mage, rogue): ")

    #Create new adventurer and add to database:
    new_adventurer = Adventurer(name = name, adventurer_class = adventurer_class, level = 1, experience = 0)
    db.session.add(new_adventurer)
    db.session.commit()

    print(f"Adventurer {name} created successfully! \n")

def delete_adventurer():
    #Get input from user:
    id = input("Which adventurer would you like to fire (1/2/3...)? ")
    adventurer = db.session.query(Adventurer).filter(Adventurer.id == id).first()

    #If adventurer is in database, delete it
    if adventurer:
        db.session.delete(adventurer)
        db.session.commit()
        print(f"Adventurer {adventurer.name} deleted successfully!")
    else:
        print(f"That adventurer doesn't exist. Please check your input.")

def assign_adventurer_to_quest(adventurer_select, quest_select):

    adventurer = db.session.query(Adventurer).filter(Adventurer.id == adventurer_select).first()
    quest = db.session.query(Quest).filter(Quest.id == quest_select).first()

    if adventurer and quest:
        quest.adventurer_id = adventurer.id
        db.session.commit()
        print(f"Adventurer {adventurer.name} assigned to quest {quest.title} successfully! \n")
    else:
        print("Invalid adventurer or quest. Please check your input.")

def get_adventurer_details(id):
    adventurer = db.session.query(Adventurer).filter(Adventurer.id == id).first()
    
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

    print('\n')