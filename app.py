# sudo nano /etc/paths

from flask import Flask
from flaskwebgui import FlaskUI
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')

debug = 0

#app.config['SQLALCHEMY_BINDS'] = {'bind_db': 'sqlite:///' + os.path.join(basedir, 'app.sqlite')}
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:lupolucio111@localhost:3306/daniel_dashboard'
db = SQLAlchemy(app)
app.secret_key = "quando ero scoglio e tu onda, ti amavo gia, anche se a poco poco, per il tuo gioco, mi sgretolavo ad ogni assalto, morivo in te, per te..."

#lupolucio111
from view import *


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    if debug:
        ui = FlaskUI(app=app, server="flask", width='800', height=600)
        ui.run()
    else:    
        app.debug = True
        app.run()
