import sys

import ipdb

from config import app

from models import *

from db_utils import *

if __name__ == "__main__":
  with app.app_context():
    def embark_on_quest():
      q_id = input("Which Quest do you want to attempt? (1/2/3...) ")
      quest = get_quest_by_id(q_id)
      if quest is None:
        print("Invalid Quest. Please check your input.")
      else:
        adventurer = get_adventurer_by_id(quest.adventurer_id)
  ipdb.set_trace(sys._getframe())
