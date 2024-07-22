from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    return 'form submitted'
