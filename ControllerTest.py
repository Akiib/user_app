import unittest
from bson import ObjectId
from models import Address,Parent,Child

class TestAddress(unittest.TestCase):
    def test_address_creation(self):
        address = Address("Shah Habibullah Road", "CTG", "CTG", "4213")
        self.assertEqual(address.street, "Shah Habibullah Road")
        self.assertEqual(address.city, "CTG")
        self.assertEqual(address.state, "CTG")
        self.assertEqual(address.zip_code, "4213")

class TestParent(unittest.TestCase):
    def test_parent_creation(self):
        address = Address("113 M.M Lane", "Chattogram", "CTG", "4203")
        parent = Parent("123", "John", "Doe", address)

        self.assertEqual(parent.user_id, "123")
        self.assertEqual(parent.first_name, "John")
        self.assertEqual(parent.last_name, "Doe")
        self.assertEqual(parent.address.street, "113 M.M Lane")

    def test_parent_to_dict(self):
        address = Address("113 M.M Lane", "Chattogram", "CTG", "4203")
        parent = Parent("123", "John", "Doe", address)
        parent_dict = parent.to_dict()

        self.assertEqual(parent_dict['_id'], '123')
        self.assertEqual(parent_dict['user_type'], 'Parent')
        self.assertEqual(parent_dict['first_name'], 'John')
        self.assertEqual(parent_dict['last_name'], 'Doe')
        self.assertEqual(parent_dict['address']['street'], '113 M.M Lane')

class TestChild(unittest.TestCase):
    def test_child_creation(self):
        parent_address = Address("113 M.M Lane", "Chattogram", "CTG", "4203")
        parent = Parent("123", "John", "Doe", parent_address)

        child = Child("111", "Jane", "Doe", parent.user_id)

        self.assertEqual(child.user_id, "111")
        self.assertEqual(child.first_name, "Jane")
        self.assertEqual(child.last_name, "Doe")
        self.assertEqual(child.parent_id, parent.user_id)

    def test_child_to_dict(self):
        parent_address = Address("113 M.M Lane", "Chattogram", "CTG", "4203")
        parent = Parent("123", "John", "Doe", parent_address)

        child = Child("111", "Jane", "Doe", parent.user_id)
        child_dict = child.to_dict()

        self.assertEqual(child_dict['_id'], '111')
        self.assertEqual(child_dict['user_type'], 'Child')
        self.assertEqual(child_dict['first_name'], 'Jane')
        self.assertEqual(child_dict['last_name'], 'Doe')
        self.assertEqual(child_dict['parent_id'], parent.user_id)
        self.assertIsNone(child_dict['address'])


if __name__ == '__main__':
    unittest.main()
