from bson import ObjectId

class Address:
    def __init__(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

class Parent:
    def __init__(self, user_id, first_name, last_name, address):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def to_dict(self):
        return {
            '_id': self.user_id, 
            'user_type': 'Parent',
            'first_name': self.first_name,
            'last_name': self.last_name,
            'address': vars(self.address) if self.address else None,
        }

class Child(Parent):
    def __init__(self, user_id, first_name, last_name, parent_id,address=None):
        super().__init__(user_id, first_name, last_name,address)
        self.parent_id = parent_id

    def to_dict(self):
        child_dict = super().to_dict()
        child_dict.update({
            'user_type': 'Child',
            'parent_id': self.parent_id,
        })
        if self.address:
            child_dict['address'] = vars(self.address)
        else:
            child_dict['address'] = None
        return child_dict