# Generated by Django 2.2.4 on 2019-08-11 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EndUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIRST_NAME', models.CharField(max_length=255)),
                ('LAST_NAME', models.CharField(max_length=255)),
                ('TITLE', models.CharField(max_length=255)),
                ('DEPARTMENT', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ItemArchetype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SKU', models.CharField(max_length=255)),
                ('COMMON_NAME', models.CharField(max_length=255)),
                ('NOTES', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MANUFACTURER', models.CharField(max_length=255)),
                ('WEBSITE', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TagInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PURCHASE_DATE', models.DateField()),
                ('PURCHASE_COST', models.DecimalField(decimal_places=2, max_digits=7)),
                ('ASSET_TAG', models.CharField(max_length=8)),
                ('ASSIGNED_USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laptops101.EndUser')),
            ],
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CPU_MODEL', models.CharField(max_length=128)),
                ('CPU_SPEED', models.DecimalField(decimal_places=2, max_digits=3)),
                ('RAM', models.IntegerField()),
                ('HDD', models.DecimalField(decimal_places=2, max_digits=4)),
                ('NOTES', models.CharField(max_length=255)),
                ('ARCHETYPE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laptops101.ItemArchetype')),
                ('TAG', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laptops101.TagInformation')),
            ],
        ),
        migrations.AddField(
            model_name='itemarchetype',
            name='MANUFACTURER',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laptops101.Manufacturer'),
        ),
    ]