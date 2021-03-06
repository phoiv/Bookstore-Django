# Generated by Django 3.1.7 on 2021-03-18 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0006_auto_20210317_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='items_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cart',
            name='price_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]
