#!/usr/bin/python3
"""this script adds arguments to a python list and serializes to a file"""
import sys
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    ls = sys.argv[1:]
    try:
        item = load("add_item.json")
    except Exception:
        save(ls, "add_item.json")
    else:
        for arg in ls:
            item.append(arg)
        save(item, "add_items.json")
