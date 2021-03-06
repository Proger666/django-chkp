# Generated by Django 2.0.3 on 2018-04-02 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MGMTServer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MgmtR80Name', models.CharField(max_length=250)),
                ('ServerIP', models.GenericIPAddressField()),
                ('Description', models.CharField(max_length=500)),
                ('MgmtR80VersionsSupported', models.CharField(choices=[('R80', 'old version'), ('R80.10', 'actual version')], default='R80.10', max_length=10)),
                ('MGMTR80IsAlive', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='R80Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('R80User', models.CharField(max_length=30)),
                ('R80Password', models.CharField(max_length=50)),
                ('UsersID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APIR80.MGMTServer')),
            ],
        ),
    ]
