from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def indexGrandPy():
	
	return render_template('index.html')	


@app.route('/', methods=['POST'])
def formGrandPy():
	
	post = request.form['post']

	return post