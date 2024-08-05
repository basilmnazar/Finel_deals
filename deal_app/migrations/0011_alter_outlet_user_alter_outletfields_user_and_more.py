# Generated by Django 4.2.5 on 2024-08-05 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_app', '0001_initial'),
        ('deal_app', '0010_dealer_alter_outlet_user_alter_outletfields_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outlet',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts_app.dealer'),
        ),
        migrations.AlterField(
            model_name='outletfields',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts_app.dealer'),
        ),
        migrations.AlterField(
            model_name='registerdealer',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts_app.dealer'),
        ),
        migrations.DeleteModel(
            name='Dealer',
        ),
    ]