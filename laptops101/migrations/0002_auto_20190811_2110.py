# Generated by Django 2.2.4 on 2019-08-11 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laptops101', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemarchetype',
            name='MANUFACTURER',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='laptops101.Manufacturer'),
        ),
        migrations.AlterField(
            model_name='taginformation',
            name='ASSIGNED_USER',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='laptops101.EndUser'),
        ),
    ]
