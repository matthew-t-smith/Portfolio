# Generated by Django 2.0.3 on 2018-05-07 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_auto_20180429_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='category',
            field=models.CharField(default='web', max_length=20),
            preserve_default=False,
        ),
    ]
