# Generated by Django 3.2.7 on 2021-11-18 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20211115_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.ImageField(default='default.jpg', null=True, upload_to='profile_pics'),
        ),
    ]
