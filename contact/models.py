from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models


class ContactModel(models.Model):
    name = models.CharField(null=False, validators=[MinLengthValidator(3)], max_length=30)
    e_mail = models.EmailField(null=False, default='')
    message = models.TextField(null=False, max_length=500, validators=[MinLengthValidator(2)])

    def __str__(self):
        return f'{self.name} * {self.e_mail} message'
