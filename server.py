from flask import Flask, request, jsonify
import json
import pymysql
import sqlite3

app = Flask(__name__)

# Hard coded name list
name_list = [
    {
        "id": 0,
        "name": "Jay",
        "age": "19"
    },
    {
        "id": 1,
        "name": "Frank",
        "age": "15"
    }
    ]


def db_connection():
    conn = None
    try:
        conn = sqlite3.conntect('books.sqlite')
    except sqlite3.error as e:
        print(e)
    return conn


@app.route('/')
def index():
    return "Hello World"


# GET/POST all of the names
@app.route('/names', methods=['GET', 'POST'])
def names():
    conn = db_connection()
    cursor = conn.cursor()
    if request.method == 'GET':
        if len(name_list) > 0:
            return jsonify(name_list)
        else:
            "Nothing found", 404
    if request.method == 'POST':
        new_name = request.form['name']
        new_age = request.form['age']
        iD = name_list[-1]['id'] + 1

        new_obj = {
            'id': iD,
            'name': new_name,
            'age': new_age
        }
        name_list.append(new_obj)
        return jsonify(new_obj), 201


# GET/PUT/DELETE single name
@app.route('/names/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_name(id):
    if request.method == 'GET':
        for name in name_list:
            if name['id'] == id:
                return jsonify(name)
            pass
    elif request.method == 'PUT':
        for name in name_list:
            if name['id'] == id:
                new_name = request.form['name']
                new_age = request.form['age']
                iD = name_list[-1]['id'] + 1

                new_obj = {
                    'id': iD,
                    'name': new_name,
                    'age': new_age
                }
                name_list.append(new_obj)
                return jsonify(new_obj), 201
    elif request.method == 'DELETE':
        for index, name in enumerate(name_list):
            if name['id'] == id:
                name_list.pop(index)
                return jsonify(name_list)


if __name__ == '__main__':
    app.run(debug=True)