# Generated by Django 5.0.4 on 2024-05-29 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='name')),
                ('slug', models.SlugField(allow_unicode=True, max_length=255, unique=True, verbose_name='slug')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/authors/images/', verbose_name='image')),
                ('location', models.CharField(blank=True, max_length=255, null=True, verbose_name='location')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='birthday')),
                ('biography', models.TextField(blank=True, null=True, verbose_name='biography')),
            ],
            options={
                'verbose_name': 'author',
                'verbose_name_plural': 'authors',
            },
        ),
    ]