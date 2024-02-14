from models import *

def get_all_quests():
    return db.session.query(Quest).all()

def get_all_adventurers():
    return db.session.query(Adventurer).all()

def get_unassigned_quests():
    return db.session.query(Quest).filter(Quest.adventurer_id.is_(None)).all()

def create_adventurer(name, adventurer_class):
    new_adventurer = Adventurer(name = name, adventurer_class = adventurer_class)
    db.session.add(new_adventurer)
    db.session.commit()

    print(f"Adventurer {name} created successfully! \n")

def delete_adventurer(id):
    adventurer = db.session.query(Adventurer).filter(Adventurer.id == id).first()

    #If adventurer is in database, delete it
    if adventurer:
        quests = adventurer.quests
        if len(quests) > 0:
            for quest in quests:
                quest.status = 'incomplete'
        db.session.delete(adventurer)
        db.session.commit()
        
        print(f"Adventurer {adventurer.name} fired successfully!")
    else:
        print(f"That adventurer doesn't exist. Please check your input.")

def assign_adventurer_to_quest(adventurer_select, quest_select):

    adventurer = db.session.query(Adventurer).filter(Adventurer.id == adventurer_select).first()
    quest = db.session.query(Quest).filter(Quest.id == quest_select).first()

    if adventurer and quest:
        if quest.adventurer:
            print(f"{quest.adventurer.name} has already been hired for {quest.title}")
        else:
            quest.adventurer = adventurer
            db.session.commit()
            print(f"Adventurer {adventurer.name} hired to {quest.title}! \n")
    else:
        print("Invalid adventurer or quest. Please check your input.")

def get_adventurer_by_id(id):
    return db.session.query(Adventurer).filter(Adventurer.id == id).first()

def get_quest_by_id(id):
    return db.session.query(Quest).filter(Quest.id == id).first()

def get_quests_by_difficulty(difficulty):
    diff = difficulty.lower()
    quests = db.session.query(Quest).filter(db.func.lower(Quest.difficulty) == diff).all()

    if quests:
        for quest in quests:
            print(f"\n{quest.title} \n Description: {quest.description} \n Difficulty: {quest.difficulty} \n Adventurer: {quest.adventurer}")
    else:
        print("Invalid difficulty. Please check your input")

def complete_quest(adventurer, experience, quest):
    adventurer.experience += experience
    quest.status = 'complete'
    db.session.commit()

    level_up_conditions = [(5, 1), (10, 2), (15, 3)]

    for experience_threshold, level_threshold in level_up_conditions:
        if adventurer.experience >= experience_threshold and adventurer.level == level_threshold:
            adventurer.level += 1
            adventurer.experience -= experience_threshold
            db.session.commit()
            print(f'{adventurer.name} leveled up! They are now level {adventurer.level}')