# Zohaib's Testing Notes

## Module

Teacher module (`Main_App/v_teacher.py` and Teacher class in `Main_App/models.py`)

I will test teacher profile updates, input validation, password changes, and access restrictions.

## 1. ECP Teacher Module

| Test | Field | Equivalence Class (Condition) | Expected |
|---|---|---|---|
| ECP-01 | gender | gender ∈ {Male, Female, Other} | Valid |
| ECP-02 | gender | gender ∉ {Male, Female, Other} | Invalid |
| ECP-03 | address | address is non-empty | Valid |
| ECP-04 | address | address is empty | Invalid |

## 2. BVA Teacher Module

Teacher class has a `gender` field with a maximum length of 15 characters.

| Test | Field | Input | Expected |
|---|---|---|---|
| BVA-01 | gender | 14 characters | Within length limit |
| BVA-02 | gender | 15 characters | Within length limit |
| BVA-03 | gender | 16 characters | Invalid |
| BVA-04 | address | Empty string | Invalid |
| BVA-05 | address | Non-empty string | Valid |

These are the intended boundaries. Actual Django validation behavior will be checked through automated tests. Gender choice validation is separate from length validation.

## 3. Other Test Cases

1. Check if teacher profile is updated with correct information.
2. Check if the teacher password is updated correctly.
3. Check if an empty password leaves the old password unchanged.
4. Check if a GET request to the profile update endpoint is rejected.
5. Check if unauthenticated users are redirected to the login page.
6. Check if non-teacher users are prevented from accessing teacher-only pages.
7. Check if invalid teacher details are handled correctly.

## 4. Testing Method

I will use:

- pytest and pytest-django for automated model and view testing.
- ECP and BVA for test case design.
- Django test client for profile update and access restriction testing.
- Parametrized tests for testing multiple input values.

## 5. My Work

I will create and execute my assigned teacher module tests, document the results, and commit my changes to GitHub.

## Test Files

- `test/test_teacher_model.py`
- `test/test_teacher_profile.py`

## Testing Commands

Run teacher model tests:

```bash
python -m pytest test/test_teacher_model.py -v
```

Run teacher profile tests:

```bash
python -m pytest test/test_teacher_profile.py -v
```

Run all tests:

```bash
python -m pytest -v
```

## Bug Report — Teacher Profile Validation

Module: Teacher (`Main_App/models.py` and `Main_App/v_teacher.py`)

Testing Technique: Equivalence Class Partitioning (ECP) and Boundary Value Analysis (BVA)

Expected Result: Teachers should be able to update their profile with valid details, while invalid input should be handled appropriately.

Actual Result: To be confirmed after executing the teacher profile tests.

Test Results: Model tests passed. Profile tests are pending execution.

Status: Profile testing in progress. Any confirmed bugs will be documented separately.

Evidence: `screenshots/Zohaib/`
