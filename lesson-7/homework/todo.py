import json
import csv
from abc import ABC, abstractmethod

class Task:
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return {
            "Task ID": self.task_id,
            "Title": self.title,
            "Description": self.description,
            "Due Date": self.due_date,
            "Status": self.status
        }

    @classmethod
    def from_dict(cls, task_dict):
        return cls(
            task_dict["Task ID"],
            task_dict["Title"],
            task_dict["Description"],
            task_dict.get("Due Date"),
            task_dict["Status"]
        )

class StorageStrategy(ABC):
    @abstractmethod
    def save(self, tasks, file_path):
        pass

    @abstractmethod
    def load(self, file_path):
        pass

class JSONStorageStrategy(StorageStrategy):
    def save(self, tasks, file_path):
        with open(file_path, "w") as file:
            json.dump([task.to_dict() for task in tasks], file, indent=4)

    def load(self, file_path):
        try:
            with open(file_path, "r") as file:
                return [Task.from_dict(task) for task in json.load(file)]
        except FileNotFoundError:
            return []

class CSVStorageStrategy(StorageStrategy):
    def save(self, tasks, file_path):
        with open(file_path, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Task ID", "Title", "Description", "Due Date", "Status"])
            writer.writeheader()
            for task in tasks:
                writer.writerow(task.to_dict())

    def load(self, file_path):
        try:
            with open(file_path, "r") as file:
                reader = csv.DictReader(file)
                return [Task.from_dict(row) for row in reader]
        except FileNotFoundError:
            return []

class ToDoApp:
    def __init__(self, storage_strategy):
        self.tasks = []
        self.storage_strategy = storage_strategy

    def add_task(self, task_id, title, description, due_date=None, status="Pending"):
        task = Task(task_id, title, description, due_date, status)
        self.tasks.append(task)

    def view_tasks(self):
        for task in self.tasks:
            print(task.to_dict())

    def update_task(self, task_id, **updates):
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = updates.get("title", task.title)
                task.description = updates.get("description", task.description)
                task.due_date = updates.get("due_date", task.due_date)
                task.status = updates.get("status", task.status)
                return True
        return False

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]

    def filter_tasks(self, status):
        return [task for task in self.tasks if task.status == status]

    def save_tasks(self, file_path):
        self.storage_strategy.save(self.tasks, file_path)

    def load_tasks(self, file_path):
        self.tasks = self.storage_strategy.load(file_path)

print("Choose storage format: 1. JSON, 2. CSV")
choice = input("Enter choice: ")

if choice == "1":
    storage = JSONStorageStrategy()
    file_path = "tasks.json"
elif choice == "2":
    storage = CSVStorageStrategy()
    file_path = "tasks.csv"
else:
    print("Invalid choice!")
    exit()

app = ToDoApp(storage)
app.load_tasks(file_path)

while True:
    print("\nWelcome to the To-Do Application!\n1. Add a new task\n2. View all tasks\n3. Update a task\n4. Delete a task\n5. Filter tasks by status\n6. Save tasks\n7. Load tasks\n8. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        task_id = input("Enter Task ID: ")
        title = input("Enter Title: ")
        description = input("Enter Description: ")
        due_date = input("Enter Due Date (YYYY-MM-DD) (optional): ") or None
        status = input("Enter Status (Pending/In Progress/Completed): ")
        app.add_task(task_id, title, description, due_date, status)
    elif choice == "2":
        app.view_tasks()
    elif choice == "3":
        task_id = input("Enter Task ID to update: ")
        updates = {
            "title": input("Enter new Title (or leave blank): ") or None,
            "description": input("Enter new Description (or leave blank): ") or None,
            "due_date": input("Enter new Due Date (YYYY-MM-DD) (or leave blank): ") or None,
            "status": input("Enter new Status (Pending/In Progress/Completed) (or leave blank): ") or None,
        }
        updates = {k: v for k, v in updates.items() if v is not None}
        if app.update_task(task_id, **updates):
            print("Task updated successfully.")
        else:
            print("Task not found.")
    elif choice == "4":
        task_id = input("Enter Task ID to delete: ")
        app.delete_task(task_id)
    elif choice == "5":
        status = input("Enter status to filter by (Pending/In Progress/Completed): ")
        filtered_tasks = app.filter_tasks(status)
        for task in filtered_tasks:
            print(task.to_dict())
    elif choice == "6":
        app.save_tasks(file_path)
        print("Tasks saved successfully.")
    elif choice == "7":
        app.load_tasks(file_path)
        print("Tasks loaded successfully.")
    elif choice == "8":
        break
    else:
        print("Invalid choice!")