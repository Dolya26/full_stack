# Generated by Django 4.1.6 on 2023-02-10 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryCategory',
            fields=[
                ('category_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='category.category')),
                ('slug1', models.SlugField(primary_key=True, serialize=False)),
                ('name1', models.CharField(max_length=50, unique=True)),
            ],
            bases=('category.category',),
        ),
    ]
