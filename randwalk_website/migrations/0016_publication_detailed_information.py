# Generated by Django 3.2.9 on 2023-02-19 06:14

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('randwalk_website', '0015_publication_publication_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='detailed_information',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=None, null=True),
        ),
    ]