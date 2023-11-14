from flask import jsonify
from models import Address, Parent, Child

class ProfileService:
    
    def __init__(self, data):
        self.data = data
    
    #Create New User 
    @staticmethod
    def create_user(data,mongo):
        required_fields = ['user_id', 'first_name', 'last_name']
        if any(field not in data for field in required_fields):
            return {'error': 'Missing required fields'}, 400
       
        # Check if user_type is valid
        if data['user_type'] not in ['Parent', 'Child']:
            return {'error': 'Invalid user type'}, 400

        # Create User
        if data['user_type'] == 'Parent':
            address = Address(
                street=data.get('address_street'),
                city=data.get('address_city'),
                state=data.get('address_state'),
                zip_code=data.get('address_zip')
            )
            user = Parent(
                user_id=data['user_id'],  
                first_name=data['first_name'],
                last_name=data['last_name'],
                address=address
            )
        elif data['user_type'] == 'Child':
            if 'parent_id' not in data:
                return {'error': 'Missing parent_id for Child'}, 400
            user = Child(
                user_id=data['user_id'],  
                first_name=data['first_name'],
                last_name=data['last_name'],
                parent_id=data['parent_id']
            )
            
        # Insert User into DB
        user_dict = user.to_dict()
        result = mongo.db.users.insert_one(user_dict)

        return {'message': 'User created successfully', 'user_id': user.user_id}, 201

    #

    #Get All Users Info
    @staticmethod
    def get_all_users(self,mongo):
        
            users = list(mongo.db.users.find())
            user_list = []
            for user in users:
                if user['user_type'] == 'Parent':
                    parent_address = None
                    if 'address' in user:
                        parent_address = Address(**user['address'])
                        user_list.append(Parent(
                            user_id=str(user['_id']),
                            first_name=user['first_name'],
                            last_name=user['last_name'],
                            address=parent_address,
                        ).to_dict())
                else:
                    parent = mongo.db.users.find_one({'_id': user['parent_id']})
                    parent_address = None
                    if parent and parent['user_type'] == 'Parent' and 'address' in parent:
                       parent_address = Address(**parent['address'])
                    user_list.append(Child(
                        user_id=str(user['_id']),
                        first_name=user['first_name'],
                        last_name=user['last_name'],
                        parent_id=user['parent_id'],
                        address = parent_address       
                    ).to_dict())

            return user_list, 200
        
    #Update User
    @staticmethod
    def update_user(data,user_id,mongo):
        
        # # Check if user_type is valid
        if data['user_type'] not in ['Parent', 'Child']:
            return {'error': 'Invalid user type'}, 400

        # Update User
        if data['user_type'] == 'Parent':
            address = Address(
                street=data.get('address_street'),
                city=data.get('address_city'),
                state=data.get('address_state'),
                zip_code=data.get('address_zip')
            )
            user = Parent(
                user_id=user_id,  
                first_name=data['first_name'],
                last_name=data['last_name'],
                address=address
            )
        else:
            user = Child(
                user_id=user_id,  
                first_name=data['first_name'],
                last_name=data['last_name'],
                parent_id=data['parent_id']
            )

        # Update User in DB
        updated_user_dict = user.to_dict()
        result = mongo.db.users.update_one({'_id': user_id}, {'$set': updated_user_dict})

        if result.modified_count == 0:
            return {'error': 'User not found'}, 404

        return {'message': 'User updated successfully'}
    
    

    #Delete user
    @staticmethod
    def delete_user(user_id,mongo):
        
        result = mongo.db.users.delete_one({'_id': user_id})

        if result.deleted_count == 0:
            return {'error': 'User not found'}, 404

        return {'message': 'User deleted successfully'}
        
    
