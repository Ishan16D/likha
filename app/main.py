import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


# def get_page(page_title):
#     conn = get_db_connection()
#     page = conn.execute('SELECT * FROM pages WHERE title = ?',
#                         (page_title,)).fetchone()
#     conn.close()
#     if page is None:
#         abort(404)
#     return page

app = Flask(__name__)

app.config['SECRET_KEY'] = 'hvasjvnjsnvjavvavasfvnsfhv'


@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/<string:page_title>')
# def page(page_title):
#     page = get_page(page_title)
#     return render_template('page.html', page=page)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        username = 'IshanD'

        if not title:
            flash('Title is required!')
        if not content:
            flash('Content is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO text (title, username, content) VALUES (?, ?, ?)', (title, username, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')