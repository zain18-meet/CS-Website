
import datetime
from flask import Flask, Response, render_template, request, redirect
# SQLAlchemy
from sqlalchemy import create_engine, Column, DateTime, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
# flask setup
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"

db = SQLAlchemy(app)
engine = create_engine('sqlite:///project.db')
db.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

class Post(db.Model):
    __tablename__  = 'post'
    id             = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(25))
    img = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())

    def __repr__(self):
        return "<Post: %r>" % (
            self.id)

db.create_all()

###### ROUTES ######


@app.route('/')
def home():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/submit', methods=['GET','POST'])
def submit():
	if request.method=='GET':
		return render_template('submit.html')
	else:
		post = Post(title=request.form.get("title"), img=request.form.get("img"), 
		created_at= request.form.get('created_at'))	
		db.session.add(post)
		db.session.commit()
		posts = db.session.query(Post).all()
		return render_template('portfolio.html', posts=posts)

@app.route('/portfolio')
def portfolio():
	posts = db.session.query(Post).all()
	return render_template('portfolio.html', posts=posts)






