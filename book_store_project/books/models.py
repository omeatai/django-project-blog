from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_not_a_number(value):
    if not str(value).isdigit():
        raise ValidationError(
            _("%(value)s is not a number!"),
            params={"value": value},
        )

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(
        validators=[validate_not_a_number, MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(blank=True, null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    # id = models.AutoField(primary_key=True)
    # author = models.CharField(max_length=100)
    # price = models.DecimalField(max_digits=5, decimal_places=2)
    # cover = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        return f"{self.title} ({self.rating})"

###
