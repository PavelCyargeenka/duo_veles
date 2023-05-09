from django.core.exceptions import ValidationError
from datetime import datetime


def life_years_validator(value):
    x = datetime.now()
    current_year = x.year
    if len(value) not in [4, 9]:
        raise ValidationError('Please enter a valid birth year or living years range')
    if len(value) == 4:
        if not value.isdigit() or int(value) < 1000 or int(value) > 2010:
            raise ValidationError('Please enter a valid birth year')
    else:
        if value[4] != '-' or not value[:4].isdigit() or not value[5:].isdigit() \
                or int(value[:4]) < 1000 or int(value[:4]) > 2000 \
                or int(value[5:]) < 1020 or int(value[5:]) > current_year \
                or int(value[5:]) - int(value[:4]) not in range(20, 100):
            raise ValidationError('Please enter a valid living years range')