#!/usr/bin/python3
"""
Python script to export employee TODO data in JSON format.
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
            username = user_data.get("username")

        todos_url = "{}/todos?userId={}".format(base_url, emp_id)
        with urllib.request.urlopen(todos_url) as response:
            todos_data = json.loads(response.read().decode())

        tasks_list = []
        for task in todos_data:
            tasks_list.append({
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            })

        out_data = {emp_id: tasks_list}
        filename = "{}.json".format(emp_id)
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(out_data, f)
