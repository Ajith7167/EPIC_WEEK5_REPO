

from abc import ABC, abstractmethod


# Base class: Inheritance
class Employee(ABC):
    def __init__(
        self,
        employee_id: str,
        name: str,
        salary: float
    ) -> None:
        self._employee_id = employee_id
        self.name = name
        self.salary = salary

    @property
    def employee_id(self) -> str:
        return self._employee_id

    @property
    def salary(self) -> float:
        return self._salary

    @salary.setter
    def salary(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Salary must be greater than zero")
        self._salary = value

    @abstractmethod
    def calculate_bonus(self) -> float:
        pass

# %%
# Inheritance: Developer is an Employee
class Developer(Employee):
    def __init__(
        self,
        employee_id: str,
        name: str,
        salary: float,
        programming_language: str
    ) -> None:
        super().__init__(employee_id, name, salary)
        self.programming_language = programming_language

    def calculate_bonus(self) -> float:
        return self.salary * 0.10


# Inheritance: Manager is an Employee
class Manager(Employee):
    def __init__(
        self,
        employee_id: str,
        name: str,
        salary: float,
        team_size: int
    ) -> None:
        super().__init__(employee_id, name, salary)

        if team_size < 0:
            raise ValueError("Team size cannot be negative")

        self.team_size = team_size

    def calculate_bonus(self) -> float:
        return self.salary * 0.15


# Separate responsibility: Employee storage
class EmployeeRepository:
    def __init__(self) -> None:
        self._employees: dict[str, Employee] = {}

    def add(self, employee: Employee) -> None:
        if employee.employee_id in self._employees:
            raise ValueError("Employee ID already exists")

        self._employees[employee.employee_id] = employee

    def get(self, employee_id: str) -> Employee:
        if employee_id not in self._employees:
            raise ValueError("Employee not found")

        return self._employees[employee_id]

    def get_all(self) -> list[Employee]:
        return list(self._employees.values())


# Composition: Service uses a repository
class EmployeeService:
    def __init__(self, repository: EmployeeRepository) -> None:
        self._repository = repository

    def register_employee(self, employee: Employee) -> None:
        self._repository.add(employee)

    def display_employees(self) -> None:
        for employee in self._repository.get_all():
            print(f"ID: {employee.employee_id}")
            print(f"Name: {employee.name}")
            print(f"Salary: {employee.salary:.2f}")
            print(f"Bonus: {employee.calculate_bonus():.2f}")
            print("-" * 30)


# Application entry point
def main() -> None:
    repository = EmployeeRepository()
    service = EmployeeService(repository)

    developer = Developer(
        "EMP001", "Ajay", 40000, "Python"
    )

    manager = Manager(
        "EMP002", "Ravi", 60000, 5
    )

    service.register_employee(developer)
    service.register_employee(manager)

    service.display_employees()


if __name__ == "__main__":
    main()
