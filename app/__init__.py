from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Command, Shell
from flask_login import LoginManager
import os

# create application instance
app = Flask(__name__)

# import views
from . import views
