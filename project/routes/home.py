from flask import Blueprint, render_template

home_route = Blueprint('home', __name__)

@home_route.route('/', methods=['GET', 'POST'])
def home():
    return render_template('teste_index.html')