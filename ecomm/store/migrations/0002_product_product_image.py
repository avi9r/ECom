# Generated by Django 3.1.4 on 2020-12-30 07:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField( upload_to=''),
            preserve_default=False,
        ),
    ]