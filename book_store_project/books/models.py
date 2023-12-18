from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField()
    # id = models.AutoField(primary_key=True)
    # author = models.CharField(max_length=100)
    # price = models.DecimalField(max_digits=5, decimal_places=2)
    # cover = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        return f"{self.title}"
