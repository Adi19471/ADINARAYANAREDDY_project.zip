# Generated by Django 3.2.8 on 2021-10-20 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0002_auto_20210911_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collegedate',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
