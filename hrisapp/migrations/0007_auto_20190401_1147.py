# Generated by Django 2.1.7 on 2019-04-01 11:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hrisapp', '0006_auto_20190329_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='bankAccountName',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='internaldeduction',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='salaryaddition',
            name='date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
    ]
