# Generated by Django 2.0.5 on 2019-03-13 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrisapp', '0013_remove_account_basicpay'),
    ]

    operations = [
        migrations.AddField(
            model_name='internaldeduction',
            name='numberOfInstallments',
            field=models.IntegerField(default=1),
        ),
    ]
