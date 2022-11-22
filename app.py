from flask import Flask,jsonify,request
import pymongo
from pymongo import MongoClient
import os
import json

app = Flask(__name__)

def get_db():
    client = MongoClient('mongodb+srv://therahulkapil:Rftg1234@cluster0.nadjl0x.mongodb.net/?retryWrites=true&w=majority')
    db = client.get_database("animal_db")
    return db
@app.route('/animals')
def get_stored_animals():
    db = get_db()
    _animals = db.animal_tb.find()
    animals = [{"id": animal["id"], "name": animal["name"], "type": animal["type"]} for animal in _animals]
    return jsonify({"animals": animals})

@app.route('/')
def test():
    return "hey this is simple flask app"
@app.route('/add',methods=['POST'])
def animalAdd():
    db = get_db()
    _json = request.json
    _id = _json['id']
    _name = _json['name']
    _type = _json['type']
    if _id and _name and _type and request.method == 'POST':
        id = db.animal_tb.insert_one({'id':_id,'name': _name, 'type': _type})
        resp = jsonify('User added successfully!')
        resp.status_code = 200
        return resp
    else:
        return "not found"
@app.route('/update/<int:id>', methods=['PUT'])
def update_animal(id):
    db = get_db()
    _json = request.json
    _id = _json['id']
    _name = _json['name']
    _type = _json['type']
    if _id and _name and _type and request.method == 'PUT':
        db.animal_tb.update_one({'id':_id},{"$set": {'name': _name,'type':_type}})
        resp = jsonify('User updated successfully!')
        resp.status_code = 200
        return resp
    else:
        return "user not found"
@app.route("/delete/<int:id>", methods=['DELETE'])
def deleteAnimal(id):
    db=get_db()
    _json = request.json
    _id = _json['id'] 
    db.animal_tb.delete_one({'id': _id})
    return "deleted successfully"

if __name__=='__main__':
    port = int(os.environ.get('PORT',5000))
    app.run(host="0.0.0.0",port=port,debug=True)