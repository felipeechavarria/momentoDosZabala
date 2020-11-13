from flask import Flask, jsonify, request
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS

app = Flask (__name__)
app.config['MONGO_URI']= 'mongodb://localhost/citasMedicasdb'
mongo = PyMongo(app)

db = mongo.db.dates

@app.route('/dates', methods= ['POST'])
def createDate():
    id = db.insert({
        'name':request.json['name'],
        'lastname':request.json['lastname'],
        'identification':request.json['identification'],
        'birthdate':request.json['birthdate'],
        'city':request.json['city'],
        'neighborhood':request.json['neighborhood'],
        'phone':request.json['phone']
    })
    return jsonify(str(ObjectId(id)))
    

@app.route('/dates', methods= ['GET'])
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

@app.route('/dates/<id>', methods= ['GET'])
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

@app.route('/dates/<id>', methods= ['DELETE'])
def deleteDate(id):
    db.delete_one({'_id':ObjectId(id)})
    return jsonify({'msg': 'Cita Eliminado'})

@app.route('/dates/<id>', methods= ['PUT'])
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
    app.run(debug=True)