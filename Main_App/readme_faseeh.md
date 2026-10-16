# Faseeh's Testing Notes

## Module

Student module (`Main_App/v_student.py` and Student class in `Main_App/models.py`)

I will test student profile updates, input validation, results, and notes.

## 1. ECP Student Module

Test Field Equivalence Class (Condition) Expected
ECP-01 std 1 ≤ std ≤ 10 Valid
ECP-02 std std < 1 Invalid
ECP-03 std std > 10 Invalid
ECP-04 std std is non-numeric Invalid
ECP-05 medium medium ∈ {Marathi, SemiEng, CBSE, Foundation} Valid
ECP-06 medium medium ∉ {Marathi, SemiEng, CBSE, Foundation} Invalid

## 2. BVA Student Module

Student class has standard (std) choices from 1 to 10.

Test Field Input Expected
BVA-01 std 0 (min − 1) Invalid
BVA-02 std 1 (min) Valid
BVA-03 std 2 (min + 1) Valid
BVA-04 std 9 (max − 1) Valid
BVA-05 std 10 (max) Valid
BVA-06 std 11 (max + 1) Invalid

These are the intended boundaries. Actual Django validation behavior will be checked through automated tests.

## 3. Other Test Cases

1. Check if student profile is updated with correct information.
2. Check if the student password is updated correctly.
3. Check if an empty password leaves the old password unchanged.
4. Check if results are filtered by the student's standard and medium.
5. Check if notes are filtered by the student's standard and medium.
6. Check if invalid student details are handled correctly.

## 4. Testing Method

I will use:

- pytest and pytest-django for automated unit testing.
- ECP and BVA for test case design.
- CSV for data-driven testing.
- pytest-xdist for parallel test execution.

## 5. My Work

**Module:** Student Module

**Application Files:** `Main_App/models.py`, `Main_App/v_student.py`

**Testing Tools:** Python, pytest, pytest-django, Django Test Client

I performed automated testing of student model validation, profile updates, password handling, invalid requests, and student content filtering.

### 5.1 Student Model Testing — ECP and BVA

**Test File:** `test/test_student_model.py`

**Application Code:** `Student` class in `Main_App/models.py`

**ECP Testing:**

- Tested valid medium choices: Marathi, SemiEng, CBSE, Foundation.
- Tested invalid medium inputs: Unknown and empty string.
- Used `@pytest.mark.parametrize` and Django's `field.clean()` for validation.

**Result:** 6 Passed

**BVA Testing:**

- Tested `std` (student standard/class) with values 0, 1, 2, 9, 10, 11.
- Checked both lower and upper boundaries.
- Identified that valid standard values were being rejected during validation.

**Result:** 2 Passed, 4 Failed

**Bug Identified:** The `std` field is a `CharField`, but its choices are defined using integers. This causes a mismatch during field validation when string values are supplied.

**Status:** Bug documented, not fixed.

**Run Command:**

`python -m pytest test/test_student_model.py -v`

**Evidence:**

- `screenshots/faseeh/student_ecp_passed.png`
- `screenshots/faseeh/student_bva_failed.png`

### 5.2 Student Profile Update Testing

**Test File:** `test/test_student_profile.py`

**Function:** `s_saveprofile()`

Tested successful profile updates using the Django test client.

**Verified:**

- First name updated.
- Last name updated.
- Email updated.
- Address updated.
- Gender updated.
- Successful redirect to `/studentprofile`.

Test data was created in the test database, a POST request was submitted, and updated values were verified using assertions.

**Result:** 1 Passed

**Run Command:**

`python -m pytest test/test_student_profile.py -v`

**Evidence:** `screenshots/faseeh/student_profile_update.png`

### 5.3 Student Password Update Testing

**Test File:** `test/test_student_profile.py`

**Function:** `s_saveprofile()`

**Technique:** ECP and condition testing

| Password Input         | Expected Behavior         | Result |
| ---------------------- | ------------------------- | ------ |
| `None` (field omitted) | Old password unchanged    | PASS   |
| `""`                   | Old password unchanged    | PASS   |
| `" "`                  | Password updated to space | PASS   |
| `"NewPass456!"`        | New password saved        | PASS   |

**Work Performed:**

- Tested both branches of the password update condition.
- Used parameterization for four different scenarios.
- Verified passwords using `check_password()`.
- Found that whitespace-only passwords are accepted by the current implementation.

**Result:** 4 Passed

