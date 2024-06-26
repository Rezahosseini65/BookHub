# Generated by Django 5.0.4 on 2024-05-29 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=64, null=True, verbose_name='Title')),
                ('image', models.ImageField(height_field='height', upload_to='images/books/', verbose_name='Image', width_field='width')),
                ('width', models.IntegerField(editable=False, verbose_name='Width')),
                ('height', models.IntegerField(editable=False, verbose_name='height')),
                ('file_hash', models.CharField(db_index=True, editable=False, max_length=40, verbose_name='File hash')),
                ('file_size', models.PositiveIntegerField(editable=False, null=True, verbose_name='File size')),
                ('focal_point_x', models.PositiveIntegerField(blank=True, null=True, verbose_name='Focal point X')),
                ('focal_point_y', models.PositiveIntegerField(blank=True, null=True, verbose_name='Focal point Y')),
                ('focal_point_width', models.PositiveIntegerField(blank=True, null=True, verbose_name='Focal point width')),
                ('focal_point_height', models.PositiveIntegerField(blank=True, null=True, verbose_name='Focal point height')),
            ],
        ),
    ]
