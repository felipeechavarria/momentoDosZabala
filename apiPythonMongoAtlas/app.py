from flask import Flask, jsonify, request
from flask_cors import CORS 
import pymongo 
from bson import ObjectId


connection_url = 'mongodb://localhost/'
app = Flask(__name__) 
client = pymongo.MongoClient(connection_url) 

Database = client.get_database('citasMedicasdb')
db = Database.dates 


@app.route('/DatePost', methods= ['POST'])
def createDate():
    id = db.insert({
        'identification':request.json['identification'],
        'name':request.json['name'],
        'lastname':request.json['lastname'],
        'birthdate':request.json['birthdate'],
        'city':request.json['city'],
        'neighborhood':request.json['neighborhood'],
        'phone':request.json['phone']
    })
    return jsonify(str(ObjectId(id)))
    

@app.route('/GetDates', methods= ['GET'])
def getDates():
    dates = []
    for doc in db.find():
        dates.append({
            '_id':str(ObjectId(doc['_id'])),
            'name':doc['name'],
            'lastname':doc['lastname'],
            'identification':doc['identification'],
            'birthdate':doc['birthdate'],
            'city':doc['city'],
            'neighborhood':doc['neighborhood'],
            'phone':doc['phone']
        })
    return jsonify(dates)

@app.route('/GetDate/<id>', methods= ['GET'])
def getDate(id):
    date = db.find_one({'_id': ObjectId(id)})
    print(date)
    return jsonify({
        '_id': str(ObjectId(date['_id'])),
        'name': date['name'],
        'lastname': date['lastname'],
        'identification': date['identification'],
        'birthdate': date['birthdate'],
        'city': date['city'],
        'neighborhood': date['neighborhood'],
        'phone': date['phone']    
    })      

@app.route('/Deletedate/<id>', methods= ['DELETE'])
def deleteDate(id):
    db.delete_one({'_id':ObjectId(id)})
    return jsonify({'msg': 'Cita Eliminado'})

@app.route('/PutDate/<id>', methods= ['PUT'])
def updateDate(id):
    db.update_one({'_id':ObjectId(id)}, {'$set': {
        'name':request.json['name'],
        'lastname':request.json['lastname'],
        'identification':request.json['identification'],
        'birthdate':request.json['birthdate'],
        'city':request.json['city'],
        'neighborhood':request.json['neighborhood'],
        'phone':request.json['phone']
    }})
    return jsonify({'msg': 'Cita actualizado'})
  
if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=4000)