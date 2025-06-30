import csv

task_list = [
    {"id": 1, "task": "eat"},
    {"id": 2, "task": "sleep"},
    {"id": 3, "task": "work"},
    {"id": 14, "task": "exercise"},
    {"id": 5, "task": "play"},
]

with open('tasks.csv', 'w', newline='') as file:
    fieldnames = ['id', 'task']
    writer = csv.DictWriter(file, fieldnames = fieldnames)
    writer.writeheader()
    writer.writerows(task_list)

try:
    with open('taks.csv', 'r') as file:
        reader = csv.DictReader(file)
        if not {'id', 'task'}.issubset(reader.fieldnames):
            raise ValueError("CSV file missing required columns")
        for row in reader:
            try:
                if int(row['id']) > 4:
                    print(row['id'], row['task'])
            except ValueError as e:
                print(e)
except FileNotFoundError:
    print("Error: File not found")
except Exception as e:
    print(e)

with open('tasks.csv', 'a', newline='') as file:
    fieldnames = ['id', 'task']
    writer = csv.DictWriter(file, fieldnames = fieldnames)
    writer.writerow({"id": 10, "task": "cook"})