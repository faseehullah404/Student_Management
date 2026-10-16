# Faseeh's Testing Notes

## Module

Student module (`Main_App/v_student.py` and Student class in `Main_App/models.py`)

I will test student profile updates, input validation, results, and notes.

## 1. ECP (Equivalence Class Partitioning)

| Test | Input / Condition                                 | Expected Result                     |
| ---- | ------------------------------------------------- | ----------------------------------- |
| 1    | Valid student profile data                        | Profile updated successfully        |
| 2    | Invalid student ID                                | Profile update fails                |
| 3    | Empty password during profile update              | Existing password remains unchanged |
| 4    | Non-empty password during profile update          | Password is updated                 |
| 5    | Valid medium (Marathi, SemiEng, CBSE, Foundation) | Accepted by model validation        |
| 6    | Invalid medium (Unknown)                          | Rejected by model validation        |
| 7    | GET request to profile update function            | Method not allowed                  |

## 2. BVA (Boundary Value Analysis)

Student class has standard (std) choices from 1 to 10.

| Test | Input       | Expected Result |
| ---- | ----------- | --------------- |
| 1    | Standard 0  | Invalid         |
| 2    | Standard 1  | Valid (minimum) |
| 3    | Standard 2  | Valid           |
| 4    | Standard 10 | Valid (maximum) |
| 5    | Standard 11 | Invalid         |

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
