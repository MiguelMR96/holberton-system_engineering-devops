#!/usr/bin/python3
""" Using an example REST API extract some data
for a given employee ID, returns information about
his/her To-Do list progress
"""
import requests
from os import sys


if __name__ == "__main__":
    """
    Gather data from API, request data filtered by id.
    id given when program run ./0-gather_data_from_an_api.py <id>
    """
    completed_tasks = 0
    total_tasks = 0
    # Request information from API, filter by id and extract in json
    user_id = {'id': sys.argv[1]}
    todos_id = {'userId': sys.argv[1]}
    users = requests.get(
        'https://jsonplaceholder.typicode.com/users', params=user_id).json()
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos', params=todos_id).json()

    # Extracting data from json to print
    name = users[0].get('name')
    for key in todos:
        if key.get('completed'):
            completed_tasks += 1
        total_tasks += 1
    # Print the info about user's to-dos
    print("Employee {} is done with tasks({}/{}):".format(name,
                                                          completed_tasks,
                                                          total_tasks))
    # Print every completed task from user
    for key in todos:
        if key.get('completed'):
            task_title = key.get('title')
            print("\t {}".format(task_title))
