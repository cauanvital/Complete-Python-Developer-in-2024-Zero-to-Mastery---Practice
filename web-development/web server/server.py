from flask import Flask, render_template, url_for

app = Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/<username>')
def blog(username=None):
    return render_template('index.html', name=username)

@app.route('/<username>/<int:post_id>')
def blog_2020_dogs(username=None, post_id=None):
    return render_template('index.html', name=username, post_id=post_id)
