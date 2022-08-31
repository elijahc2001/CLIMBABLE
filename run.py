from flask import Flask, render_template
import sqlite3
app = Flask(__name__)

CLIMBDATABASE = 'CLIMBABLE_DATABASE'

@app.route('/')
def index():
      return render_template ("index.html")