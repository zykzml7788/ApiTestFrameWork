#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 22:34
# @Author  : uncleyong
# @Blog    : http://www.cnblogs.com/UncleYong
# @Gitee   : https://gitee.com/UncleYong
# @QQ交流群 : 66719336


from flask import Flask, jsonify, g
import copy

app = Flask(__name__)


@app.before_request
def init_data():
    g.data = [
        {'id': 1, 'uname': 'tom'},
        {'id': 2, 'uname': 'jack'},
        {'id': 3, 'uname': 'lucy'}
    ]

    g.user_does_not_exist = {"code": "01", "msg": "user does not exist"}


@app.route('/api/user')
def get_all_users():
    print(type(jsonify(g.data)))
    return jsonify({"code": "00", "msg": g.data})


@app.route('/api/user/<int:user_id>')
def get_user(user_id):
    if user_id > 0 and user_id <= len(g.data):
        return jsonify({"code": "00", "msg": g.data[user_id - 1]})
    else:
        return jsonify(g.user_does_not_exist)

if __name__ == '__main__':
    app.run()