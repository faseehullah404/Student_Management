# Zohaib's Testing Notes

## Module

Teacher module (`Main_App/models.py`, `Main_App/v_teacher.py`) and Login (`Main_App/views.py`).

I tested teacher model validation, profile updates, passwords, results, notes, and access restrictions.

## 1. ECP Teacher Module

| Test | Field | Equivalence Class (Condition) | Expected |
|---|---|---|---|
| ECP-01 | gender | gender is Male, Female, or Other | Valid |
| ECP-02 | gender | gender is not an allowed choice | Invalid |
| ECP-03 | address | address is non-empty | Valid |
| ECP-04 | address | address is empty | Invalid |

## 2. BVA Teacher Module

The Teacher gender field has `max_length=15`.

| Test | Field | Input | Expected |
|---|---|---|---|
| BVA-01 | gender length | 14 characters | Within length limit |
| BVA-02 | gender length | 15 characters | Within length limit |
| BVA-03 | gender length | 16 characters | Invalid |
| BVA-04 | address | Empty string | Invalid |
| BVA-05 | address | Non-empty string | Valid |

Gender choice validation is different from length validation. A 14-character string can satisfy the length limit but fail the gender choice rule. The tests check these separately.

## 3. Other Test Cases

1. Update teacher first name, last name, email, gender, and address.
2. Check that an empty password keeps the old password.
3. Check that a new password is saved.
4. Reject GET requests for profile updates.
5. Redirect unauthenticated users to the login page.
6. Show teacher results and notes for different standards and mediums.
7. Return an empty collection if no content exists.
8. Test login with valid and invalid credentials.

## 4. Testing Method

- pytest and pytest-django for automated testing.
- ECP and BVA for input test design.
- Django test client and test database for profile and content tests.
- Parameterized tests for several inputs and content scenarios.
- External CSV data for Task 3.
- pytest-xdist for Task 4 parallel execution.

## 5. My Work

### 5.1 Teacher Model Testing

**Application code:** `Teacher` class in `Main_App/models.py`  
**Test file:** `test/test_teacher_model.py`

Checked allowed and disallowed gender values, gender length 14/15/16, default gender `Other`, and required address validation.

Gender length is checked using field validators separately from choices.

**Result:** 11 passed.

**Command:** `python -m pytest test/test_teacher_model.py -v`

**Evidence:**
- `screenshots/Zohaib/ecp_passed_teacher_module.png`
- `screenshots/Zohaib/BVA_passed_teacher.png`

### 5.2 Teacher Profile Testing

**Function:** `t_saveprofile()` in `Main_App/v_teacher.py`  
**Test file:** `test/test_teacher_profile.py`

Tested successful update, empty password, new password, rejection of GET requests, and unauthenticated access.

**Result:** 5 passed.

**Command:** `python -m pytest test/test_teacher_profile.py -v`

**Evidence:** `screenshots/Zohaib/teacher_profile_update.png`

### 5.3 Teacher Results and Notes Testing

**Functions:** `t_viewresult()` and `t_viewnotes()` in `Main_App/v_teacher.py`  
**Test file:** `test/test_teacher_content.py`

Tested content with different standards and mediums, no records, multiple records, and access without login. Teacher content pages display the available content rather than filtering it to one teacher's class/medium.

**Result:** 12 passed (10 content scenarios and 2 login restriction cases).

**Command:** `python -m pytest test/test_teacher_content.py -v`

**Evidence:** `screenshots/Zohaib/teacher_content_test.png`

### 5.4 Login Module Testing

**Function:** `loginuser()` in `Main_App/views.py`

I added automated login tests as my contribution to the third application area (Authentication/Login).

The latest login test filename and exact execution results must be copied from the updated GitHub branch. They are not present in the older ZIP used to review the existing Teacher tests.

**Run login-named tests:** `python -m pytest test/ -k login -v`

### 5.5 Task 3 - CSV Data-Driven Testing

**Test file:** `test/test_task3_zohaib_csv.py`  
**CSV file:** `test_data/zohaib_teacher_gender.csv`  
**Excel file:** `Task3_Test_Cases_Simple.xlsx`

| Case | Input | Expected |
|---|---|---|
| Z-CSV-01 | Male | Valid |
| Z-CSV-02 | Female | Valid |
| Z-CSV-03 | Unknown | Invalid |
| Z-CSV-04 | Empty string | Invalid |

Used `csv.DictReader` to read external data, then checked Django Teacher gender field validation with parameterized pytest cases. Actual results should be entered into the Excel sheet after execution.

**Command:** `python -m pytest test/test_task3_zohaib_csv.py -v`

**Evidence:** `screenshots/Zohaib/task3_csv_tests.png` (if saved with this name).

### 5.6 Existing Teacher Test Summary

| Testing area | Passed | Failed |
|---|---:|---:|
| Teacher model | 11 | 0 |
| Teacher profile | 5 | 0 |
| Teacher results and notes | 12 | 0 |
| Total before Login and CSV | 28 | 0 |

Login and CSV results should be added from the latest local execution. No confirmed Teacher defect was found in the existing recorded test runs.

### 5.7 Testing Commands

```powershell
# Teacher model
python -m pytest test/test_teacher_model.py -v

# Teacher profile
python -m pytest test/test_teacher_profile.py -v

# Teacher results and notes
python -m pytest test/test_teacher_content.py -v

# Login tests (if their names contain 'login')
python -m pytest test/ -k login -v

# My CSV tests
python -m pytest test/test_task3_zohaib_csv.py -v
```

I completed and documented my Teacher tests and contributed Login and CSV testing. I used pytest instead of Selenium.

### 5.8 Task 4 - Test Execution

I worked on test suite execution and verification.

**File:**
- `run_suites.ps1`

**Work Performed:**
- Verified the execution of separate test groups.
- Used a PowerShell script to run test suites sequentially.
- Verified the execution order: Student, Teacher, Authentication, CSV.
- Tested parallel execution using pytest-xdist.
- Verified that test execution continues even if an earlier group has failed tests.

**Commands Used:**

Run suites in order:

`powershell -ExecutionPolicy Bypass -File .\run_suites.ps1`

Run tests in parallel:

`python -m pytest test/ -n 2 --dist loadfile -v`

Run Teacher group:

`python -m pytest test/ -m teacher -v`

**Result:** Ordered and parallel test execution commands ran successfully.

Known Student BVA failures remain documented.