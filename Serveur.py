#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from waitress import serve #serveur de production
from flask import Flask #serveur web python

import random

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def hello_world():
    return "<h1> Hello World! </h1>"

@app.route('/test')
def display_random_list():
    return random_list()

def random_list():
    list = []
    for i in range(0,5):
        list.append(random.randint(1,10))
    return list

serve(app, host='0.0.0.0', port=30080)