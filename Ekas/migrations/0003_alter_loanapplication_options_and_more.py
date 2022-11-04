# Generated by Django 4.0.6 on 2022-07-07 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ekas', '0002_loanapplication_date_time_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='loanapplication',
            options={'verbose_name': 'Loan Application', 'verbose_name_plural': 'Loan Applications'},
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='alt_phone_number',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Alternative Phone Number'),
        ),
    ]