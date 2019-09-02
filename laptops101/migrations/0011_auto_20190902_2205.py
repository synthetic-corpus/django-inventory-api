# Generated by Django 2.2.4 on 2019-09-02 22:05

from django.db import migrations, models
import laptops101.customValidators


class Migration(migrations.Migration):

    dependencies = [
        ('laptops101', '0010_auto_20190902_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enduser',
            name='FIRST_NAME',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='ASSET_TAG',
            field=models.CharField(max_length=8, unique=True, validators=[laptops101.customValidators.validate_test]),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='ASSET_TAG',
            field=models.CharField(max_length=8, unique=True, validators=[laptops101.customValidators.validate_test]),
        ),
    ]
