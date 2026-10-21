from unittest.mock import Mock

import pytest
from employee_management import (
    Employee,
    EmployeeRepository,
    EmployeeService,
)


@pytest.fixture
def repository() -> EmployeeRepository:
    return EmployeeRepository()


@pytest.fixture
def service(
    repository: EmployeeRepository,
) -> EmployeeService:
    return EmployeeService(repository)


def test_add_and_get_employee(service: EmployeeService) -> None:
    employee = Employee("EMP001", "Ajith", 35000.0)

    service.add_employee(employee)

    result = service.get_employee("EMP001")

    assert result == employee


def test_duplicate_employee_id(
    repository: EmployeeRepository,
) -> None:
    employee = Employee("EMP001", "Ajith", 35000.0)

    repository.add(employee)

    with pytest.raises(ValueError, match="already exists"):
        repository.add(employee)


def test_employee_not_found(
    service: EmployeeService,
) -> None:
    with pytest.raises(ValueError, match="Employee not found"):
        service.get_employee("EMP999")


def test_list_employees(service: EmployeeService) -> None:
    employee1 = Employee("EMP001", "Ajith", 35000.0)
    employee2 = Employee("EMP002", "Ravi", 45000.0)

    service.add_employee(employee1)
    service.add_employee(employee2)

    result = service.list_employees()

    assert len(result) == 2
    assert employee1 in result
    assert employee2 in result


def test_service_uses_repository_mock() -> None:
    repository = Mock(spec=EmployeeRepository)
    service = EmployeeService(repository)
    employee = Employee("EMP001", "Ajith", 35000.0)

    service.add_employee(employee)

    repository.add.assert_called_once_with(employee)


def test_service_returns_repository_result() -> None:
    repository = Mock(spec=EmployeeRepository)
    employee = Employee("EMP001", "Ajith", 35000.0)
    repository.get.return_value = employee

    service = EmployeeService(repository)

    result = service.get_employee("EMP001")

    assert result == employee
    repository.get.assert_called_once_with("EMP001")
