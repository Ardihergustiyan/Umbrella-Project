from flask import Flask, redirect, url_for, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)