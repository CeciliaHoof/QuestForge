import sys

import ipdb

from config import app

from models import *

from db_utils import *

if __name__ == "__main__":
  with app.app_context():
    pass
  ipdb.set_trace(sys._getframe())
