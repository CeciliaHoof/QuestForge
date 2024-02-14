from models import *

def get_all_quests():
    return db.session.query(Quest).all()

def get_all_adventurers():
    return db.session.query(Adventurer).all()

def get_unassigned_quests():
    return db.session.query(Quest).filter(Quest.adventurer_id.is_(None))

def create_adventurer(name, adventurer_class):
    new_adventurer = Adventurer(name = name, adventurer_class = adventurer_class, level = 1, experience = 0)
    db.session.add(new_adventurer)
    db.session.commit()

    print(f"Adventurer {name} created successfully! \n")

def delete_adventurer(id):
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
        quest.adventurer = adventurer
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

def get_quest_details(id):
    quest = db.session.query(Quest).filter(Quest.id == id).first()

    if quest:
        print(f"\n{quest.title} \n Description: {quest.description} \n Difficulty: {quest.difficulty} \n Adventurer: {quest.adventurer}")
    else:
        print("Invalid quest. Please check your input")

def get_quests_by_difficulty(difficulty):
    diff = difficulty.lower()
    quests = db.session.query(Quest).filter(db.func.lower(Quest.difficulty) == diff).all()

    if quests:
        for quest in quests:
            print(f"\n{quest.title} \n Description: {quest.description} \n Difficulty: {quest.difficulty} \n Adventurer: {quest.adventurer}")
    else:
        print("Invalid difficulty. Please check your input")