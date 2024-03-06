#!/usr/bin/python3
"""
Base Model Module

This module contains the base model class for other models.
"""
import uuid
from datetime import datetime
class BaseModel:
    """
    Base Model Class

    Attributes:
        id (str): A unique identifier for the object.
        created_at (datetime): The timestamp when the object was created.
        updated_at (datetime): The timestamp when the object was last updated.
    """
    def __init__(self):
         """Initialize a new BaseModel object."""
         self.id = str(uuid.uuid4())
         self.created_at = datetime.utcnow()
         self.updated_at = datetime.utcnow()

    def save(self):
        """Update the 'updated_at' attribute to the current time."""
        self.updated_at = datetime.utcnow()

    def __str__(self):
        """Return a string representation of the object."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def to_dict(self):
        """Convert the object to a dictionary."""
        instance_dict = self.__dict__.copy()
        instance_dict.update({
            "__class__": self.__class__.__name__,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
            })
        return instance_dicit

if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
