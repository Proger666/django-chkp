# Generated by Django 2.1.1 on 2018-10-14 15:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('APIR80', '0008_mgmtserverobjectsnetworks'),
    ]

    operations = [
        migrations.AddField(
            model_name='mgmtserver',
            name='LastPublishSession',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
