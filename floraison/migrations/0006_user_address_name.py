# Generated by Django 4.0.4 on 2022-04-21 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floraison', '0005_alter_category_options_alter_user_address_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_address',
            name='name',
            field=models.CharField(default='My Address', max_length=50),
            preserve_default=False,
        ),
    ]