from flask import Flask, Response, render_template, request, redirect, url_for

# flask setup
app = Flask(__name__)
app.config["SECRET_KEY"] = "ITSASECRET"

# SQLAlchemy
from model import Base, Post, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

###### ROUTES ######

@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/portfolio')
def portfolio():
	return render_template("portfolio.html")


@app.route('/submit', methods=['GET', 'POST'])
def submit():
	if request.method=='GET':
			return render_template('submit.html')
		else:
			post = Post(title=request.form.get("title"), text=request.form.get("img"))
			print("adding post")	
			session.add(post)
			session.commit()
			return redirect('/home')






