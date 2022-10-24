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
        conn = sqlite3.connect('names.sqlite')
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
        cursor = conn.execute("SELECT * FROM name")
        names = [
            dict(id=row[0], name=row[1], age=row[2])
            for row in cursor.fetchall()
        ]
        if names is not None:
            return jsonify(names)
        else:
            "Nothing found", 404
    if request.method == 'POST':
        new_name = request.form['name']
        new_age = request.form['age']
        sql = """INSERT INTO name (name, age)
                 VALUES (?, ?)"""
        cursor = cursor.execute(sql, (new_name, new_age))
        conn.commit()
        
        return "name with the id: {cursor.lastrowid} created successfuly", 201


# GET/PUT/DELETE single name
@app.route('/names/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_name(id):
    conn = db_connection()
    cursor = conn.cursor()
    name = None
    if request.method == 'GET':
        cursor.execute("SELECT * FROM name WHERE id=?", (id,))
        rows = cursor.fetchall()
        for r in rows:
            name = r
        if name is not None:
            return jsonify(name), 200
        else:
            return "Sum-ting wong", 404
    elif request.method == 'PUT':
        sql = """UPDATE name
                    SET name=?,
                        age=?,
                    WHERE id=? """
        new_name = request.form['name']
        new_age = request.form['age']

        new_obj = {
                'id': iD,
                'name': new_name,
                'age': new_age
            }
        conn.execute(sql, (author, language, title, id))
        conn.commit()
        return jsonify(new_obj), 201
    elif request.method == 'DELETE':
        sql = """ DELETE FROM name WHERE id=? """
        conn.execute(sql, (id,))
        conn.commit()
        return "The book with has been deleted", 200


if __name__ == '__main__':
    app.run(debug=True)