#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from flask import request, make_response
from . import app


@app.route('/', methods=['GET'])
def index():
    data = []
    for i in range(1000):
        hash = random.getrandbits(128)
        data.append(hash)
    str_out = 0
    for i in data:
        str_out += int(str_out) + i
    return make_response(str(str_out), 200) 
