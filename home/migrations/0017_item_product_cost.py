# Generated by Django 3.0.7 on 2021-04-17 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20210414_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='product_cost',
            field=models.IntegerField(default=0),
        ),
    ]
