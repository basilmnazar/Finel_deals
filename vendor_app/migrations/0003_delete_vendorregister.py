# Generated by Django 4.2.5 on 2024-08-29 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_app', '0002_vendorregister_booking_reference'),
    ]

    operations = [
        migrations.DeleteModel(
            name='VendorRegister',
        ),
    ]