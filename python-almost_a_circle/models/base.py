#!/usr/bin/python3

"""module for a class"""
import json
import os.path


class Base:
    """class for some shapes"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """func to convert to json string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        my_list = json.dumps(list_dictionaries)
        return my_list

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        Class method to save json represantation of
        object files
        '''

        with open(f"{cls.__name__}.json", "w+") as file_js:
            if list_objs is None:
                file_js.write(json.dumps([]))
                return
            list_of_dictionaries = []
            for objs in list_objs:
                if issubclass(objs.__class__, Base):
                    list_of_dictionaries.append(objs.to_dictionary())
            file_js.write(Base.to_json_string(list_of_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        '''
        Function that returns the list
        of the json_string representation
        '''

        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
        Function that creates an instance
        from dictionary given
        '''
        if cls.__name__ == 'Rectangle':
            new_instance = cls(1, 1)
        if cls.__name__ == 'Square':
            new_instance = cls(1)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        '''
        Function that returns a list of instances
        '''
        if os.path.isfile(f"{cls.__name__}.json"):
            with open(f"{cls.__name__}.json") as text_json:
                obj_dict = cls.from_json_string(text_json.read())
                obj_list = []
                for dictionaries in obj_dict:
                    new_obj = cls.create(**dictionaries)
                    obj_list.append(new_obj)
                return obj_list
        else:
            return []
