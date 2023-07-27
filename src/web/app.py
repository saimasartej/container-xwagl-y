from flask import Flask, render_template
from db import get_db, close_db
import sqlalchemy
from logger import log

app = Flask(__name__)



@app.route("/")
def index():
    return "kk"


