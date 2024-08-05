#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""

from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pep8
import unittest
DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Test tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestDBStorage(unittest.TestCase):
    """Test the DBStorage class"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_returns_dict(self):
        """Test that all returns a dictionary"""
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_no_class(self):
        """Test that all returns all rows when no class is passed"""
        pass

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_new(self):
        """Test that new adds an object to the database"""
        pass

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_save(self):
        """Test that save properly saves objects to the database"""
        pass

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_create_new_object(self):
        """Test that a new object is created in the database"""
        new_state = State(name="California")
        models.storage.new(new_state)
        models.storage.save()
        self.assertIn(new_state.id, models.storage.all(State).keys())

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_read_object(self):
        """Test that an object can be read from the database"""
        new_city = City(name="San Francisco", state_id="test_state_id")
        models.storage.new(new_city)
        models.storage.save()
        city = models.storage.get(City, new_city.id)
        self.assertIsNotNone(city)
        self.assertEqual(city.name, "San Francisco")

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_update_object(self):
        """Test that an object's attributes can be updated in the database"""
        new_user = User(email="test@example.com", password="password")
        models.storage.new(new_user)
        models.storage.save()
        new_user.first_name = "Test"
        models.storage.save()
        updated_user = models.storage.get(User, new_user.id)
        self.assertEqual(updated_user.first_name, "Test")

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_delete_object(self):
        """Test that an object can be deleted from the database"""
        new_amenity = Amenity(name="Wi-Fi")
        models.storage.new(new_amenity)
        models.storage.save()
        models.storage.delete(new_amenity)
        models.storage.save()
        self.assertIsNone(models.storage.get(Amenity, new_amenity.id))

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_invalid_data_type(self):
        """Test storing an object with an invalid data type"""
        with self.assertRaises(TypeError):
            invalid_state = State(name=12345)  # Name should be a string
            models.storage.new(invalid_state)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_duplicate_objects(self):
        """Test storing duplicate objects"""
        new_user1 = User(email="duplicate@example.com", password="password")
        new_user2 = User(email="duplicate@example.com", password="password")
        models.storage.new(new_user1)
        models.storage.save()
        with self.assertRaises(Exception):  # Replace Exception with the specific exception if known
            models.storage.new(new_user2)
            models.storage.save()

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_empty_null_values(self):
        """Test storing objects with empty and null values"""
        new_city = City(name="")
        models.storage.new(new_city)
        models.storage.save()
        self.assertEqual(models.storage.get(City, new_city.id).name, "")

        new_place = Place(name=None)
        models.storage.new(new_place)
        models.storage.save()
        self.assertIsNone(models.storage.get(Place, new_place.id).name)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_count_all_objects(self):
        """Test counting all objects in the database"""
        initial_count = models.storage.count()
        new_user = User(email="count@example.com", password="password")
        models.storage.new(new_user)
        models.storage.save()
        self.assertEqual(models.storage.count(), initial_count + 1)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_count_specific_class(self):
        """Test counting objects of a specific class in the database"""
        initial_count = models.storage.count(User)
        new_user = User(email="specific_count@example.com", password="password")
        models.storage.new(new_user)
        models.storage.save()
        self.assertEqual(models.storage.count(User), initial_count + 1)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_get_valid_id(self):
        """Test retrieving an object with a valid ID"""
        new_state = State(name="New York")
        models.storage.new(new_state)
        models.storage.save()
        self.assertEqual(models.storage.get(State, new_state.id), new_state)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_get_invalid_id(self):
        """Test retrieving an object with an invalid ID"""
        self.assertIsNone(models.storage.get(State, "invalid_id"))

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_save_multiple_objects(self):
        """Test saving multiple objects to the database"""
        new_state = State(name="Nevada")
        new_city = City(name="Las Vegas", state_id=new_state.id)
        models.storage.new(new_state)
        models.storage.new(new_city)
        models.storage.save()
        self.assertIn(new_state.id, models.storage.all(State).keys())
        self.assertIn(new_city.id, models.storage.all(City).keys())
