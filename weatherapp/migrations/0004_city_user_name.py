# Generated by Django 2.0 on 2018-08-18 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0003_city_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='user_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
