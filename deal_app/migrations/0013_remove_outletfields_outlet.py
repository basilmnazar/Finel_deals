# Generated by Django 4.2.5 on 2024-08-06 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deal_app', '0012_outletfields_outlet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outletfields',
            name='outlet',
        ),
    ]
