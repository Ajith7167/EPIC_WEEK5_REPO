import pytest
from employee_management import Employee


def test_create_employee() -> None:
    employee = Employee("EMP001", "Ajith", 35000.0)

    assert employee.employee_id == "EMP001"
    assert employee.name == "Ajith"
    assert employee.salary == 35000.0


def test_strip_spaces() -> None:
    employee = Employee(" EMP001 ", " Ajith ", 35000.0)

    assert employee.employee_id == "EMP001"
    assert employee.name == "Ajith"


@pytest.mark.parametrize(
    ("employee_id", "name", "salary", "error_message"),
    [
        ("", "Ajith", 35000.0, "Employee ID cannot be empty"),
        ("EMP001", "", 35000.0, "Employee name cannot be empty"),
        ("EMP001", "Ajith", 0.0, "Salary must be greater than zero"),
        ("EMP001", "Ajith", -100.0, "Salary must be greater than zero"),
        ("   ", "Ajith", 35000.0, "Employee ID cannot be empty"),
        ("EMP001", "   ", 35000.0, "Employee name cannot be empty"),
    ],
)
def test_invalid_employee_data(
    employee_id: str,
    name: str,
    salary: float,
    error_message: str,
) -> None:
    with pytest.raises(ValueError, match=error_message):
        Employee(employee_id, name, salary)
