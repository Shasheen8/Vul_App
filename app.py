from flask import Flask, render_template
from flask_wtf import Form 
from wtforms import StringField
from wtforms.validators import InputRequired
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
import os

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'yoursecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'test.db')

db = SQLAlchemy(app)

@app.cli.command('db_create') #database creation
def db_create():
	db.create.all()
	print('Database Created')

@app.cli.command('db_create') #database dropped
def db_drop():
	db.drop.all()
	print('Database Dropped')


class NormalForm(Form):
	username = StringField('Input Field: Username', validators=[InputRequired()])

@app.route('/', methods=['GET','POST'])
def home():
	form = NormalForm()
	if form.validate_on_submit():
		return 'Thank you for your submission!!'
	return render_template('index.html', form=form)

if __name__ == '__main__':
	app.run(debug=True)
