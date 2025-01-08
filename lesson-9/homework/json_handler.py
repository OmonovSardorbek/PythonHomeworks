import json
import csv

def load_tasks_from_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def save_tasks_to_json(filename, tasks):
    with open(filename, 'w') as f:
        json.dump(tasks, f, indent=4)

def display_tasks(tasks):
    print("Tasks:")
    for task in tasks:
        print(f"ID: {task['id']}, Task Name: {task['task']}, Completed: {task['completed']}, Priority: {task['priority']}")

def calculate_task_stats(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'])
    pending_tasks = total_tasks - completed_tasks
    total_priority = sum(task['priority'] for task in tasks)
    average_priority = total_priority / total_tasks
    return {
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,
        "average_priority": average_priority
    }

def convert_json_to_csv(json_filename, csv_filename):
    tasks = load_tasks_from_json(json_filename)
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['ID', 'Task Name', 'Completed Status', 'Priority']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for task in tasks:
            writer.writerow({
                'ID': task['id'],
                'Task Name': task['task'],
                'Completed Status': task['completed'],
                'Priority': task['priority']
            })

if __name__ == "__main__":
    tasks_filename = 'tasks.json'
    tasks = load_tasks_from_json(tasks_filename)

    display_tasks(tasks)

    stats = calculate_task_stats(tasks)
    print(f"Total Tasks: {stats['total_tasks']}")
    print(f"Completed Tasks: {stats['completed_tasks']}")
    print(f"Pending Tasks: {stats['pending_tasks']}")
    print(f"Average Priority: {stats['average_priority']:.2f}")

    convert_json_to_csv(tasks_filename, 'tasks.csv')