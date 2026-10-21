from dataclasses import dataclass


@dataclass
class Employee:
    employee_id: int
    name: str
    salary: float

    def __post_init__(self) -> None:
        if self.employee_id <= 0:
            raise ValueError("Employee ID must be positive")

        if not self.name.strip():
            raise ValueError("Employee name cannot be empty")

        if self.salary <= 0:
            raise ValueError("Salary must be positive")


class EmployeeService:
    def __init__(self) -> None:
        self.employees: dict[int, Employee] = {}

    def add_employee(self, employee: Employee) -> None:
        if employee.employee_id in self.employees:
            raise ValueError("Employee already exists")

        self.employees[employee.employee_id] = employee

    def get_employee(self, employee_id: int) -> Employee:
        if employee_id not in self.employees:
            raise ValueError("Employee not found")

        return self.employees[employee_id]

    def get_all_employees(self) -> list[Employee]:
        return list(self.employees.values())

    def update_salary(self, employee_id: int, salary: float) -> None:
        employee = self.get_employee(employee_id)

        if salary <= 0:
            raise ValueError("Salary must be positive")

        employee.salary = salary

    def delete_employee(self, employee_id: int) -> None:
        if employee_id not in self.employees:
            raise ValueError("Employee not found")

        del self.employees[employee_id]


if __name__ == "__main__":
    service = EmployeeService()

    service.add_employee(Employee(101, "Ajith", 30000))
    service.add_employee(Employee(102, "Rahul", 35000))

    for employee in service.get_all_employees():
        print(employee)
