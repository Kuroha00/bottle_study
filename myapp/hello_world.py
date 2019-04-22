# -*- coding: utf-8 -*-
from ..bottle import route, run, Bottle, template

# オブジェクト指向的な記述
# app = Bottle()

# @app.route("/hello")
# def hello():
#     return "Hello World"

# # ビルトインのWebサーバが起動
# run(app, host="localhost", port=8000)



# ルートがデフォルトアプリケーションに複数追加
# 
@route("/")
@route("/hello/<name>")
# def greet(name='Stranger'):
#     return template('Hello {{name}}, how are you?', name=name)
def hello():
    return "hello world"

run(host="local_host", port=8000)

