#!/usr/bin/env python

from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def index() :
    return "<h1>Hello World</h1>"

@app.route('/user/<name>')
def user(name) :
    return f"<h1>Hello {name}</h1>" + f"Your browser is {request.headers.get('User-Agent')}"

if __name__ == "__main__" :
    app.run()
