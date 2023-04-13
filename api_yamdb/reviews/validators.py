import datetime as dt

from django.core.exceptions import ValidationError


def validate_year(data):
    year = dt.date.today().year
    if year < data:
        raise ValidationError(
            f'Год {data} больше текущего!',
        )
