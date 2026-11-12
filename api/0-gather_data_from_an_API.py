#!/usr/bin/python3
"""
Module that uses a REST API for a given employee ID,
returns information about his/her TODO list progress.
"""

import json
import sys
import urllib.request

if __name__ == "__main__":
    if len(sys.argv) > 1:
        emp_id = sys.argv[1]
        base_url = "https://jsonplaceholder.typicode.com"

        user_url = "{}/users/{}".format(base_url, emp_id)
        with urllib.request.urlopen(user_url) as response:
            user_data = json.loads(response.read().decode())
            emp_name = user_data.get("name")

        todos_url = "{}/todos?userId={}".format(base_url, emp_id)
        with urllib.request.urlopen(todos_url) as response:
            todos_data = json.loads(response.read().decode())

        total_tasks = len(todos_data)
        done_tasks = [t for t in todos_data if t.get("completed")]
        number_of_done = len(done_tasks)

        print("Employee {} is done with tasks({}/{}):".format(
            emp_name, number_of_done, total_tasks))

        for task in done_tasks:
            print("\t {}".format(task.get("title")))
