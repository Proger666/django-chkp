# Generated by Django 2.1.1 on 2018-10-13 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APIR80', '0004_mgmtserver_mgmtport'),
    ]

    operations = [
        migrations.CreateModel(
            name='MGMTServerObjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MGMTServerPortsFilePath', models.CharField(default='/home/carlos/django-chkp/APIR80/tmp/portschkp.txt', max_length=250)),
                ('MGMTServerObjectsFilePath', models.CharField(default='/home/carlos/django-chkp/APIR80/tmp/objectschkp.txt', max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='mgmtserver',
            name='Description',
            field=models.TextField(max_length=500),
        ),
        migrations.AddField(
            model_name='mgmtserverobjects',
            name='MGMTServerObjectsID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APIR80.MGMTServer'),
        ),
    ]
