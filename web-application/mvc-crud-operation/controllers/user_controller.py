from flask import Blueprint, request, jsonify
from models.user_model import UserModel

user_controller = Blueprint('user_controller', __name__)

@user_controller.route('/signup', methods=['POST'])
def insert_record():
    data = request.json
    if not data or 'name' not in data or 'email' not in data or 'password' not in data:
        return jsonify({"Status": "Invalid input"}), 400

    response, error = UserModel.create(data['name'], data['email'], data['password'])
    if error:
        return jsonify({"Status": error}), 400
    return jsonify(response), 201

@user_controller.route('/read', methods=['GET'])
def read_record():
    records, error = UserModel.get_all()
    if error:
        return jsonify({"Status": error}), 500
    return jsonify(records), 200

@user_controller.route('/update/<int:user_id>', methods=['PUT'])
def update_record(user_id):
    data = request.json
    if not data or 'name' not in data:
        return jsonify({"Status": "Invalid input"}), 400

    response, error = UserModel.update(user_id, data['name'])
    if error:
        return jsonify({"Status": error}), 400
    return jsonify(response), 200

@user_controller.route('/delete/<int:user_id>', methods=['DELETE'])
def delete_record(user_id):
    response, error = UserModel.delete(user_id)
    if error:
        return jsonify({"Status": error}), 400
    return jsonify(response), 200