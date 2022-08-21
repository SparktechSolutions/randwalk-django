# Generated by Django 3.2.9 on 2022-07-30 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('randwalk_website', '0012_auto_20220721_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField(max_length=250)),
                ('image', models.ImageField(upload_to='')),
                ('link', models.CharField(max_length=250)),
            ],
        ),
    ]