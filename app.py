from flask import Flask, render_template, redirect, flash
from flask.helpers import url_for
from flask_wtf import Form 
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True)


def __repr__(self):
	return f"User('{self.username}')"


class NormalForm(Form):
	username = StringField('Username', validators=[DataRequired(), Length(max=20)])

@app.route('/', methods=['GET','POST'])
def home():
	form = NormalForm()
	if form.validate_on_submit():
		user = User(username= form.username.data)
		db.session.add(user)
		db.session.commit()
		flash(f'Thank you for your submission: {form.username.data}! You are now part of our secure database ;)', 'success')
		return redirect(url_for('home'))
	return render_template('index.html', form=form)

if __name__ == '__main__':
	app.run(debug=True)
