# Generated by Django 4.2.6 on 2023-11-10 20:51

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('GICA', '0002_donorniya_donor_country_donor_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='Phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='donorniya',
            name='Phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='member',
            name='Phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]