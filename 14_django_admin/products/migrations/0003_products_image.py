# Generated by Django 4.2.7 on 2023-11-20 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_products_options_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, default='defaults/aa.png', null=True, upload_to='products'),
        ),
    ]
