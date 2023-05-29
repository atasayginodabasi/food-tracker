from foodTracker import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


# Login Manager
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    profile_image = db.Column(db.String(20), nullable=False, default='default_profile.png')
    username = db.Column(db.String(64), unique=True, index=True)
    fullname = db.Column(db.String(128), index=True)
    password_hash = db.Column(db.String(128))

    entries = db.relationship('Entries', backref='entry', lazy=True)

    def __init__(self, fullname, username, password):
        self.fullname = fullname
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Entries(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    food_selection = db.Column(db.Integer, db.ForeignKey('foods.id'), nullable=False)

    def __init__(self, date, food_selection, user_id):
        self.food_selection = food_selection
        self.user_id = user_id
        self.date = date


class Foods(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    food_name = db.Column(db.String(64), unique=True, index=True)
    protein = db.Column(db.Integer, nullable=False)
    carbohydrates = db.Column(db.Integer, nullable=False)
    fat = db.Column(db.Integer, nullable=False)

    food_names = db.relationship('Entries', backref='food', lazy=True)

    def __init__(self, food_name, protein, carbohydrates, fat):
        self.food_name = food_name
        self.protein = protein
        self.carbohydrates = carbohydrates
        self.fat = fat
