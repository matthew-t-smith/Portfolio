# Generated by Django 2.0.3 on 2018-04-29 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20180428_0521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(upload_to='static/img'),
        ),
    ]
