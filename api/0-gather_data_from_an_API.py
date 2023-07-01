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

    emp_name = emp_info.get("name")
    comp_tasks = [task["title"] for task in emp_tasks if task["completed"]]
    num_tasks = len(comp_tasks)
    total_tasks = len(emp_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        emp_name, num_tasks, total_tasks))

    for task in comp_tasks:
        print(f"\t {task}")
