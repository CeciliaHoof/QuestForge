from config import app

from models import *

if __name__ == "__main__":
  with app.app_context():
    print('Clearing out tables...')

    Adventurer.query.delete()
    Quest.query.delete()

    print("Seeding quests table...")
    quests = [
      Quest(
        title = "The Goblins' Menace",
        description = "Goblins have invaded the peaceful village of Eldoria. Embark on a quest to defeat the goblin horde, rescue the captured villagers, and restore peace to Eldoria.",
        difficulty = "easy"
      ),

      Quest(
        title = 'Enchanted Forest Exploration',
        description = 'Venture into the mystical Enchanted Forest to discover its secrets and gather rare herbs for the village alchemist. Beware of magical creatures and hidden challenges.',
        difficulty = "medium"
      ),

      Quest(
        title = "Dragon's Roar",
        description = "A menacing dragon has taken residence in the nearby mountains. Gather a group of brave adventurers to confront the dragon, safeguard the kingdom, and claim the dragon's treasure.",
        difficulty = "hard"
      ),

      Quest(
        title = "Feywild Diplomacy",
        description = "The ethereal Feywild has opened a portal to our realm, causing disturbances. Travel to the Feywild, negotiate with its magical inhabitants, and restore the balance between the two worlds.",
        difficulty = "medium"
      ),

      Quest(
        title = "Ghostly Hauntings",
        description = "A haunted castle on the outskirts of the kingdom is causing distress among the locals. Investigate the ghostly occurrences, unravel the mysteries, and lay the spirits to rest.",
        difficulty = "medium"
      )
    ]

    db.session.add_all(quests)
    db.session.commit()

    print("Seeding adventurers table...")

    dummy = Adventurer(
      name = "Dummy Adventure",
      adventurer_class = "druid",
      level = 1
    )

    db.session.add(dummy)
    db.session.commit()
