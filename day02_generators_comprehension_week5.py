
from functools import wraps
from contextlib import contextmanager
from typing import Iterator


# Sample employee records
employees = [
    {"id": 101, "name": "Ajith", "department": "IT", "salary": 30000},
    {"id": 102, "name": "Rahul", "department": "HR", "salary": 25000},
    {"id": 103, "name": "Priya", "department": "IT", "salary": 40000},
    {"id": 104, "name": "Kiran", "department": "Finance", "salary": 35000},
]


# 1. ITERATOR
def employee_iterator(records):
    iterator = iter(records)

    while True:
        try:
            employee = next(iterator)
            yield employee
        except StopIteration:
            break


# 2. GENERATOR
def high_salary_employees(records, minimum_salary: int) -> Iterator[dict]:
    for employee in records:
        if employee["salary"] >= minimum_salary:
            yield employee


# 3. DECORATOR
def log_operation(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"Starting: {function.__name__}")
        result = function(*args, **kwargs)
        print(f"Completed: {function.__name__}")
        return result

    return wrapper


@log_operation
def display_employees(records):
    for employee in records:
        print(employee)


# 4. CONTEXT MANAGER
@contextmanager
def employee_file(filename):
    file = open(filename, "w", encoding="utf-8")
    try:
        yield file
    finally:
        file.close()


def save_employees(records, filename):
    with employee_file(filename) as file:
        for employee in records:
            file.write(
                f'{employee["id"]},'
                f'{employee["name"]},'
                f'{employee["department"]},'
                f'{employee["salary"]}\n'
            )


# 5. LIST COMPREHENSION
def get_it_employees(records):
    return [
        employee for employee in records
        if employee["department"] == "IT"
    ]


# 6. DICTIONARY COMPREHENSION
def employee_salary_mapping(records):
    return {
        employee["name"]: employee["salary"]
        for employee in records
    }


# MAIN PROGRAM
if __name__ == "__main__":
    print("\n--- Iterator ---")
    for employee in employee_iterator(employees):
        print(employee["name"])

    print("\n--- Generator: Salary >= 30000 ---")
    for employee in high_salary_employees(employees, 30000):
        print(employee["name"], employee["salary"])

    print("\n--- Decorator ---")
    display_employees(employees)

    print("\n--- Context Manager ---")
    save_employees(employees, "employees_output.txt")
    print("Employee records saved successfully.")

    print("\n--- List Comprehension: IT Employees ---")
    print(get_it_employees(employees))

    print("\n--- Dictionary Comprehension ---")
    print(employee_salary_mapping(employees))
