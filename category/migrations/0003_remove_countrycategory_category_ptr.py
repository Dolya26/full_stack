# Generated by Django 4.1.6 on 2023-02-13 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_countrycategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='countrycategory',
            name='category_ptr',
        ),
    ]