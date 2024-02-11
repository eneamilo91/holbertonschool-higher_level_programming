#!/usr/bin/python3

"""module to perform action"""
import json


def class_to_json(obj):
    """func to convert to json"""
    return json.dumps(obj.__dict__)
