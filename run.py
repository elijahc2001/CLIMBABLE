from flask import Flask, render_template
import sqlite3
app = Flask(__name__)

CLIMBDATABASE = 'CLIMBABLE_DATABASE.db'

@app.route('/')
def index():
      return render_template ("index.html")

def get_all(db):
    pokemon = []
    cur = db.execute('SELECT * FROM pokemon_cleaned')
    for row in cur:
        pokemon.append(list(row))
    return {'pokemon':pokemon}
