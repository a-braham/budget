# Generated by Django 3.0.8 on 2020-08-11 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_auto_20200807_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='budget',
        ),
    ]