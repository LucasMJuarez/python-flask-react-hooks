from flask import Flask, jsonify, request
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS


app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost/pythonreactdb'
mongo = PyMongo(app)  # devuelve un objeto que interactua como una conexion

# simil middleware de express
CORS(app)

# Database
# defino una colecion de usuarios en forma abreviada como db
db = mongo.db.users


# Definimos las rutas para el CRUD

@app.route('/users', methods=['POST'])
def createUser():
    print(request.json)
    id = db.insert({
        'name': request.json['name'],
        'email': request.json['email'],
        'password': request.json['password']
    })
    return jsonify(str(ObjectId(id)))


@app.route('/users', methods=['GET'])
def getUsers():
    users = []
    for doc in db.find():
        users.append({
            '_id': str(ObjectId(doc['_id'])),
            'name': doc['name'],
            'email': doc['email'],
            'password': doc['password']
        })
    return jsonify(users)


@app.route('/users/<id>', methods=['GET'])
def getUser(id):
    user = db.find_one({'_id': ObjectId(id)})
    print(user)
    return jsonify({
        '_id': str(ObjectId(user['_id'])),
        'name': user['name'],
        'email': user['email'],
        'password': user['password']
    })


@app.route('/users/<id>', methods=['DELETE'])
def deleteUser(id):
    db.delete_one({'_id': ObjectId(id)})
    return jsonify({'message': 'User deleted'})


@app.route('/users/<id>', methods=['PUT'])
def updateUser(id):
    print(request.json)
    db.update_one({'_id': ObjectId(id)}, {"$set": {
        'name': request.json['name'],
        'email': request.json['email'],
        'password': request.json['password']
    }})
    return jsonify({'msg': 'User updated'})


# Inicializamos el paquete


if __name__ == "__main__":
    # cuando llamen arranca la app con debug en true para que se ejecute solo ante cualquier cambio
    app.run(debug=True)
