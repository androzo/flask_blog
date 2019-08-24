from flask import Flask, render_template, url_for
#import socket
import connection

# Connect to MySQL
#db_host = socket.gethostbyname('database')
conn = connection.connect("database","sys","root","test")

# Disconnect from MySQL
if conn is not None:
    connection.disconnect(conn)
else:
    print("Flask startup aborted")
    exit

app = Flask(__name__)

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

if __name__ == '__main__':
	app.run("0.0.0.0", port=80, debug=True)