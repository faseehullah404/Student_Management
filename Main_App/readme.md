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

We configured pytest to run tests in different groups, execute them in order, and support parallel testing.

### 9.1 Test Groups

Tests are divided into four groups:

| Group   | Tests                                     |
| ------- | ----------------------------------------- |
| student | Student model, profile, results and notes |
| teacher | Teacher model, profile, results and notes |
| auth    | Authentication and login                  |
| csvdata | External CSV-based tests                  |

**Configuration Files:**

- `pytest.ini` - Defines the test markers and Django settings.
- `test/conftest.py` - Assigns tests to groups and sets collection order.
- `run_suites.ps1` - Runs the test groups in a fixed sequence.

### 9.2 Test Group Commands

Student tests:

`python -m pytest test/ -m student -v`

Teacher tests:

`python -m pytest test/ -m teacher -v`

Authentication tests:

`python -m pytest test/ -m auth -v`

CSV tests:

`python -m pytest test/ -m csvdata -v`

### 9.3 Execution Order

The test groups run in this order:

1. Student
2. Teacher
3. Authentication
4. CSV

Command:

`powershell -ExecutionPolicy Bypass -File .\run_suites.ps1`

The PowerShell script executes each group sequentially, even if an earlier group has failing tests. The `conftest.py` file also defines a predictable collection order within groups.

### 9.4 Parallel Testing

We used pytest-xdist to execute tests using two workers.

Command:

`python -m pytest test/ -n 2 --dist loadfile -v`

The `-n 2` option uses two workers, and `--dist loadfile` groups tests from the same file onto one worker.

Parallel execution does not guarantee a fixed completion order.

### 9.5 Test Parameterization

We used `@pytest.mark.parametrize` to execute the same test with different input values.

Parameterization was used in Student, Teacher, Authentication and CSV-based tests.

The CSV tests read external test data using Python's `csv.DictReader`.

### 9.6 Execution Results

Test grouping, collection order, sequential execution and parallel execution were tested successfully.

The four previously identified Student BVA failures remain documented and were not modified.

Task 4 configuration and execution verification are complete.

## 10. Submission Notes

The repository should contain source code, tests, configuration, CSV and Excel data, screenshots, the setup video, and the summary report if required by the assignment.

The assignment PDF lists 21 October 2026 as the due date and prohibits repository updates after the deadline. Check instructor permission before any later push.
