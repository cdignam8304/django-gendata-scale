# Generated by Django 2.2.12 on 2020-05-22 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20200522_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='mktg_opt_in',
            field=models.BooleanField(choices=[('IN', 'In'), ('OUT', 'Out')], default='IN', max_length=3),
        ),
    ]
