#!/usr/bin/python3
"""This is the base class of the project"""
import json
import os
import csv
import turtle

class Base:
    """this is the base class for the project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor method
        Args:
            id (always int): identification for all classes
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        return json.dumps(list_dictionaries)
    
    @staticmethod
    def from_json_string(json_string):
        """
        returns a list of the json string representation of json_string
        """
        if json_string is None or len (json_string) == 0:
            return []
        return json.loads(json_string)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """"writes a Json string representation to a file"""
        filename = "{}.json".format(cls.__name__)
        with open(filename, mode="w", encoding="utf-8") as file:
            if list_objs is None or len(list_objs) < 1:
                file.write('[]')
            else:
                diction = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(diction))
    
    @classmethod
    def create(cls, **dictionary):
        """
            Returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(2, 1)
        elif cls.__name__ == "Square":
            dummy = cls(4)
        dummy.update(**dictionary)
        return dummy
    
    @classmethod
    def load_from_file(cls):
        """
            returns a list of instances contained in a file
        """
        filename = "{}.json".format(cls.__name__)
        ls_instances = [] #to hold instances of the class
        ls_dicts = [] #to hold dictionaries loaded from the Json file
        if os.path.exists(filename): #check  if file exists, open if do
            with open(filename, mode='r') as F:
                js_str = F.read()
                ls_dicts = cls.from_json_string(js_str) #decode json string into list of dictionaries
            for dct in ls_dicts: #loop over each dictionary
                ls_instances.append(cls.create(**dct)) #create instances
        return ls_instances
