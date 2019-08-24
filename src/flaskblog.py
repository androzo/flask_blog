from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
import connection

""" # Connect to MySQL
conn = connection.connect("database","sys","root","test")

# Disconnect from MySQL
if conn is not None:
    connection.disconnect(conn)
else:
    print("Flask startup aborted")
    exit
 """
app = Flask(__name__)

app.config['SECRET_KEY'] = '357bf5222c435a949b9c2ccc7a82e914'

posts = [
    {
        'author': 'Andre Buchmann',
        'title': 'Blog post 1',
        'content': 'First content',
        'date_posted': 'April 20, 2019'
    },
    {
        'author': 'Andre Buchmann',
        'title': 'Blog post 2',
        'content': 'Second content',
        'date_posted': 'April 22, 2019'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title="Home", posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
	app.run("0.0.0.0", port=80, debug=True)
