
# Day 5 Capstone: Employee Application

## Objective
Build a small Python employee management application
with validation and automated testing.

## Design Decisions
1. Employee uses a dataclass to store employee details.
2. EmployeeService handles employee operations.
3. A dictionary stores employees using employee ID as the key.
4. ValueError handles invalid employee data and operations.
5. Type hints improve readability and support code maintenance.

## Testing
The pytest suite checks:
- Adding and retrieving employees
- Listing employee records
- Duplicate employee IDs
- Updating salary
- Deleting employees
- Invalid employee details
- Invalid salary updates

## Test Results
Run `python -m pytest -v` and record the actual
number of passed and failed tests here.

## Limitations
Data is stored in memory and is lost when the program ends.
The application does not use a database or web API.

## Conclusion
The capstone demonstrates basic application design,
validation, automated testing, and documentation.
