# Generated by Django 3.2.9 on 2023-02-19 06:53

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('randwalk_website', '0016_publication_detailed_information'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='detailed_information',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
    ]