#!/usr/bin/python3
""" Console Module """
"""
Python script that uses this  rest api for given
employee ID to return info about his/her todo list progress
"""
if __name__ == '__main__':
    import json
    from requests import get
    from sys import argv
    """this module is fucking documented"""

    employee_ID = argv[1]
    all_todos = get(f'https://jsonplaceholder.typicode.com/todos')
    users = get(f'https://jsonplaceholder.typicode.com/users')

    employee_list = json.loads(all_todos.text)
    users = json.loads(users.text)
    for user in users:
        if user.get('id') == int(employee_ID):
            employee_name = user.get('name')

    completed_task = 0
    task_count = 0
    task_list = []
    for employee in employee_list:
        if employee.get('userId') == int(employee_ID):
            task_count += 1
            if employee.get('completed') is True:
                completed_task += 1
                task_list.append(employee['title'])

    firstline = (
        f'Employee {employee_name} is done'
        f' with tasks({completed_task}/{task_count}):'
    )
    print(firstline)

    for task in task_list:
        print(f'\t {task}')
