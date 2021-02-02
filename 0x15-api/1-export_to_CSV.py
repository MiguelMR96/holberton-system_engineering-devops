#!/usr/bin/python3
""" Using an example REST API extract some data
for a given employee ID, returns information about
his/her To-Do list progress
"""
import csv
from os import sys
import requests


if __name__ == "__main__":
    """
    Gather data from API, request data filtered by id.
    id given when program run ./1-exporpy <id>
    """
    # Request information from API, filter by id and extract in json
    user_id = {'id': sys.argv[1]}
    todos_id = {'userId': sys.argv[1]}
    users = requests.get(
        'https://jsonplaceholder.typicode.com/users', params=user_id).json()
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos', params=todos_id).json()

    # Extracting data from json to print
    username = users[0].get('username')
    with open(sys.argv[1] + '.csv', 'w') as fd:

        for item in todos:
            employee_writer = csv.writer(fd, delimiter=',',
                                         quotechar='"', quoting=csv.QUOTE_ALL)
            status = item.get('completed')
            title = item.get('title')
            employee_writer.writerow([sys.argv[1], username, status, title])
