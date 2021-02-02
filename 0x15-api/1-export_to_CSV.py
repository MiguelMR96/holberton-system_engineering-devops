#!/usr/bin/python3
""" Using an example REST API extract some data
for a given employee ID, then write it in a CSV file
"""
import csv
from os import sys
import requests


if __name__ == "__main__":
    """
    Gather data from API, request data filtered by id.
    Write the data in CSV format.
    Should give id when program runs ./1-export_to_CSV.py <id>
    """
    # Request information from API, filter by id and extract in json format
    user_id = {'id': sys.argv[1]}
    todos_id = {'userId': sys.argv[1]}
    users = requests.get(
        'https://jsonplaceholder.typicode.com/users', params=user_id).json()
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos', params=todos_id).json()

    # Extracting data from json to save it in file
    username = users[0].get('username')
    with open(sys.argv[1] + '.csv', 'w') as fd:
        # Iterate to write every row with the title and the task
        # owned by the user
        for item in todos:
            # Formatting CSV file output // See documentation
            employee_writer = csv.writer(fd, delimiter=',',
                                         quotechar='"', quoting=csv.QUOTE_ALL)
            status = item.get('completed')
            title = item.get('title')
            employee_writer.writerow([sys.argv[1], username, status, title])
