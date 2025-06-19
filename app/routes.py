from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from . import mongo
from .schemas import UserSchema

users_bp = Blueprint('users', __name__, url_prefix='/users')
user_schema = UserSchema()
users_schema = UserSchema(many=True)

@users_bp.route('/', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    return jsonify(users_schema.dump(users)), 200

@users_bp.route('/<id>', methods=['GET'])
def get_user(id):
    try:
        user = mongo.db.users.find_one({"_id": ObjectId(id)})
        if not user:
            return jsonify({"message": "User not found"}), 404
        return jsonify(user_schema.dump(user)), 200
    except Exception:
        return jsonify({"message": "Invalid ID format"}), 400

@users_bp.route('/', methods=['POST'])
def create_user():
    user_data = request.get_json()
    try:
        validated_data = user_schema.load(user_data)
    except Exception as err:
        return jsonify(err.messages), 400

    hashed_password = generate_password_hash(validated_data['password'])
    validated_data['password'] = hashed_password

    result = mongo.db.users.insert_one(validated_data)
    created_user = mongo.db.users.find_one({"_id": result.inserted_id})
    return jsonify(user_schema.dump(created_user)), 201

@users_bp.route('/<id>', methods=['PUT'])
def update_user(id):
    user_data = request.get_json()
    try:
        validated_data = user_schema.load(user_data, partial=True)
    except Exception as err:
        return jsonify(err.messages), 400

    try:
        user = mongo.db.users.find_one({"_id": ObjectId(id)})
        if not user:
            return jsonify({"message": "User not found"}), 404

        if 'password' in validated_data:
            validated_data['password'] = generate_password_hash(validated_data['password'])

        mongo.db.users.update_one({"_id": ObjectId(id)}, {"$set": validated_data})
        updated_user = mongo.db.users.find_one({"_id": ObjectId(id)})
        return jsonify(user_schema.dump(updated_user)), 200
    except Exception:
        return jsonify({"message": "Invalid ID format"}), 400

@users_bp.route('/<id>', methods=['DELETE'])
def delete_user(id):
    try:
        result = mongo.db.users.delete_one({"_id": ObjectId(id)})
        if result.deleted_count == 0:
            return jsonify({"message": "User not found"}), 404
        return jsonify({"message": "User deleted"}), 204
    except Exception:
        return jsonify({"message": "Invalid ID format"}), 400