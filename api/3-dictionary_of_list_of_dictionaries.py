#!/usr/bin/python3
""" Console Module """
"""
Python script that uses this  rest api for given
employee ID to return info about his/her todo list progress
"""
if __name__ == '__main__':
    import json
    from requests import get
    """this module is fucking documented"""

    all_todos = get(f'https://jsonplaceholder.typicode.com/todos')
    users = get(f'https://jsonplaceholder.typicode.com/users')

    todo_list = json.loads(all_todos.text)
    users = json.loads(users.text)

    task_count = 0
    task_list = []
    task_success = []
    json_list = []
    THE_dict = {}
    user_count = 0
    for user in users:
        user_count += 1
        employee_name = user.get('username')
        for employee in todo_list:
            if employee.get('userId') == user.get('id'):
                task_list.append(employee['title'])
                task_success.append(employee['completed'])
        for i in range(len(task_list)):
            true_or_false = bool(task_success[i])
            task = f'{task_list[i]}'
            name = employee_name
            every_dict = ({'username': name,
                           'task': task,
                           'completed': true_or_false})
            json_list.append(every_dict)

        THE_dict[str(user_count)] = json_list
        json_list = []
        task_list = []
        task_success = []
    with open('todo_all_employees.json', 'w') as f:
        json.dump(THE_dict, f)
