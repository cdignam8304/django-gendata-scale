# Generated by Django 2.2.12 on 2020-05-25 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_schema_photo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='ContactType',
        ),
    ]