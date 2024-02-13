from models import *

def get_all_quests():
    return db.session.query(Quest).all()

def get_all_adventurers():
    return db.session.query(Adventurer).all()

def create_adventurer():
    #Get input from the user:
    name = input("Enter the name of the adventurer: ")
    adventurer_class = input("Enter the class of the adventurer (warrior, mage, rogue): ")

    #Create new adventurer and add to database:
    new_adventurer = Adventurer(name = name, adventurer_class = adventurer_class, level = 1, experience = 0)
    db.session.add(new_adventurer)
    db.session.commit()

    print(f"Adventurer {name} created successfully!")

def delete_adventurer():
    #Get input from user:
    name = input("Enter the name of the adventurer to fire: ").lower()
    adventurer = db.session.query(Adventurer).filter(db.func.lower(Adventurer.name) == name).first()

    #If adventurer is in database, delete it
    if adventurer:
        db.session.delete(adventurer)
        db.session.commit()
        print(f"Adventurer {name} deleted successfully!")
    else:
        print(f"No adventurer found with the name {name}.")

def get_unassigned_quests():
    return db.session.query(Quest).filter(Quest.adventurer_id.is_(None))

def assign_adventurer_to_quest(adventurer_select, quest_select):

    adventurer = db.session.query(Adventurer).filter(Adventurer.id == adventurer_select).first()
    quest = db.session.query(Quest).filter(Quest.id == quest_select).first()

    if adventurer and quest:
        quest.adventurer = adventurer
        db.session.commit()
        print(f"Adventurer {adventurer.name} assigned to quest {quest.title} successfully!")
    else:
        print("Invalid adventurer or quest. Please check your input.")
