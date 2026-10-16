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

I have performed automated testing on the Student Module using Python, pytest, and pytest-django.

### 5.1 Student Model Testing

File: `test/test_student_model.py`

Testing Techniques: Equivalence Class Partitioning (ECP) and Boundary Value Analysis (BVA)

ECP Testing:

- Tested valid medium values: Marathi, SemiEng, CBSE, Foundation.
- Tested invalid medium values: Unknown and empty string.
- Used `@pytest.mark.parametrize` for multiple test inputs.
- Result: 6 Passed

BVA Testing:

- Tested Student Standard (`std`) field with boundary values: 0, 1, 2, 9, 10, 11.
- Used Django field validation to check valid and invalid values.
- **Result: 2 Passed, 4 Failed**
- Identified a potential validation bug where valid standard values were rejected.
- The suspected cause is a mismatch between integer choices and the `CharField` data type.
- The issue was documented without modifying the original application code.

Command to Run:

```bash
python -m pytest test/test_student_model.py -v
```

Screenshots:

- `screenshots/faseeh/student_ecp_passed.png`
- `screenshots/faseeh/student_bva_failed.png`

### 5.2 Student Profile Update Testing

File: `test/test_student_profile.py`

Function Tested: `s_saveprofile()`

Testing Framework: pytest + pytest-django

Test Case: Student Profile Update

- Created a test student user and student profile.
- Used Django test client to simulate login.
- Sent a POST request with updated student information.
- Verified successful update of first name, last name, email, address, and gender.
- Verified successful redirection after profile update.
- Used assertions to compare expected and actual results.

Result: 1 Passed

Command to Run:

```bash
python -m pytest test/test_student_profile.py -v
```

Screenshot:

- `screenshots/faseeh/student_profile_update.png`

### 5.3 Student Password Update Testing

File: `test/test_student_profile.py`

Function Tested: `s_saveprofile()`

Testing Technique: Equivalence Class Partitioning (ECP) and Condition Testing

Test Cases:

| Input                  | Expected Result               | Actual Result |
| ---------------------- | ----------------------------- | ------------- |
| `None` (field omitted) | Old password unchanged        | PASS          |
| `""` (empty string)    | Old password unchanged        | PASS          |
| `" "` (single space)   | Password updated to space     | PASS          |
| `"NewPass456!"`        | Password updated successfully | PASS          |

Work Performed:

- Used `@pytest.mark.parametrize` to execute four password scenarios.
- Used Django test client to send profile update requests.
- Verified passwords using `check_password()`.
- Confirmed that `None` and empty passwords leave the old password unchanged.
- Observed that the application accepts whitespace-only passwords, which may be a validation weakness.

Result: 4 Passed

**Command to Run:**

```bash
python -m pytest test/test_student_profile.py -v
```

Screenshot: `screenshots/faseeh/student_password_tests.png`

**Command to Run All My Tests:**

```bash
python -m pytest test/test_student_model.py test/test_student_profile.py -v
```

### 5.4 Tools Used

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
