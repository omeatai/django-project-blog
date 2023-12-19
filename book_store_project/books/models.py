from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.text import slugify

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
    slug = models.SlugField(default="", null=False, db_index=True, primary_key=False)

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug]) # kwargs={"pk": self.pk}

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.rating})"
