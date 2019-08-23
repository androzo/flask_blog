from flask import Flask, render_template, url_for

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
	app.run(debug=True)
