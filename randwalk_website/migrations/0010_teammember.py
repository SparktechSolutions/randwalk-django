# Generated by Django 3.2.9 on 2022-07-21 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('randwalk_website', '0009_alter_projectimage_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('designation', models.TextField(max_length=60)),
                ('linkedin_profile_link', models.TextField(null=True)),
                ('facebook_profile_link', models.TextField(null=True)),
                ('instagram_profile_link', models.TextField(null=True)),
                ('twitter_profile_link', models.TextField(null=True)),
                ('profile_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
