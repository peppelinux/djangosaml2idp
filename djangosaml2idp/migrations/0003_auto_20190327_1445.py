# Generated by Django 2.0.13 on 2019-03-27 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangosaml2idp', '0002_auto_20190322_1457'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agreementrecord',
            options={'verbose_name': 'Agreement Record', 'verbose_name_plural': 'Agreement Records'},
        ),
        migrations.RemoveField(
            model_name='agreementrecord',
            name='modified',
        ),
    ]