**Run Command:**

`python -m pytest test/test_student_profile.py -v`

**Evidence:** `screenshots/faseeh/student_password_tests.png`

### 5.4 Student Profile Negative Testing

**Test File:** `test/test_student_profile.py`

**Function:** `s_saveprofile()`

**Technique:** Negative testing and invalid input testing

| Test Case | Input / Condition      | Expected Behavior | Result |
| --------- | ---------------------- | ----------------- | ------ |
| TC-01     | GET request            | Update rejected   | PASS   |
| TC-02     | PUT request            | Update rejected   | PASS   |
| TC-03     | Nonexistent student ID | Error handled     | PASS   |
| TC-04     | Non-numeric student ID | Error handled     | PASS   |
| TC-05     | Missing student ID     | Error handled     | PASS   |

**Work Performed:**

- Tested rejection of non-POST requests.
- Tested error handling for invalid student identifiers.
- Verified failure messages and redirects.
- Confirmed original user email remained unchanged for the tested invalid IDs.

**Result:** 5 Passed

**Run Command:**

`python -m pytest test/test_student_profile.py -v`

**Evidence:** `screenshots/faseeh/student_profile_negative_tests.png`

### 5.5 Student Results and Notes Filtering

**Test File:** `test/test_student_content.py`

**Functions:** `s_viewresult()` and `s_viewnotes()`

Verified that students receive results and notes filtered according to their standard and medium.

| Test Scenario                | Expected Behavior             |
| ---------------------------- | ----------------------------- |
| Matching standard and medium | Record included               |
| Different standard           | Record excluded               |
| Different medium             | Record excluded               |
| No records                   | Empty collection              |
| Multiple matching records    | All matching records included |

The five scenarios were executed for both Results and Notes using parameterization.

**Work Performed:**

- Created temporary student and content records in the test database.
- Simulated authenticated requests using Django test client.
- Verified standard and medium filtering.
- Checked response context using assertions.
- Tested multiple matching and nonmatching records.

**Result:** 10 Passed

**Run Command:**

`python -m pytest test/test_student_content.py -v`

**Evidence:** `screenshots/faseeh/student_content_tests.png`

### 5.6 Overall Test Execution Results

| Testing Activity                 | Passed | Failed |
| -------------------------------- | -----: | -----: |
| Student Model ECP                |      6 |      0 |
| Student Model BVA                |      2 |      4 |
| Student Profile Update           |      1 |      0 |
| Password Condition Testing       |      4 |      0 |
| Student Profile Negative Testing |      5 |      0 |
| Results and Notes Filtering      |     10 |      0 |
| **Total**                        | **28** |  **4** |

**Total Test Executions:** 32

**Known Defect:** Four BVA cases fail due to student standard choice validation.

### 5.7 Commands to Execute Tests

**Student Model — ECP and BVA:**

`python -m pytest test/test_student_model.py -v`

**Student Profile, Password and Negative Tests:**

`python -m pytest test/test_student_profile.py -v`

**Student Results and Notes:**

`python -m pytest test/test_student_content.py -v`

**Run All Student Tests:**

`python -m pytest test/test_student_model.py test/test_student_profile.py test/test_student_content.py -v`

**Expected combined outcome based on recorded executions:** 28 passed, 4 failed.

The failed cases are documented validation defects and have not been removed or changed to force passing results.

### 5.8 Summary of Contribution

I developed automated tests for the Student Module covering model validation, boundary values, profile updates, password conditions, invalid requests, and content filtering.

I used pytest parameterization, Django model validation, Django test client, assertions, and an isolated test database.

The tests identified a potential standard validation defect and demonstrated the current behavior of password and profile handling.

### 5.9 Tools Used

- Python
- pytest
- pytest-django
- Django Test Client

All tests were automated using pytest without Selenium.

**Remaining Work:** Student password update testing and further test coverage.

## Bug Report — Student Standard Validation

Module: Student (`Main_App/models.py`)

Testing Technique: Boundary Value Analysis (BVA)

Expected Result: Standard values from 1 to 10 should be accepted.

Actual Result: Values 1, 2, 9, and 10 were rejected during field validation.

Test Results: 8 passed, 4 failed (including ECP tests).

Suspected Cause: The `std` field uses `CharField`, while its choices are defined as integers.

Status: Bug identified and documented. Not fixed.

Evidence: `screenshots/faseeh/student_bva_failed.png`
