import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, jsonify
from Service import ProfileService

class TestProfileService(unittest.TestCase):

    def setUp(self):
        self.mock_mongo = MagicMock()

    def test_create_user_parent(self):

        data = {
            'user_type': 'Parent',
            'user_id': '123',
            'first_name': 'John',
            'last_name': 'Doe',
            'address_street': '123 Main St',
            'address_city': 'City',
            'address_state': 'State',
            'address_zip': '12345'
        }


        response,status_code = ProfileService.create_user(data, self.mock_mongo)
        
        expected_response = {'message': 'User created successfully', 'user_id': '123'}
        self.assertEqual(response, expected_response)
        self.assertEqual(status_code, 201)
        self.mock_mongo.db.users.insert_one.assert_called_once()

    def test_create_user_child(self):

        data = {
            'user_type': 'Child',
            'user_id': '123',
            'first_name': 'Jane',
            'last_name': 'Doe',
            'parent_id': '456'
        }


        response,status_code = ProfileService.create_user(data, self.mock_mongo)

        expected_response = {'message': 'User created successfully', 'user_id': '123'}
        self.assertEqual(response, expected_response)
        self.assertEqual(status_code, 201)
        self.mock_mongo.db.users.insert_one.assert_called_once()

    def test_get_all_users(self):

        response, status_code = ProfileService.get_all_users(self.mock_mongo)

        expected_response = [],200
        self.assertEqual((response,status_code), expected_response)
        self.mock_mongo.db.users.find.assert_called_once()

    def test_update_user_parent(self):

        user_id = '123'
        data = {
            'user_type': 'Parent',
            'first_name': 'John',
            'last_name': 'Doe',
            'address_street': '456 New St',
            'address_city': 'New City',
            'address_state': 'New State',
            'address_zip': '54321'
        }

        response = ProfileService.update_user(data, user_id, self.mock_mongo)
        
        expected_response = {'message': 'User updated successfully'}
        self.assertEqual(response, expected_response)
        self.mock_mongo.db.users.update_one.assert_called_once()

    def test_delete_user(self):
        user_id = '123'

        response = ProfileService.delete_user(user_id, self.mock_mongo)
            
        expected_response = {'message': 'User deleted successfully'}
        self.assertEqual(response, expected_response)
        self.mock_mongo.db.users.delete_one.assert_called_once()

if __name__ == '__main__':
    unittest.main()
