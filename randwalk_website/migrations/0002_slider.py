# Generated by Django 3.2.9 on 2022-06-17 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('randwalk_website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
