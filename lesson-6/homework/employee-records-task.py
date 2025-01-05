import os

file_name = "employees.txt"


if not os.path.exists(file_name):
    with open(file_name, 'w') as file:
        pass  

def add_employee():
    employee_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    position = input("Enter Position: ")
    salary = input("Enter Salary: ")

    
    with open(file_name, 'a') as file:
        file.write(f"{employee_id}, {name}, {position}, {salary}\n")
    print("Employee record added successfully!")


def view_all_employees():
    with open(file_name, 'r') as file:
        employees = file.readlines()

    if employees:
        print("\nEmployee Records:")
        for record in employees:
            print(record.strip())
    else:
        print("No employee records found.")


def search_employee():
    search_id = input("Enter Employee ID to search: ")
    with open(file_name, 'r') as file:
        employees = file.readlines()

    found = False
    for record in employees:
        if record.startswith(search_id):
            print("\nEmployee Found:")
            print(record.strip())
            found = True
            break

    if not found:
        print(f"No employee found with ID {search_id}.")


def update_employee():
    search_id = input("Enter Employee ID to update: ")
    with open(file_name, 'r') as file:
        employees = file.readlines()

    found = False
    with open(file_name, 'w') as file:
        for record in employees:
            if record.startswith(search_id):
                found = True
                print("Employee found. What would you like to update?")
                print("1. Name")
                print("2. Position")
                print("3. Salary")
                choice = input("Enter your choice (1/2/3): ")

                if choice == '1':
                    new_name = input("Enter new Name: ")
                    record = f"{search_id}, {new_name}, {record.split(', ')[2]}, {record.split(', ')[3]}"
                elif choice == '2':
                    new_position = input("Enter new Position: ")
                    record = f"{search_id}, {record.split(', ')[1]}, {new_position}, {record.split(', ')[3]}"
                elif choice == '3':
                    new_salary = input("Enter new Salary: ")
                    record = f"{search_id}, {record.split(', ')[1]}, {record.split(', ')[2]}, {new_salary}"
                else:
                    print("Invalid choice.")
                    file.write(record)
                    continue
                print("Employee record updated successfully!")
            file.write(record)

    if not found:
        print(f"No employee found with ID {search_id}.")

def delete_employee():
    delete_id = input("Enter Employee ID to delete: ")
    with open(file_name, 'r') as file:
        employees = file.readlines()

    found = False
    with open(file_name, 'w') as file:
        for record in employees:
            if not record.startswith(delete_id):
                file.write(record)
            else:
                found = True

    if found:
        print(f"Employee with ID {delete_id} has been deleted.")
    else:
        print(f"No employee found with ID {delete_id}.")


while True:
    print("\n--- Employee Records Manager ---")
    print("1. Add new employee record")
    print("2. View all employee records")
    print("3. Search for an employee by Employee ID")
    print("4. Update an employee's information")
    print("5. Delete an employee record")
    print("6. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == '1':
        add_employee()
    elif choice == '2':
        view_all_employees()
    elif choice == '3':
        search_employee()
    elif choice == '4':
        update_employee()
    elif choice == '5':
        delete_employee()
    elif choice == '6':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select again.")


