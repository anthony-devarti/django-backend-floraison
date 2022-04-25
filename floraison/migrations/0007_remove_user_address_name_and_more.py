# Generated by Django 4.0.4 on 2022-04-21 16:53

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('floraison', '0006_user_address_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_address',
            name='name',
        ),
        migrations.AlterField(
            model_name='user_address',
            name='contact_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]