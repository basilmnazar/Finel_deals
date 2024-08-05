# Generated by Django 4.2.5 on 2024-08-05 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deal_app', '0009_remove_outletfields_outlet_outletfields_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='outlet',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='deal_app.dealer'),
        ),
        migrations.AlterField(
            model_name='outletfields',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='deal_app.dealer'),
        ),
        migrations.AlterField(
            model_name='registerdealer',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='deal_app.dealer'),
        ),
    ]