# Generated by Django 4.0.4 on 2022-05-02 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floraison', '0018_remove_order_delivery_alter_order_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='due_date',
            field=models.DateTimeField(null=True),
        ),
    ]