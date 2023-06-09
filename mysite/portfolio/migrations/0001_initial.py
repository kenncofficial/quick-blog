# Generated by Django 3.2.11 on 2022-10-26 19:27

import ckeditor.fields
import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio_Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('client', models.CharField(max_length=255)),
                ('project_date', models.DateField(auto_now_add=True)),
                ('tools_used', models.CharField(max_length=255, null=True)),
                ('Discription', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
                ('image2', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
                ('image3', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
                ('project_url', models.URLField(default='non given', max_length=255)),
            ],
        ),
    ]
