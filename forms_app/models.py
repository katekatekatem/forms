from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from .validators import validate_date


TYPE_CHOICES = (
    ('text', models.TextField(blank=True)),
    ('email', models.EmailField(blank=True)),
    ('phone', PhoneNumberField(region="RU", blank=True)),
    ('date', models.DateField(
        null=True,
        blank=True,
        help_text='YYYY-MM-DD or DD.MM.YYYY',
        validators=[validate_date]
    )),
)


class FormTemplate(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class FormField(models.Model):
    template = models.ForeignKey(FormTemplate, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=5, choices=TYPE_CHOICES)

    def __str__(self):
        return self.name
