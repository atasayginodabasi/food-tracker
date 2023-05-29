from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

dbHost = 'localhost'
dBName = 'food_tracker'
dbUserName = 'ata'
dbUserPassword = 'ata125'
dbPort = 5432

# ----------------------------------------------------------------------------------------------------------------------

app = Flask(__name__)

app.config['SECRET_KEY'] = '123ddfsdfsdf'

# ----------------------------------------------------------------------------------------------------------------------

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{dbUserName}:{dbUserPassword}@" \
                                        f"{dbHost}:{dbPort}/{dBName}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

# ----------------------------------------------------------------------------------------------------------------------

# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'users.login'

# ----------------------------------------------------------------------------------------------------------------------

from foodTracker.home_page.views import home_page
from foodTracker.entries.views import day_details
from foodTracker.add_new_food.views import add_new_food
from foodTracker.users.views import users


app.register_blueprint(home_page)
app.register_blueprint(day_details)
app.register_blueprint(add_new_food)
app.register_blueprint(users)
