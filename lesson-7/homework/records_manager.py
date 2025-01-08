import os
class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id},{self.name},{self.position},{self.salary}"


class EmployeeManager:
    FILE_NAME = os.path.join(os.path.dirname(__file__), "employees.txt")

    def add_employee(self, employee):
        if self._is_employee_id_unique(employee.employee_id):
            with open(self.FILE_NAME, "a") as file:
                file.write(str(employee) + "\n")
            print("Employee added successfully!")
        else:
            print("Error: Employee ID must be unique.")

    def view_all_employees(self, sort_by=None):
        employees = self._read_all_employees()
        if sort_by == "name":
            employees.sort(key=lambda emp: emp.name)
        elif sort_by == "position":
            employees.sort(key=lambda emp: emp.position)
        elif sort_by == "salary":
            employees.sort(key=lambda emp: emp.salary)

        if employees:
            print("Employee Records:")
            for emp in employees:
                print(emp)
        else:
            print("No records found.")

    def search_employee(self, employee_id):
        employees = self._read_all_employees()
        for emp in employees:
            if emp.employee_id == employee_id:
                print("Employee Found:")
                print(emp)
                return
        print("Error: Employee not found.")

    def update_employee(self, employee_id):
        employees = self._read_all_employees()
        for emp in employees:
            if emp.employee_id == employee_id:
                print("Enter new details (leave blank to keep current value):")
                name = input(f"Name ({emp.name}): ") or emp.name
                position = input(f"Position ({emp.position}): ") or emp.position
                try:
                    salary = input(f"Salary ({emp.salary}): ")
                    salary = float(salary) if salary else emp.salary
                except ValueError:
                    print("Invalid salary. Update canceled.")
                    return
                emp.name, emp.position, emp.salary = name, position, salary
                self._write_all_employees(employees)
                print("Employee updated successfully!")
                return
        print("Error: Employee not found.")

    def delete_employee(self, employee_id):
        employees = self._read_all_employees()
        for emp in employees:
            if emp.employee_id == employee_id:
                employees.remove(emp)
                self._write_all_employees(employees)
                print("Employee deleted successfully!")
                return
        print("Error: Employee not found.")

    def _is_employee_id_unique(self, employee_id):
        employees = self._read_all_employees()
        return all(emp.employee_id != employee_id for emp in employees)

    def _read_all_employees(self):
        employees = []
        try:
            with open(self.FILE_NAME, "r") as file:
                for line in file:
                    employee_id, name, position, salary = line.strip().split(",")
                    employees.append(Employee(employee_id, name, position, float(salary)))
        except FileNotFoundError:
            open(self.FILE_NAME, "w").close()  
        return employees

    def _write_all_employees(self, employees):
        with open(self.FILE_NAME, "w") as file:
            for emp in employees:
                file.write(str(emp) + "\n")

    def menu(self):
        while True:
            print("\nWelcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")

            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 6.")
                continue

            if choice == 1:
                try:
                    employee_id = input("Enter Employee ID: ")
                    name = input("Enter Name: ")
                    position = input("Enter Position: ")
                    salary = float(input("Enter Salary: "))
                    new_employee = Employee(employee_id, name, position, salary)
                    self.add_employee(new_employee)
                except ValueError:
                    print("Invalid input! Salary must be a number.")

            elif choice == 2:
                sort_by = input("Sort by (name/position/salary, or leave blank for none): ").lower()
                self.view_all_employees(sort_by=sort_by if sort_by in ["name", "position", "salary"] else None)

            elif choice == 3:
                employee_id = input("Enter Employee ID to search: ")
                self.search_employee(employee_id)

            elif choice == 4:
                employee_id = input("Enter Employee ID to update: ")
                self.update_employee(employee_id)

            elif choice == 5:
                employee_id = input("Enter Employee ID to delete: ")
                self.delete_employee(employee_id)

            elif choice == 6:
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    manager = EmployeeManager()
    manager.menu()