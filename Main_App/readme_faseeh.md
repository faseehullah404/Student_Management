# Faseeh's Testing Notes

## Module

Student model (`Main_App/models.py`)

I will test student data and check which values are allowed.

## 1. ECP (Equivalence Class Partitioning)

| Test | Input          | Expected Result |
| ---- | -------------- | --------------- |
| 1    | Class 1        | Valid           |
| 2    | Class 5        | Valid           |
| 3    | Class 10       | Valid           |
| 4    | Class 0        | Invalid         |
| 5    | Class 11       | Invalid         |
| 6    | Gender Male    | Valid           |
| 7    | Gender Female  | Valid           |
| 8    | Gender Other   | Valid           |
| 9    | Gender Unknown | Invalid         |

## 2. BVA (Boundary Value Analysis)

Student class choices are from 1 to 10.

| Test | Input | Expected Result |
| ---- | ----- | --------------- |
| 1    | 0     | Invalid         |
| 2    | 1     | Valid           |
| 3    | 2     | Valid           |
| 4    | 9     | Valid           |
| 5    | 10    | Valid           |
| 6    | 11    | Invalid         |

## 3. Other Test Cases

1. Check if a student can be created with valid data.
2. Check the default gender value.
3. Check if the selected medium is valid.
4. Check if a student profile is created for a student user.
5. Check if required fields are entered.

## 4. Testing Method

I will use Selenium with Python and pytest for automated browser tests.

I will also check model validation where needed.

## 5. My Work

I will write the test cases, run the tests, and commit my changes to GitHub.
