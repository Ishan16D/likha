import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

app = Flask(__name__)

app.config['SECRET_KEY'] = 'hvasjvnjsnvjavvavasfvnsfhv'

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/about')
def about():

    return render_template('about.html')
