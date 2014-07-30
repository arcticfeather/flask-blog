# blog.py - controller

from flask import Flask, render_template, request, session. \
    flash, redirect, url_for, g
import sqlite3

# config
DATABASE = "blog.db"
app = Flask(__name__)

# pulls in app configuration by looking for UPPERCASE variables
app.config.from_object(__name__)

# function used for connecting to the DATABASE
def connect_db():
    return sqllite3.connect(app.config['DATABASE'])

# views

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/main')
def main():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)