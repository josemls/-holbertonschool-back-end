#!/usr/bin/python3
"""Gather data from an API."""


import requests
import sys
import json

if __name__ == '__main__':

    emp_id = sys.argv[1]

    api_url = "https://jsonplaceholder.typicode.com"

    url = f"{api_url}/users/{emp_id}/todos"
    resp = requests.get(url)
    emp_tasks = resp.json()

    url = f"{api_url}/users/{emp_id}"
    resp = requests.get(url)
    emp_info = resp.json()

    emp_todos = [
        {
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': emp_info.get('username'),
        }
        for task in emp_tasks
    ]
    output_json = {emp_id: emp_todos}

    with open(f"{emp_id}.json", mode="w") as f:
        json.dump(output_json, f)
