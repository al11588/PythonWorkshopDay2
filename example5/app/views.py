#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alvin Lawson
# @Date:   2015-05-11 12:40:10
# @Last Modified by:   Alvin Lawson
# @Last Modified time: 2015-05-11 12:50:34
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Alvin'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user)
