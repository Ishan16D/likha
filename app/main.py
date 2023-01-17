import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, Blueprint
from werkzeug.exceptions import abort
from flask_login import login_required, current_user
from .models import Pages, User
from . import db

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_page(page_id):
    page_id=page_id
    page = Pages.query.filter_by(id=page_id)

    if page is None:
        abort(404)
    return page


main = Blueprint('main', __name__)


@main.route('/', methods= ['POST', 'GET'])
def index():
    return render_template('index.html')

@main.route('/profile', methods=["GET"])
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


@main.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        tagline = request.form['tagline']
        content = request.form['content']
        name = current_user.name

        user_id = User.query.filter_by(name=name).first().id
        new_page = Pages(
                user_id = user_id,
                title = title,
                tagline = tagline,
                content = content
        )

        if not title:
            flash('Title is required!')
        if not tagline:
            flash('Content is required!')
        if not content:
            flash('Content is required!')
        else:
            db.session.add(new_page)
            db.session.commit()


    return render_template('create.html')

@main.route('/my_work')
@login_required
def my_work():
    name = current_user.name
    user_id = User.query.filter_by(name=name).first().id

    pages = Pages.query.filter_by(user_id=user_id).all()


    return render_template('my_work.html', pages=pages)

@main.route('/<string:page_id>', methods=['GET'])
@login_required
def page(page_id):
    page = get_page(page_id)
    return render_template('page.html', page=page)



