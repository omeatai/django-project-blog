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

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()

    def full_name(self):
        return f"{self.first_name} {self.last_name} ({self.age})"

    def __str__(self):
        return self.full_name()

class Book(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(
        validators=[validate_not_a_number, MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True, related_name="author_books")
    # models.CASCADE, models.PROTECT, models.SET_NULL, models.SET_DEFAULT, models.DO_NOTHING
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, blank=True, editable=True, db_index=True, primary_key=False)

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug]) # kwargs={"pk": self.pk}

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.rating})"


# class Author(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()


# class Publisher(models.Model):
#     name = models.CharField(max_length=300)


# class Book(models.Model):
#     name = models.CharField(max_length=300)
#     pages = models.IntegerField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     rating = models.FloatField()
#     authors = models.ManyToManyField(Author)
#     publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
#     pubdate = models.DateField()


# class Store(models.Model):
#     name = models.CharField(max_length=300)
#     books = models.ManyToManyField(Book)
