from flask import Flask, request, jsonify
from bson import ObjectId
from models import Address, Parent, Child
from Service import ProfileService


def create_user(app,mongo):
    # API to create a user
    @app.route('/api/users', methods=['POST'])
    def create_user():
        data = request.get_json()
        # response = ProfileService.create_user(data,mongo)
        try:
            response = ProfileService.create_user(data,mongo)
        except Exception as e:
            return jsonify({'error': 'Invalid data input'}), 400
        return response


def get_all_users(app,mongo):
    # API to show all users
    @app.route('/api/users', methods=['GET'])
    def get_all_users():
        response = ProfileService.get_all_users(app,mongo)
        return response


def update_user(app,mongo):
    # API to update user data
    @app.route('/api/users/<string:user_id>', methods=['PUT'])
    def update_user(user_id):
        data = request.get_json()
        
        try:
            response = ProfileService.update_user(data,user_id,mongo)
        except Exception as e:
            return jsonify({'error': 'Invalid data input'}), 400
        return response


def delete_user(app,mongo):
    # API to delete user data
    @app.route('/api/users/<string:user_id>', methods=['DELETE'])
    def delete_user(user_id):
        response = ProfileService.delete_user(user_id,mongo)
        return response
        
