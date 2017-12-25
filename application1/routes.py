from application1 import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
	some1 = {'username': 'mike'}
	postser = [
	{
		'author': {'username': 'John'},
		'body' : 'Beuatiful day in Portland!'
	},
	{
		'author' : {'username': 'Susan'},
		'body' : 'The Avengers is a cool movie'
	}
	]

	return render_template('index.html', title='Home', user=some1, posts=postser)

''' 

@app.route('/test1/<name>')
def index1(name):
	some1 = {'username': name+"\'s"}
	return render_template('index.html', title='Home', user=some1)
'''

