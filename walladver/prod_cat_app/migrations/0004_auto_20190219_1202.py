# Generated by Django 2.0 on 2019-02-19 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prod_cat_app', '0003_auto_20190219_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, upload_to='%Y/%m/%d'),
        ),
    ]
