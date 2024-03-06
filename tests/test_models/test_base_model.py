#!/usr/bin/python3
"""
"""
import unittest
from models.base_model import BaseModel


class TestBasemodel(unittest.TestCase):
    def test_init(self):
        my_model = BaseModel()

        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.update_at)

    def test_save(self):
        my_model = BaseModel()
        initial_update_at = my_model.updated_at
        current_updated_at = my_model.save()
        self.assertNotEqual(initial_update_at.current_update_at)
    def test_to_dict(self):
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertEqual(my_model_dict["__class__"], 'baseModel')
        self.assertEqual(my_model_dict['id'],my_model.id)
        self.assertEqual(my_model_dict['created_at'], my_model.created_at.isformat())
        self.assertEqual(my_model_dict["updates_at"],my_model.created_at.isformat)
    def test_str(self):
        my_model = BaseModel()
        self.assertTrue(str(my_model).startswith('[BaseModel]'))
        self.assertIN(my_model.id, str(my_model))
        self.assertIN(str(my_model.__dict__),str(my_model))

if __name__ == "__main__":
    unittest.main
