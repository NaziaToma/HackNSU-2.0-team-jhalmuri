# Generated by Django 2.2 on 2020-09-20 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procurebd_api', '0002_item_item_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_quantity',
            field=models.IntegerField(default=0),
        ),
    ]