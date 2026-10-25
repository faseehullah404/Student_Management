# Faseeh's Testing Notes

## Module

Student module (`Main_App/models.py`, `Main_App/v_student.py`) and Email Authentication (`Main_App/EmailAuthentication.py`).

I tested student data validation, profile updates, passwords, invalid requests, results, notes, and email authentication.

## 1. ECP Student Module

| Test   | Field  | Equivalence Class (Condition)                   | Expected         |
| ------ | ------ | ----------------------------------------------- | ---------------- |
| ECP-01 | std    | 1 <= std <= 10                                  | Valid (intended) |
| ECP-02 | std    | std < 1                                         | Invalid          |
| ECP-03 | std    | std > 10                                        | Invalid          |
| ECP-04 | std    | std is non-numeric                              | Invalid          |
| ECP-05 | medium | medium is Marathi, SemiEng, CBSE, or Foundation | Valid            |
| ECP-06 | medium | medium is not one of the allowed choices        | Invalid          |

`std` uses a CharField with integer choices. Because of this mismatch, some intended valid values are rejected during actual validation.

## 2. BVA Student Module

The intended standard choices are 1 to 10.

| Test   | Field | Input        | Expected |
| ------ | ----- | ------------ | -------- |
| BVA-01 | std   | 0 (min - 1)  | Invalid  |
| BVA-02 | std   | 1 (min)      | Valid    |
| BVA-03 | std   | 2 (min + 1)  | Valid    |
| BVA-04 | std   | 9 (max - 1)  | Valid    |
| BVA-05 | std   | 10 (max)     | Valid    |
| BVA-06 | std   | 11 (max + 1) | Invalid  |

Expected results above describe the intended behavior. Automated tests found four failures.

## 3. Other Test Cases

1. Update a student's first name, last name, email, gender, and address.
2. Keep the old password when the new password is missing or empty.
3. Update the password when a non-empty password is submitted.
4. Reject GET and PUT requests for profile updates.
5. Handle nonexistent, non-numeric, and missing student IDs.
6. Filter results and notes using the student's standard and medium.
7. Return no records when there are no matches, and all records when multiple match.
8. Authenticate a user with an email and password.

## 4. Testing Method

- pytest and pytest-django for automated testing.
- ECP, BVA, positive tests, and negative tests.
- Django test client and a test database for view tests.
- `unittest.mock` for isolated email authentication tests.
- `@pytest.mark.parametrize` for multiple input cases.
- External CSV files for data-driven tests (Task 3).
- pytest-xdist for parallel execution (Task 4 configuration).

## 5. My Work

### 5.1 Student Model Testing

**Application code:** `Student` class in `Main_App/models.py`  
**Test file:** `test/test_student_model.py`

ECP tested four valid and two invalid values of the `medium` field using Django's `field.clean()`.

BVA tested `std` with 0, 1, 2, 9, 10, and 11 using `field.clean()`.

**Results:** Medium ECP: 6 passed. Standard BVA: 2 passed, 4 failed.

**Command:** `python -m pytest test/test_student_model.py -v`

**Evidence:**

- `screenshots/Faseeh/ecp_passedmodule1.png`
- `screenshots/Faseeh/bvafailedmodule1.png`

### 5.2 Student Profile Update Testing

**Application function:** `s_saveprofile()` in `Main_App/v_student.py`  
**Test file:** `test/test_student_profile.py`

Created a student in the test database and sent a POST request using Django test client. Verified updates to first name, last name, email, address, gender, and redirect.

**Result:** 1 passed.

**Command:** `python -m pytest test/test_student_profile.py -v`

**Evidence:** `screenshots/Faseeh/student_profile_update_success.png`

### 5.3 Student Password Testing

**Function:** `s_saveprofile()`  
**Test file:** `test/test_student_profile.py`

| Password input       | Expected behavior             | Result |
| -------------------- | ----------------------------- | ------ |
| None (field omitted) | Old password stays the same   | Pass   |
| Empty string (`""`)  | Old password stays the same   | Pass   |
| Single space (`" "`) | Password changes to one space | Pass   |
| `NewPass456!`        | Password is updated           | Pass   |

Used `check_password()` to verify the stored password. Accepting a space-only password is a possible validation weakness.

**Result:** 4 passed.

**Command:** `python -m pytest test/test_student_profile.py -v`

**Evidence:** `screenshots/Faseeh/student_password_tests.png`

### 5.4 Student Profile Negative Tests

**Function:** `s_saveprofile()`  
**Test file:** `test/test_student_profile.py`

| Test   | Input                  | Expected behavior | Result |
| ------ | ---------------------- | ----------------- | ------ |
| NEG-01 | GET request            | Update rejected   | Pass   |
| NEG-02 | PUT request            | Update rejected   | Pass   |
| NEG-03 | Nonexistent student ID | Error handled     | Pass   |
| NEG-04 | Non-numeric student ID | Error handled     | Pass   |
| NEG-05 | Missing student ID     | Error handled     | Pass   |

