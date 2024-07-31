from config import SQLALCHEMY_DATABASE_URI
from app import db
import os.path

# creates the database file for the application
db.create_all()
