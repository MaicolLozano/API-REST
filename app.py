from flask import Flask, request, jsonify
import  mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test",
    port="3307"
)

@app.route('/empleados', methods=['GET'])
def get_users():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM user")
    myresult = cursor.fetchall()
    return jsonify(myresult)

@app.route('/empleados/<int:id>', methods=['GET'])
def get_user(id):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM user WHERE id = %s", (id,))
    myresult = cursor.fetchone()
    return jsonify(myresult)

@app.route('/empleados', methods=['POST'])
def create_user():
    cursor = mydb.cursor()
    name = request.json['name']
    age = request.json['age']
    cursor.execute("INSERT INTO user (name, age) VALUES (%s, %s)", (name, age))
    mydb.commit()
    return jsonify({"message": "User created"})

@app.route('/empleados/<int:id>', methods=['PUT'])
def update_user(id):
    cursor = mydb.cursor()
    name = request.json['name']
    age = request.json['age']
    cursor.execute("UPDATE user SET name = %s, age = %s WHERE id = %s", (name, age, id))
    mydb.commit()
    return jsonify({"message": "User updated"})

@app.route('/empleados/<int:id>', methods=['DELETE'])
def delete_user(id):
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM user WHERE id = %s", (id,))
    mydb.commit()
    return jsonify({"message": "User deleted"})

if __name__ == '__main__':
    app.run(debug=True)