# Generated by Django 3.2.3 on 2021-05-26 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkoutline',
            name='variant_price',
        ),
    ]