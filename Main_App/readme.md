# Student Management System — Automated Testing

## 1. Project Overview

This project is a Python Django-based Student Management System.
It provides functionality for managing students, teachers, administrators,
and academic information.

## 2. Assignment Objective

The objective is to build an automated testing solution for the Django Student Management System using pytest and pytest-django.

Three application areas were selected for testing:

1. Student Module — Faseeh
2. Teacher Module — Zohaib
3. Authentication/Login Module — Faseeh and Zohaib

## 3. Testing Tools

- Python
- Django
- pytest
- pytest-django
- pytest-xdist for parallel execution
- unittest.mock for isolated unit tests
- CSV for external test data
- Microsoft Excel for test case documentation
- Git and GitHub for version control

Selenium is not used in this assignment.

## 4. Testing Approach

The testing approach includes:

- Equivalence Class Partitioning (ECP)
- Boundary Value Analysis (BVA)
- Positive and negative testing
- Parameterized automated tests
- Django model validation tests
- Django test-client tests
- Mock-based isolated unit tests
- Data-driven testing with external CSV files

## 5. Team Contributions

| Member | Assigned Work                                                    |
| ------ | ---------------------------------------------------------------- |
| Faseeh | Student Module and EmailAuth.authenticate()                      |
| Zohaib | Teacher Module and loginuser()                                   |
| Both   | CSV/Excel documentation, test suites and execution configuration |

Individual testing documentation is stored in:

- `Main_App/readme_faseeh.md`
- `Main_App/readme_zohaib.md`

## 6. Test Execution

Run Student tests:

`python -m pytest test/test_student_model.py test/test_student_profile.py test/test_student_content.py -v`

Run Teacher tests:

`python -m pytest test/test_teacher_model.py test/test_teacher_profile.py test/test_teacher_content.py -v`

Run Email Authentication tests:

`python -m pytest test/test_email_auth.py -v`

Run all automated tests:

`python -m pytest test/ -v`

## 7. Current Test Results

The Student Module has 32 recorded test executions: 28 passed and 4 failed due to a documented standard validation issue.

The Teacher Module has 28 recorded passing test executions.

Authentication/Login test results must be updated using the latest combined test run.

## 8. Task 3 — External Test Data

Test cases are documented in an Excel workbook, and selected automated tests consume their input data from external CSV files.

Test cases are divided between Faseeh and Zohaib to demonstrate individual contributions.

## 9. Task 4 — Test Configuration

Test suites, execution order, parallel execution and data-driven parameterization will be configured and documented separately.
