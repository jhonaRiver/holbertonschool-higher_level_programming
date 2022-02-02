#!/usr/bin/python3
"""
script that adds all arguments to a Python list, and then save them to a file
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    f = load_from_json_file("add_item.json")
except:
    f = []
for i in sys.argv[1:]:
    f.append(i)
save_to_json_file(f, "add_item.json")
