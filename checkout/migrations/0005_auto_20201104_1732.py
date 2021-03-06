# Generated by Django 3.1.1 on 2020-11-04 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_remove_order_non_delivery'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_registered',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='orderlineitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
