# Generated by Django 5.0 on 2023-12-20 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_author_alter_book_slug_alter_book_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='author',
            old_name='lastname',
            new_name='last_name',
        ),
    ]