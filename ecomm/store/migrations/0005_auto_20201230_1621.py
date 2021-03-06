# Generated by Django 3.1.4 on 2020-12-30 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20201230_1318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='customer_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='customer_fname',
            new_name='fname',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='customer_lname',
            new_name='lname',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='customer_mobile',
            new_name='mobile',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='customer_password',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_disp',
            new_name='disp',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
