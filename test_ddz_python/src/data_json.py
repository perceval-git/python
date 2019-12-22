"""Module provides wrapper class for JSON-object to receive from file"""
import json


def load_data(json_file) -> dict:
    """Function loads data from file to Json-object"""

    if json_file is not None:
        with open(json_file, 'r') as file:
            return json.load(file)
