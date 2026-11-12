#!/usr/bin/python3
"""
Python script to export employee TODO data in CSV format.
"""

import csv
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

        filename = "{}.csv".format(emp_id)
        with open(filename, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            for task in todos_data:
                writer.writerow([
                    emp_id,
                    username,
                    str(task.get("completed")),
                    task.get("title")
                ])