Verified the response, redirect, error message where applicable, and that the original email did not change for invalid IDs.

**Result:** 5 passed.

**Command:** `python -m pytest test/test_student_profile.py -v`

**Evidence:** `screenshots/Faseeh/student_profile_negative_tests.png`

### 5.5 Student Results and Notes Testing

**Functions:** `s_viewresult()` and `s_viewnotes()` in `Main_App/v_student.py`  
**Test file:** `test/test_student_content.py`

| Scenario                  | Expected behavior        |
| ------------------------- | ------------------------ |
| Same standard and medium  | Record is returned       |
| Different standard        | Record is excluded       |
| Different medium          | Record is excluded       |
| No records                | Empty list               |
| Multiple matching records | All matches are returned |

The five scenarios were run for both functions using parameterization and Django test client.

**Result:** 10 passed (5 results tests and 5 notes tests).

**Command:** `python -m pytest test/test_student_content.py -v`

**Evidence:** `screenshots/Faseeh/student_content_tests.png`

### 5.6 Student Module Test Summary

| Testing area           | Passed | Failed |
| ---------------------- | -----: | -----: |
| Medium ECP             |      6 |      0 |
| Standard BVA           |      2 |      4 |
| Profile update         |      1 |      0 |
| Password handling      |      4 |      0 |
| Negative profile tests |      5 |      0 |
| Results and notes      |     10 |      0 |
| Total                  |     28 |      4 |

**Total executions:** 32.

**Command to run Student tests:**

```powershell
python -m pytest test/test_student_model.py test/test_student_profile.py test/test_student_content.py -v
```

### 5.7 Bug Report - Student Standard Validation

**Module:** `Student` in `Main_App/models.py`  
**Technique:** BVA

**Expected:** Values 1 through 10 should be valid standards.  
**Actual:** Values 1, 2, 9, and 10 were rejected in the BVA tests.  
**Suspected cause:** The `std` field is a `CharField`, but its choices are integers.  
**Status:** Documented, not fixed.  
**Evidence:** `screenshots/Faseeh/bvafailedmodule1.png`

### 5.8 Email Authentication Testing

**Application function:** `EmailAuth.authenticate()` in `Main_App/EmailAuthentication.py`  
**Test file:** `test/test_email_auth.py`  
**Technique:** ECP, negative testing, and mocking

| Test    | Condition                  | Expected      |
| ------- | -------------------------- | ------------- |
| AUTH-01 | Valid email and password   | User returned |
| AUTH-02 | Wrong password             | None          |
| AUTH-03 | Unknown email              | None          |
| AUTH-04 | Empty email                | None          |
| AUTH-05 | Missing email              | None          |
| AUTH-06 | Empty password             | None          |
| AUTH-07 | Missing password           | None          |
| AUTH-08 | Username instead of email  | None          |
| AUTH-09 | Wrong password letter case | None          |
| AUTH-10 | Email with trailing space  | None          |

Used mock user and database objects to test the actual `authenticate()` method without accessing a real database.

**Cases written:** 10. Record the actual test result from the latest run.

**Command:** `python -m pytest test/test_email_auth.py -v`

**Evidence:** `screenshots/Faseeh/authentication_tests.png` (if saved with this name).

### 5.9 Task 3 - CSV Data-Driven Testing

**Test file:** `test/test_task3_faseeh_csv.py`  
**CSV file:** `test_data/faseeh_student_medium.csv`  
**Excel file:** `Task3_Test_Cases_Simple.xlsx`

| Case     | Input        | Expected |
| -------- | ------------ | -------- |
| F-CSV-01 | Marathi      | Valid    |
| F-CSV-02 | CBSE         | Valid    |
| F-CSV-03 | Unknown      | Invalid  |
| F-CSV-04 | Empty string | Invalid  |

Used Python's `csv.DictReader` to load external values. pytest parameterization runs one test case for each CSV row. Actual results should be copied into the Excel sheet after execution.

**Command:** `python -m pytest test/test_task3_faseeh_csv.py -v`

**Evidence:** `screenshots/Faseeh/task3_csv_tests.png` (if saved with this name).

### 5.10 Commands and Contribution

```powershell
# Student model
python -m pytest test/test_student_model.py -v

# Student profile, passwords, and invalid requests
python -m pytest test/test_student_profile.py -v

# Student results and notes
python -m pytest test/test_student_content.py -v

# Email authentication
python -m pytest test/test_email_auth.py -v

# My CSV tests
python -m pytest test/test_task3_faseeh_csv.py -v
```

I wrote automated tests, recorded the outcomes, documented the BVA defect, and contributed the email authentication and CSV tests. I did not use Selenium.
