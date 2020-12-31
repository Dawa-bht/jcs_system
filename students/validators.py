from django.core.exceptions import ValidationError


def validate_cid(value):
    if len(value) != 11:
        raise ValidationError("Cid number should have 11 digits.")
    return value


def validate_phone(value):
    if len(value) != 8:
        raise ValidationError("Phone number should have 8 digits.")
    return value


def validate_email(value):
    if '@education.gov.bt' not in value:
        raise ValidationError("We accept only education mail")
    return value
