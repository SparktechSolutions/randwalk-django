# Generated by Django 3.2.9 on 2022-06-17 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('randwalk_website', '0002_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='position',
            field=models.IntegerField(null=True),
        ),
    ]
