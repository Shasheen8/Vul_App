from flask import Flask
from flask import session, request, render_template, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# config mysql
app.config['MYSQL_HOST'] = 'host'
app.config['MYSQL_USER'] = 'db_name'
app.config['MYSQL_PASSWORD'] = 'db_password'
app.config['MYSQL_DB'] = 'host'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.secret_key = 'key'

mysql = MySQL()
mysql.init_app(app)

@app.cli.command('db_create') # need these, they allow you to create the database
def db_create():
    cur = mysql.connection.cursor()
    test_db = cur.execute("""
    create table sql5419806.users (
    id integer not null auto_increment unique,
    username varchar(70),
    password varchar(70));""")
    
@app.cli.command('populate_db')
def db_populate():
   cur = mysql.connection.cursor()
   populate_db = cur.execute("""
        USE sql5419806;
        INSERT INTO users (
            username, password
            )
        VALUES
        ('test', 'pass'),
        ('Ana', 'eat'),
        ('admin', 'admin'),
        ('admin', 'ginger')
    ;""")


@app.route('/')
def root():
    try:
        user = session['user']
        status = session['logged_in']
    except:
        user = 'guest'
        status = 'logged out'
    
    return '<h2>Login Status</h2><br><h3>Go to the /home to Login</h3><strong>User: </strong><span>%s</span><br><strong>Status: </strong><span>%s</span>' % (user, status)

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # get form fields
        username = request.form['username']
        password_candidate = request.form['password']
        

        # create cursor
        cur = mysql.connection.cursor()
        
        #Un-parameterized Input 
        #result = cur.execute(f"SELECT * FROM users WHERE username = '{username}'")
        #result = cur.execute("SELECT * FROM users WHERE username = '{}'".format(username))
        
        # Parametrized Input 
        result = cur.execute("SELECT * FROM users WHERE username = %s", [username])

        if result > 0:
            # get stored hash
            data = cur.fetchone()
            password = data['password']
            
            # compare password
            if password_candidate == password:
                session['logged_in'] = True
                session['user'] = username

                return redirect(url_for('root'))
            else:
                error = "Invalid password!"
                return error
            
            # close connection
            cur.close()
        
        else:
            error = "Thank you for your submission, You are now part of my secure database"
            return error
    
    return render_template('index.html')
    
# logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('root'))


if __name__ == '__main__':
    app.run(debug=True)
