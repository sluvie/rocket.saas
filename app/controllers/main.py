from flask import (
    render_template, 
    g,
    request,
    session,
    redirect,
    url_for
)
from app import app

@app.route('/', methods = ['GET'])
@app.route("/index")
def index():
    return render_template('index.html', title="rocket.saas")


@app.route('/home', methods = ['GET'])
def home():
    return render_template('home.html', title="main menu")
