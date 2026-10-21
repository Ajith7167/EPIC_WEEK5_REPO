import pytest

from employee import Employee, EmployeeService


@pytest.fixture
def service():
    return EmployeeService()


def test_add_employee(service):
    employee = Employee(101, "Ajith", 30000)
    service.add_employee(employee)

    assert service.get_employee(101) == employee


def test_get_all_employees(service):
    service.add_employee(Employee(101, "Ajith", 30000))
    service.add_employee(Employee(102, "Rahul", 35000))

    assert len(service.get_all_employees()) == 2


def test_duplicate_employee(service):
    service.add_employee(Employee(101, "Ajith", 30000))

    with pytest.raises(ValueError, match="already exists"):
        service.add_employee(Employee(101, "Rahul", 35000))


def test_update_salary(service):
    service.add_employee(Employee(101, "Ajith", 30000))
    service.update_salary(101, 40000)

    assert service.get_employee(101).salary == 40000


def test_delete_employee(service):
    service.add_employee(Employee(101, "Ajith", 30000))
    service.delete_employee(101)

    with pytest.raises(ValueError, match="not found"):
        service.get_employee(101)


@pytest.mark.parametrize(
    "employee_id, name, salary",
    [
        (0, "Ajith", 30000),
        (101, "", 30000),
        (101, "Ajith", 0),
        (101, "Ajith", -1000),
    ],
)
def test_invalid_employee(employee_id, name, salary):
    with pytest.raises(ValueError):
        Employee(employee_id, name, salary)


def test_invalid_updated_salary(service):
    service.add_employee(Employee(101, "Ajith", 30000))

    with pytest.raises(ValueError, match="Salary must be positive"):
        service.update_salary(101, -500)
