#!/usr/bin/python3
"""Gather data from an API."""


import requests
import sys

if __name__ == '__main__':

    emp_id = sys.argv[1]

    api_url = "https://jsonplaceholder.typicode.com"

    url = f"{api_url}/users/{emp_id}/todos"
    resp = requests.get(url)
    emp_tasks = resp.json()

    url = f"{api_url}/users/{emp_id}"
    resp = requests.get(url)
    emp_info = resp.json()

    for task in emp_tasks:

        output = f'\"{emp_info.get("id")}\",\"{emp_info.get("username")}\",\"\
            {task.get("completed")}\",\"{task.get("title")}\"\n'

        with open(f"{emp_id}.csv", mode="a", newline="") as f:
            f.write(output)
