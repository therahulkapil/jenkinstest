from flask import Flask, jsonify
from flask_pymongo import PyMongo
from pymongo import MongoClient

app = Flask(__name__)

def get_db():
    client = MongoClient(host='kapil-pc',
                         port=27017, 
                         username='Rahul', 
                         password='12345',
                        authSource="admin")
    db = client["animal_db"]
    return db

@app.route('/')
def ping_server():
    return "Welcome to the world of animals."

@app.route('/animals')
def fetch_animals():
    db = get_db()
    _animals = db.animal_tb.find()
    animals = [{"id": animal["id"], "name": animal["name"], "type": animal["type"]} for animal in _animals]
    return jsonify({"animals": animals})
    

if __name__=='__main__':
    app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)
