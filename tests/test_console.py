#!/usr/bin/python3
import os
import pep8
import unittest
import json
from datetime import datetime
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage


class TestHBNBCommandDocs(unittest.TestCase):
    """ Documentation check"""
    def test_class_doc(self):
        """ check for class documentation """
        self.assertTrue(len(HBNBCommand.__doc__) > 0)


class TestHBNBCommandPep8(unittest.TestCase):
    """ check for pep8 validation """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'console.py'
        file2 = 'tests/test_console.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestHBNBCommand(unittest.TestCase):
    """ HBNBCommand class test """
    pass
