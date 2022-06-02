from flask import Blueprint, jsonify, request
from sqlalchemy import null

# Entities
from models.entities.User import User

# Models
from models.UserModel import UserModel

main = Blueprint('user_blueprint', __name__)

@main.route('/')
def get_users():
    try:
        users = UserModel.get_users()
        return jsonify(users)
    except Exception as ex:
        return jsonify({'message': f'{str(ex)}'}), 500

@main.route('/<id>')
def get_user(id):
    try:
        user = UserModel.get_user(id)
        if user != None:
            return jsonify(user)
        else:
            return jsonify({'error': f'There is no register with the id: {id}'}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/add', methods = ['POST'])
def add_user():
    try:
        userName = request.json['userName']
        userPwd = request.json['userPwd']
        # EL CONSTRUCTOR USA LOS PARAMETROS DE ACA PARA USARLOS EN LA CONSULTA DEL MODELO
        # PODEMOS PASAR NULL EL ID Y EL DATE PQ EN LA BD ESO SE HACE AUTOMATICAMENTE, POR LO QUE LOS VALORES CAMBIAN AL INSERTAR
        user = User(null, userName, userPwd, null) 

        affected_rows = UserModel.add_user(user)

        if affected_rows == 1:
            return jsonify(f'The user: {user.userName}, was successfully added')
        else:
            return jsonify({'message': "Error on insert"}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/update/<id>', methods=['PUT'])
def update_user(id):
    try:
        userName = request.json['userName']
        userPwd = request.json['userPwd']
        user = User(id, userName, userPwd, null)

        affected_rows = UserModel.update_user(user)

        if affected_rows == 1:
            return jsonify(f'The user: {user.userName}, was successfully updated')
        else:
            return jsonify({'message': "No user updated"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/delete/<id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = User(id)

        affected_rows = UserModel.delete_user(user)

        if affected_rows == 1:
            return jsonify(f'The user with id: {user.userId}, was successfully deleted')
        else:
            return jsonify({'message': "No user deleted"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500