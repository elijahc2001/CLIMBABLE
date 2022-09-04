from flask import Flask, render_template
import sqlite3
app = Flask(__name__)

CLIMBDATABASE = 'CLIMBABLE_DATABASE.db'


@app.route('/')
def index():
    db = sqlite3.connect(CLIMBDATABASE)
    tables = get_all(db)
    db.close()
    return render_template('index.html',
    title=tables['climbs'])

def get_all(db):
    title = []
    cur = db.execute('SELECT * FROM climbs')
    for row in cur:
        title.append(list(row))
    return {'title':climbs}
