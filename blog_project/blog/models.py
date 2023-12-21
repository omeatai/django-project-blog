from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.text import slugify

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.caption}"


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email_address}"


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True, editable=False)
    content = models.TextField(validators=[MinLengthValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="author_posts")
    tag = models.ManyToManyField(Tag, related_name="tag_posts")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {self.author.first_name} {self.author.last_name}"


##