from enum import unique
from flask import Flask, render_template
from flask_wtf import Form 
from wtforms import StringField
from wtforms.validators import InputRequired, Email
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)

def __repr__(self):
	return '<User {}>'.format(self.username)

class NormalForm(Form):
	username = StringField('Input Field: Username', validators=[InputRequired(), Email()])

@app.route('/', methods=['GET','POST'])
def home():
	form = NormalForm()
	if form.validate_on_submit():
		return 'Thank you for your submission!!'
	return render_template('index.html', form=form)

if __name__ == '__main__':
	app.run(debug=True)
