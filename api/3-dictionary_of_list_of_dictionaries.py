#!/usr/bin/python3
"""
Python script to export TODO data of all employees in JSON format.
"""

import json
import urllib.request

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    users_url = "{}/users".format(base_url)
    with urllib.request.urlopen(users_url) as response:
        users_data = json.loads(response.read().decode())

    todos_url = "{}/todos".format(base_url)
    with urllib.request.urlopen(todos_url) as response:
        todos_data = json.loads(response.read().decode())

    users_dict = {user["id"]: user["username"] for user in users_data}
    out_data = {}

    for user in users_data:
        user_id = str(user["id"])
        username = user["username"]
        out_data[user_id] = []

    for task in todos_data:
        user_id = str(task["userId"])
        username = users_dict.get(task["userId"])
        out_data[user_id].append({
            "username": username,
            "task": task["title"],
            "completed": task["completed"]
        })

    with open("todo_all_employees.json", "w", encoding="utf-8") as f:
        json.dump(out_data, f)
