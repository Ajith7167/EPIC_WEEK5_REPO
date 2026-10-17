# %%
from dataclasses import dataclass
from typing import Protocol


# %%
# 1. Domain model: Employee data and validation
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


# %%
# 2. Protocol: Defines the repository contract
class EmployeeRepository(Protocol):
    def add(self, employee: Employee) -> None: ...

    def get(self, employee_id: str) -> Employee: ...

    def get_all(self) -> list[Employee]: ...


# %%
# 3. Repository: Handles data storage
class InMemoryEmployeeRepository:
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


# %%
# 4. Service: Contains business logic
class EmployeeService:
    def __init__(self, repository: EmployeeRepository) -> None:
        self._repository = repository

    def add_employee(self, employee: Employee) -> None:
        self._repository.add(employee)

    def get_employee(self, employee_id: str) -> Employee:
        return self._repository.get(employee_id)

    def list_employees(self) -> list[Employee]:
        return self._repository.get_all()


# %%
# 5. Presentation layer: Handles output
def display_employees(employees: list[Employee]) -> None:
    if not employees:
        print("No employees found.")
        return

    for employee in employees:
        print(f"ID: {employee.employee_id}")
        print(f"Name: {employee.name}")
        print(f"Salary: Rs. {employee.salary:.2f}")
        print("-" * 30)


# %%
# 6. Main function: Connects all components
def main() -> None:
    repository = InMemoryEmployeeRepository()
    service = EmployeeService(repository)

    try:
        employee1 = Employee("EMP001", "Ajith", 85000.0)
        employee2 = Employee("EMP002", "Varun", 45000.0)

        service.add_employee(employee1)
        service.add_employee(employee2)

        print("Employee Management System")
        print("=" * 30)

        employees = service.list_employees()
        display_employees(employees)

        employee = service.get_employee("EMP001")
        print(f"Found employee: {employee.name}")

    except ValueError as error:
        print(f"Error: {error}")


# %%
if __name__ == "__main__":
    main()
