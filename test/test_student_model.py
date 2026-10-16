
import pytest
from django.core.exceptions import ValidationError
from Main_App.models import Student


# ECP: Valid medium equivalence class
@pytest.mark.parametrize("medium", [
    "Marathi", "SemiEng", "CBSE", "Foundation"
])
def test_valid_medium(medium):
    field = Student._meta.get_field("medium")
    assert field.clean(medium, Student()) == medium


# ECP: Invalid medium equivalence class
@pytest.mark.parametrize("medium", [
    "Unknown", ""
])
def test_invalid_medium(medium):
    field = Student._meta.get_field("medium")

    with pytest.raises(ValidationError):
        field.clean(medium, Student())


# BVA: Student Standard (1 to 10)

@pytest.mark.parametrize("std, expected_valid", [
    (0, False),   
    (1, True),    
    (2, True),    
    (9, True),    
    (10, True),   
    (11, False)   
])
def test_std_boundary(std, expected_valid):
    field = Student._meta.get_field("std")

    try:
        field.clean(str(std), Student())
        actual_valid = True
    except ValidationError:
        actual_valid = False

    assert actual_valid == expected_valid, (
        f"Standard {std}: Expected valid={expected_valid}, "
        f"but got valid={actual_valid}"
    )
