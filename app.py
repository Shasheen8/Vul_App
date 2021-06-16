from flask import Flask, render_template
from flask_wtf import Form 
from wtforms import StringField
from wtforms.validators import InputRequired
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'yoursecretkey'

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
