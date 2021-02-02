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
    Saves all employees with their tasks in JSON file
    Should give id when program runs
    ./dictionary_of_list_of_dictionaries.py<id>
    """
    dic_employees = {}
    # Request all information from API and extract in json
    users = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos').json()

    # Extracting data from json
    name = users[0].get('name')
    with open('todo_all_employees.json', 'w') as file_json:
        # Go through all users extracting data
        for iterator in users:
            employee_list = []
            username = iterator.get('username')
            employee_id = iterator.get('id')
            # Go to every employee tasks, asign the values and append it
            # in the list of the employee's tasks (employee_list)
            for inner_iter in todos:
                tasks_dic = {}
                tasks_dic['username'] = username
                tasks_dic['task'] = inner_iter.get('title')
                tasks_dic['completed'] = inner_iter.get('completed')
                employee_list.append(tasks_dic)
            # Finally asign the employee id in the dictionary where
            # all employees are stored (dic_employees) and then
            # the dictionary is stored in JSON format-file.
            dic_employees[employee_id] = employee_list
        json.dump(dic_employees, file_json)
