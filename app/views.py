from flask import url_for, redirect, render_template, request
from app import app
from app.models import TokensModel, BlockedUsersModel


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/<link:string>/', methods = ['GET','POST'])
def posts():
    if request.method == 'get':
        TokensModel.query.get()
        pass
    if request.method == 'post':
        # Make new link or return from db
        pass
    return render_template('index.html', link="abc", status="cde")