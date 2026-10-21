from dataclasses import dataclass


@dataclass
class Employee:
    employee_id: str
    name: str
    salary: float

    def __post_init__(self) -> None:
        self.employee_id = self.employee_id.strip()
        self.name = self.name.strip()

        if not self.employee_id:
            raise ValueError("Employee ID cannot be empty")

        if not self.name:
            raise ValueError("Employee name cannot be empty")

        if self.salary <= 0:
            raise ValueError("Salary must be greater than zero")


class EmployeeRepository:
    def __init__(self) -> None:
        self._employees: dict[str, Employee] = {}

    def add(self, employee: Employee) -> None:
        if employee.employee_id in self._employees:
            raise ValueError("Employee ID already exists")

        self._employees[employee.employee_id] = employee

    def get(self, employee_id: str) -> Employee:
        employee = self._employees.get(employee_id)

        if employee is None:
            raise ValueError("Employee not found")

        return employee

    def get_all(self) -> list[Employee]:
        return list(self._employees.values())


class EmployeeService:
    def __init__(self, repository: EmployeeRepository) -> None:
        self._repository = repository

    def add_employee(self, employee: Employee) -> None:
        self._repository.add(employee)

    def get_employee(self, employee_id: str) -> Employee:
        return self._repository.get(employee_id)

    def list_employees(self) -> list[Employee]:
        return self._repository.get_all()
