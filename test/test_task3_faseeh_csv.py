import csv
from pathlib import Path

import pytest
from django.core.exceptions import ValidationError
from Main_App.models import Student
csv_path = Path(__file__).resolve().parents[1] / "test_data" / "faseeh_student_medium.csv"
with csv_path.open(newline="", encoding="utf-8") as file:
    cases = list(csv.DictReader(file))

@pytest.mark.parametrize("case", cases, ids=[case["case_id"] for case in cases])
def test_student_medium_csv(case):
    field = Student._meta.get_field("medium")
    value = case["value"]
    expected = case["expected"]

    assert expected in ("valid", "invalid")

    if expected == "valid":
        assert field.clean(value, Student()) == value
    else:
        with pytest.raises(ValidationError):
            field.clean(value, Student())
