#-*-coding=utf-8-*-

from flask import Flask,url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello,World!'

@app.route('/abc')
def abc():
	return 'abc'

with app.test_request_context():
	print(url_for('hello_world'))
	print(url_for('abc'))

if __name__ == '__main__':
	app.run()