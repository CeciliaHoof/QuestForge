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
    return new_adventurer

def delete_adventurer(id):
    adventurer = db.session.query(Adventurer).filter(Adventurer.id == id).first()
    if adventurer:
        quests = adventurer.quests
        if len(quests) > 0:
            for quest in quests:
                quest.status = 'Incomplete'
        db.session.delete(adventurer)
        db.session.commit()
        return True
    else:
        return False

def assign_adventurer_to_quest(adventurer_select, quest_select):

    adventurer = db.session.query(Adventurer).filter(Adventurer.id == adventurer_select).first()
    quest = db.session.query(Quest).filter(Quest.id == quest_select).first()

    if adventurer and quest:
        quest.adventurer = adventurer
        db.session.commit()
        return(adventurer, quest)
    else:
        print("Invalid adventurer or quest. Please check your input.")

def get_adventurer_by_id(id):
    return db.session.query(Adventurer).filter(Adventurer.id == id).first()

def get_quest_by_id(id):
    return db.session.query(Quest).filter(Quest.id == id).first()

def get_quests_by_type(type):
    q_type = type.lower()
    return db.session.query(Quest).filter(db.func.lower(Quest.quest_type) == q_type).all()

def complete_quest(adventurer, experience, quest):
    adventurer.experience += experience
    quest.status = 'Complete'
    db.session.commit()

    level_up_conditions = [(5, 1), (10, 2), (15, 3)]

    for experience_threshold, level_threshold in level_up_conditions:
        if adventurer.experience >= experience_threshold and adventurer.level == level_threshold:
            adventurer.level += 1
            adventurer.experience -= experience_threshold
            db.session.commit()
            print(f'{adventurer.name} leveled up! They are now level {adventurer.level}')