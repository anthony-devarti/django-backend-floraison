# Generated by Django 4.0.4 on 2022-04-26 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('floraison', '0011_item_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='image',
        ),
    ]