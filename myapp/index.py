# -*- coding: utf-8 -*-
from ..bottle import route, run, template

# @route('/hello/<name>')
# def index(name):
#     return template('<b>Hello {{name}}</b>!', name=name)

# run(host='localhost', port=8000)


@route("/object/<id:int>")
def callback(id):
    assert isinstance(id, int)
    return "hello world"

run(host="localhost", port=8000)