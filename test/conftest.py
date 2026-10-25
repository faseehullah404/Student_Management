from pathlib import Path
import pytest


# Decide suite based on the existing test filenames.
def suite_for(filename):
    if filename.startswith("test_task3_"):
        return "csvdata"
    if filename.startswith("test_student_"):
        return "student"
    if filename.startswith("test_teacher_"):
        return "teacher"
    if "auth" in filename or "login" in filename:
        return "auth"
    return None


# Group the tests and give their collection a predictable order.
def pytest_collection_modifyitems(items):
    order = {"student": 0, "teacher": 1, "auth": 2, "csvdata": 3}
    for item in items:
        filename = Path(str(item.path)).name.lower()
        suite = suite_for(filename)
        if suite:
            item.add_marker(getattr(pytest.mark, suite))

    items.sort(key=lambda item: (
        order.get(suite_for(Path(str(item.path)).name.lower()), 99),
        str(item.path),
        item.location[1],  # test source line
        item.name,
    ))
