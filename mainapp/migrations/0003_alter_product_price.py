# Generated by Django 4.2.1 on 2024-02-22 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_newproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
