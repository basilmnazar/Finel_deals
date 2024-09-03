# Generated by Django 4.2.5 on 2024-09-01 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dealers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchant_name', models.CharField(max_length=255)),
                ('business_owner_name', models.CharField(default='', max_length=255)),
                ('merchant_type', models.CharField(choices=[('hotel', 'Hotel'), ('restuarent', 'Restuarent'), ('spa', 'Spa'), ('saloon', 'Saloon')], max_length=30, null=True)),
                ('merchant_address', models.CharField(max_length=255, null=True)),
                ('city', models.CharField(max_length=40, null=True)),
                ('phone', models.BigIntegerField(null=True)),
                ('contact_person', models.IntegerField(blank=True, null=True)),
                ('outlet_name', models.CharField(blank=True, max_length=255, null=True)),
                ('outlet_description', models.TextField(blank=True, null=True)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('outlet_img', models.ImageField(blank=True, upload_to='images/')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voucher_name', models.CharField(blank=True, max_length=255, null=True)),
                ('voucher_price', models.IntegerField(default=0)),
                ('voucher_about', models.TextField(blank=True, default='')),
                ('voucher_description', models.TextField(blank=True, default='')),
                ('button_link', models.URLField(blank=True, null=True)),
                ('voucher_date', models.DateField(blank=True, null=True)),
                ('dealer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='deal_app.dealers')),
            ],
        ),
        migrations.CreateModel(
            name='VoucherCoupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon_name', models.CharField(default='', max_length=255, null=True)),
                ('coupon_description', models.TextField(blank=True, default='', null=True)),
                ('coupon_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('coupon_button_link', models.URLField(blank=True, null=True)),
                ('voucher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coupons', to='deal_app.voucher')),
            ],
        ),
    ]
