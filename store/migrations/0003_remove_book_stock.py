# Generated by Django 3.2.12 on 2022-03-23 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20220323_0229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='stock',
        ),
    ]
