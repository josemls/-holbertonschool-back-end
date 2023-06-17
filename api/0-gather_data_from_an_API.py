#!/usr/bin/python3
"""api"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        id = int(sys.argv[1])

    url = "https://jsonplaceholder.typicode.com/"
    employee_name = ""
    try:
        response_users = requests.request("GET", "{}users/{}".format(url, id))
        response_tasks = requests.request("GET", "{}todos/".format(url))
        employee_name = response_users.json()["name"]

    except KeyError:
        pass

    total_number_of_tasks = len(response_tasks.json())
    total_number_of_undone_tasks = 0
    total_number_of_done_task = 0

    for i in range(total_number_of_tasks):
        if response_tasks.json()[i]['userId'] == id:
            if response_tasks.json()[i]['completed']:
                total_number_of_done_task += 1
            elif response_tasks.json()[i]['completed'] is False:
                total_number_of_undone_tasks += 1

    total_number_of_done_or_undone_tasks = total_number_of_undone_tasks + \
        total_number_of_done_task
    print("Employee {} is done with tasks({}/{}):".format(employee_name,
          total_number_of_done_task, total_number_of_done_or_undone_tasks))
    for i in range(total_number_of_tasks):
        if response_tasks.json()[i]['userId'] == id:
            if response_tasks.json()[i]['completed']:

                print("\t" + " " + response_tasks.json()[i]['title'])
