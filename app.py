from flask import Flask, Response, render_template, request, redirect, url_forfrom 
from flask.ext.sqlalchemy import SQLAlchemy


# flask setup
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"

# SQLAlchemy
from model import Base, Post, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
db = SQLAlchemy(app)

###### ROUTES ######


@app.route('/')
def home():
	return render_template('home.html')

@app.route('/portfolio')
def portfolio():
	return render_template('portfolio.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/submit', methods=['GET','POST'])
def post():
	title= requets.form['title']
	img= request.form['img']
	created_at= request.form['created_at']

	if request.method=='GET':
		return render_template('submit.html')
	else:
		post = Post(title=request.form.get("title"), img=request.form.get("img"), 
		created_at= request.form.get('created_at'))
		print("adding post")	
		session.add(post)
		session.commit()
		return redirect('portfolio.html')






