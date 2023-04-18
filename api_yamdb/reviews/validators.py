from django.core.exceptions import ValidationError
from django.utils import timezone


def year_validator(year):
    if not (0 < year <= timezone.now().year):
        raise ValidationError('Год указан не верно')
