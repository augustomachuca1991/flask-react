from flask import Flask
from flask_cors import CORS
import mysql.connector
from connection import connect_db

app = Flask(__name__)
CORS(app)




# Members API Route

@app.route("/users", methods=['GET' , 'POST'])
def users():
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM `users`;"
    cursor.execute(query)
    users = cursor.fetchall()
    conn.close()
    return {"users" : users}

@app.route("/")
def home():
    return "Esta es la home"

if __name__ == "__main__":
    app.run(debug=True)

