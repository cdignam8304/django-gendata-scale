# Generated by Django 2.2.12 on 2020-05-22 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20200522_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schema',
            name='date1',
            field=models.CharField(max_length=200, null=True, verbose_name='date1'),
        ),
        migrations.AlterField(
            model_name='schema',
            name='date2',
            field=models.CharField(max_length=200, null=True, verbose_name='date2'),
        ),
        migrations.AlterField(
            model_name='schema',
            name='date3',
            field=models.CharField(max_length=200, null=True, verbose_name='date3'),
        ),
        migrations.AlterField(
            model_name='schema',
            name='string2',
            field=models.CharField(max_length=200, null=True, verbose_name='string2'),
        ),
        migrations.AlterField(
            model_name='schema',
            name='string3',
            field=models.CharField(max_length=200, null=True, verbose_name='string3'),
        ),
        migrations.AlterField(
            model_name='schema',
            name='string4',
            field=models.CharField(max_length=200, null=True, verbose_name='string4'),
        ),
        migrations.AlterField(
            model_name='schema',
            name='string5',
            field=models.CharField(max_length=200, null=True, verbose_name='string5'),
        ),
    ]
