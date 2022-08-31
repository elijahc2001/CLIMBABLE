from flask import Flask, render_template
import sqlite3
app = Flask(__name__)

CLIMBDATABASE = 'CLIMBABLE_DATABASE'

@app.route('/')
def index():
      db = sqlite3.connect(CLIMBABLE_DATABASE)
    print(db)