
import pytest
from django.core.exceptions import ValidationError
from Main_App.models import Teacher


@pytest.mark.parametrize("gender", [
    "Male",
    "Female",
    "Other"
])
def test_teacher_valid_gender(gender):
    field = Teacher._meta.get_field("gender")
    assert field.clean(gender, Teacher()) == gender


@pytest.mark.parametrize("gender", [
    "Unknown",
    "",
    "InvalidGender"
])
def test_teacher_invalid_gender(gender):
    field = Teacher._meta.get_field("gender")

    with pytest.raises(ValidationError):
        field.clean(gender, Teacher())


@pytest.mark.parametrize("length", [
    14,
    15
])
def test_teacher_gender_length_within_maximum(length):
    field = Teacher._meta.get_field("gender")
    value = "A" * length

    field.run_validators(value)


def test_teacher_gender_length_exceeds_maximum():
    field = Teacher._meta.get_field("gender")
    value = "A" * 16

    with pytest.raises(ValidationError):
        field.run_validators(value)


def test_teacher_gender_default():
    teacher = Teacher()

    assert teacher.gender == "Other"


def test_teacher_address_required():
    field = Teacher._meta.get_field("address")

    with pytest.raises(ValidationError):
        field.clean("", Teacher())