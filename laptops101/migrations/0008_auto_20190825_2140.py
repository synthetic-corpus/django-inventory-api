# Generated by Django 2.2.4 on 2019-08-25 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptops101', '0007_auto_20190825_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enduser',
            name='EMAIL',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]
