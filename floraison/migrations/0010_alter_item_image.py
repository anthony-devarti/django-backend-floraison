# Generated by Django 4.0.4 on 2022-04-25 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floraison', '0009_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.FileField(default='None', upload_to='./images/'),
        ),
    ]
