from config import app

from models import *

if __name__ == "__main__":
  with app.app_context():

    Adventurer.query.delete()
    Quest.query.delete()

    quests = [
      Quest(
          title="Herbology Challenge",
          description="Collect rare herbs from the enchanted forest for the town's apothecary.",
          difficulty="Easy",
          quest_type="Magic",
          death="poisoned by misidentifying a dangerous plant"
      ),
      Quest(
          title="Sorcerer's Apprentice",
          description="Assist a powerful sorcerer with a magical experiment gone awry.",
          difficulty="Medium",
          quest_type="Magic",
          death="accidentally transformed into a small creature"
      ),
      Quest(
          title="Arcane Anomaly",
          description="Investigate a magical anomaly disrupting the balance of the mystical ley lines.",
          difficulty="Hard",
          quest_type="Magic",
          death="unraveled by uncontrollable magical energies"
      ),
      Quest(
          title="The Cursed Relic",
          description="Retrieve a cursed relic from an ancient tomb without succumbing to its dark influence.",
          difficulty="Medium",
          quest_type="Magic",
          death="corrupted and transformed into an undead minion"
      ),
      Quest(
          title="Goblin Gathering",
          description="Clear out a goblin camp that has been causing trouble in the nearby woods.",
          difficulty="Easy",
          quest_type="Strength",
          death="ambushed by goblin archers"
      ),
      Quest(
          title="Bandit Infestation",
          description="Eliminate a bandit group causing chaos on the trade route.",
          difficulty="Medium",
          quest_type="Strength",
          death="ambushed by cunning bandit leaders"
      ),
      Quest(
          title="Dragon's Lair",
          description="Slay the mighty dragon that has terrorized the kingdom for centuries.",
          difficulty="Hard",
          quest_type="Strength",
          death="incinerated by dragon's breath"
      ),
      Quest(
          title="Tournament of Champions",
          description="Compete in a grand tournament against skilled warriors from across the realm.",
          difficulty="Medium",
          quest_type="Strength",
          death="defeated in a duel against a formidable opponent"
      ),
      Quest(
          title="Haunted Ruins",
          description="Explore ancient ruins rumored to be haunted and recover a valuable artifact.",
          difficulty="Easy",
          quest_type="Stealth",
          death="possessed by vengeful spirits"
      ),
      Quest(
          title="Labyrinth of Shadows",
          description="Navigate a dark labyrinth to retrieve a lost artifact.",
          difficulty="Hard",
          quest_type="Stealth",
          death="trapped and consumed by shadows"
      ),
      Quest(
          title="Assassination Contract",
          description="Infiltrate an enemy stronghold and eliminate a dangerous target.",
          difficulty="Medium",
          quest_type="Stealth",
          death="captured and executed by enemy guards"
      ),
      Quest(
          title="Thieves' Guild Heist",
          description="Steal a priceless artifact from the heavily guarded Thieves' Guild headquarters.",
          difficulty="Hard",
          quest_type="Stealth",
          death="caught in the act and subjected to the guild's ruthless punishment"
      )
    ]

    db.session.add_all(quests)
    db.session.commit()

