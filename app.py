from flask import Flask
from model import setup_db
app = Flask(__name__)
db, app = setup_db(app)
