import csv
from pathlib import Path

import pytest
from django.core.exceptions import ValidationError
from Main_App.models import Teacher

csv_path = Path(__file__).resolve().parents[1] / "test_data" / "zohaib_teacher_gender.csv"
with csv_path.open(newline="", encoding="utf-8") as file:
    cases = list(csv.DictReader(file))


@pytest.mark.parametrize("case", cases, ids=[case["case_id"] for case in cases])
def test_teacher_gender_csv(case):
    field = Teacher._meta.get_field("gender")
    value = case["value"]
    expected = case["expected"]

    assert expected in ("valid", "invalid")

    if expected == "valid":
        assert field.clean(value, Teacher()) == value
    else:
        with pytest.raises(ValidationError):
            field.clean(value, Teacher())
