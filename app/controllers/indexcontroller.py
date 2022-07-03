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
    return render_template('index.html')