from flask import Flask, request, jsonify
import json
import pymysql

app = Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = pymysql.connect(
            host='sql5.freesqldatabase.com',  
            database='sql5528137',
            user='sql5528137',
            password='l5Fmqx2StM',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
    except pymysql.Error as e:
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
        cursor.execute("SELECT * FROM name")
        names = [
            dict(id=row['id'], name=row['name'], age=row['age'])
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
                 VALUES (%s, %s)"""
        cursor = cursor.execute(sql, (new_name, new_age))
        conn.commit()
        
        return f"name with the id: {cursor.lastrowid} created successfuly", 201


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