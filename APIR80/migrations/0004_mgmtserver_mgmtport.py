# Generated by Django 2.1.1 on 2018-10-01 02:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIR80', '0003_ansiblegeneraldeploy'),
    ]

    operations = [
        migrations.AddField(
            model_name='mgmtserver',
            name='MgmtPort',
            field=models.PositiveIntegerField(default=443, validators=[django.core.validators.MaxValueValidator(65525)]),
        ),
    ]
