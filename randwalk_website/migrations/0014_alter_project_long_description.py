# Generated by Django 3.2.9 on 2022-09-04 05:52

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('randwalk_website', '0013_publication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='long_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
