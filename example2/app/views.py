#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alvin Lawson
# @Date:   2015-05-11 12:40:10
# @Last Modified by:   Alvin Lawson
# @Last Modified time: 2015-05-11 12:40:28
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"