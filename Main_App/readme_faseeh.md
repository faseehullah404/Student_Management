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

- Selenium with Python for automated browser/UI testing.
- pytest and pytest-django for automated unit testing.
- ECP and BVA for test case design.
- CSV for data-driven testing.
- pytest-xdist for parallel test execution.

## 5. My Work

I will create and execute my assigned student module tests, document the results, and commit my changes to GitHub.

## Bug Report — Student Standard Validation

Module: Student (`Main_App/models.py`)

Testing Technique: Boundary Value Analysis (BVA)

Expected Result: Standard values from 1 to 10 should be accepted.

Actual Result: Values 1, 2, 9, and 10 were rejected during field validation.

Test Results: 8 passed, 4 failed (including ECP tests).

Suspected Cause: The `std` field uses `CharField`, while its choices are defined as integers.

Status: Bug identified and documented. Not fixed.

Evidence: `screenshots/faseeh/student_bva_failed.png`
