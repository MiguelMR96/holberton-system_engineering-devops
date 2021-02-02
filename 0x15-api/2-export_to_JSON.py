#!/usr/bin/python3
""" Using an example REST API extract some data
for a given employee ID, returns information about
his/her To-Do list progress
"""
import json
from os import sys
import requests


if __name__ == "__main__":
    """
    Gather data from API, request data filtered by id.
    Saves the data in JSON file
    Should give id when program runs ./2-export_to_JSON.py <id>
    """
    new_dic = {}
    # Request information from API, filter by id and extract in json
    user_id = {'id': sys.argv[1]}
    todos_id = {'userId': sys.argv[1]}
    users = requests.get(
        'https://jsonplaceholder.typicode.com/users', params=user_id).json()
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos', params=todos_id).json()

    # Extracting data from json to save it in file
    username = users[0].get('username')
    with open(sys.argv[1] + '.json', 'w') as json_file:
        new_list = []
        # Iterate and add tasks in dictionary format inside a list
        for item in todos:
            new_list.append({'task': item.get('title'),
                             'completed': item.get('completed'),
                             'username': users[0].get('username')})
        # Set dictionary by id to the dictionary list of task
        new_dic[sys.argv[1]] = new_list
        json.dump(new_dic, json_file)
