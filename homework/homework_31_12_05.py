# Костромин Андрей Львович

import csv
import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

with open('response.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=todos[0].keys(), lineterminator='\r')
    writer.writeheader()
    for row in todos:
        writer.writerow(row)
