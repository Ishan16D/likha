import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, Blueprint
from werkzeug.exceptions import abort
from flask_login import login_required, current_user


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile', methods=["GET"])
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)
