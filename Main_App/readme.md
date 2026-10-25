# Student Management System - Automated Testing

## 1. Project Overview

This project is a Python Django-based Student Management System. It manages students, teachers, administrators, and academic information.

## 2. Assignment Objective

Build an automated testing solution for three application areas:

1. Student module - Faseeh
2. Teacher module - Zohaib
3. Authentication/Login module - Faseeh and Zohaib

The testing work includes ECP, BVA, automated tests, an Excel test-case sheet, external CSV test data, and test execution configuration.

## 3. Testing Tools

- Python and Django
- pytest and pytest-django
- unittest.mock for isolated unit tests
- pytest-xdist for parallel testing
- Python csv module for external test data
- Microsoft Excel for test-case documentation
- Git and GitHub for individual contributions

Selenium is not used.

## 4. Testing Approach

- ECP and BVA to design input cases
- Positive and negative tests
- Parameterized tests using pytest
- Django model validation
- Django test-client tests for views
- Mock-based unit tests for email authentication
- Data-driven tests using external CSV files

Not all test-client tests are isolated unit tests. They also check Django view and database integration.

## 5. Team Contributions

| Member | Work                                                                             |
| ------ | -------------------------------------------------------------------------------- |
| Faseeh | Student model, student views, EmailAuth.authenticate(), Student medium CSV tests |
| Zohaib | Teacher model, teacher views, loginuser(), Teacher gender CSV tests              |
| Both   | Test case Excel sheet, test suite configuration, screenshots, documentation      |

Individual notes:

- `Main_App/readme_faseeh.md`
- `Main_App/readme_zohaib.md`

## 6. Test Files and Commands

Run Student tests:

```powershell
python -m pytest test/test_student_model.py test/test_student_profile.py test/test_student_content.py -v
```

Run Teacher tests:

```powershell
python -m pytest test/test_teacher_model.py test/test_teacher_profile.py test/test_teacher_content.py -v
```

Run Email Authentication tests:

```powershell
python -m pytest test/test_email_auth.py -v
```

Run Task 3 CSV tests:

```powershell
python -m pytest test/test_task3_faseeh_csv.py test/test_task3_zohaib_csv.py -v
```

Run all tests:

```powershell
python -m pytest test/ -v
```

## 7. Recorded Results and Known Issue

| Module               | Recorded results                                    |
| -------------------- | --------------------------------------------------- |
| Student              | 28 passed, 4 failed, out of 32 executions           |
| Teacher              | 28 passed, before new Login/CSV work                |
| Email Authentication | 10 test cases written; see latest execution         |
| Login                | Zohaib's added tests; see latest execution          |
| CSV tests            | 4 cases per member; see Excel for execution results |

The four Student failures come from testing `Student.std`: the CharField has integer-valued choices. The issue was documented and not fixed.

Do not treat the known failures as passed tests.

## 8. Task 3 - Excel and External CSV Data

**Excel:** `Task3_Test_Cases_Simple.xlsx`

**External data:**

- `test_data/faseeh_student_medium.csv` (4 cases)
- `test_data/zohaib_teacher_gender.csv` (4 cases)

**Python tests:**

- `test/test_task3_faseeh_csv.py`
- `test/test_task3_zohaib_csv.py`

The tests read the CSV files using `csv.DictReader` and use pytest parameterization. Enter actual results and Pass/Fail in the Excel sheet after running the tests.

## 9. Task 4 - Test Configuration

Task 4 requires suites/groups, parameterization, parallel execution, and execution order. The following files are prepared separately and should be tested before marking the task complete:

- `pytest.ini` - pytest configuration and suite markers
- `test/conftest.py` - groups tests by module and orders collection
- `run_suites.ps1` - runs each test group in a fixed order

Sequential runs provide a predictable order. Parallel execution using `pytest-xdist` does not guarantee the exact completion order of individual test cases.

## 10. Submission Notes

The repository should contain source code, tests, configuration, CSV and Excel data, screenshots, the setup video, and the summary report if required by the assignment.

The assignment PDF lists 21 October 2026 as the due date and prohibits repository updates after the deadline. Check instructor permission before any later push.
