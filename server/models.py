from config import db

# Define the Adventurer and Quest classes
class Adventurer(db.Model):
    __tablename__ = 'adventurers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    adventurer_class = db.Column(db.String)
    level = db.Column(db.Integer, default = 0)
    experience = db.Column(db.Integer, default = 0)

    quests = db.relationship('Quest', back_populates='adventurer')

    def __repr__(self) -> str:
        return f'{self.name}'

class Quest(db.Model):
    __tablename__ = 'quests'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String)
    difficulty = db.Column(db.String)
    status = db.Column(db.String, default = 'incomplete')

    adventurer_id = db.Column(db.Integer, db.ForeignKey('adventurers.id'))
    adventurer = db.relationship('Adventurer', back_populates='quests')
