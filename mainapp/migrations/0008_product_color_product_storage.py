# Generated by Django 4.2.1 on 2024-02-22 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_rename_desc_product_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='storage',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
    ]
