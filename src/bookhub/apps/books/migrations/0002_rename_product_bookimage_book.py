# Generated by Django 5.0.4 on 2024-05-29 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookimage',
            old_name='product',
            new_name='book',
        ),
    ]