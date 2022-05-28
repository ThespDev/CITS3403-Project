from flask import Blueprint,redirect, url_for, Config, render_template


main = Blueprint('main', __name__)

@main.route('/')
def main_index():
    return 'Hello Blueprint'

@main.route('/index')
def index():
    return render_template('index.html')