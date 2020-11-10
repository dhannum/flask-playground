from app import app
from flask import render_template, request, redirect, url_for, flash, make_response, session

@app.route('/')
def index():
    url = request.args.get('url')
    return render_template('index.html', result=url)
