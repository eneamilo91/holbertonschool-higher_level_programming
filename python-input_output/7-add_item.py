#!/usr/bin/python3

"""module to manipulate file"""
import json
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


my_list = []

for i in range(1, len(argv)):
    my_list.append(argv)

save_to_json_file(my_list, "add_item.json")
load_from_json_file("add_item.json")
