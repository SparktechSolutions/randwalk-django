from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField, RichTextUploadingFormField


# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_image = models.CharField(max_length=50)


class Slider(models.Model):
    position = models.IntegerField(null=True)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    image = models.ImageField()


class Testimonial(models.Model):
    cus_name = models.CharField(max_length=50)
    cus_designation = models.CharField(max_length=50, null=True)
    message = models.TextField(max_length=200)
    cus_image = models.ImageField()
    rating = models.IntegerField()


class Project(models.Model):
    name = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100, null=True)
    short_description = models.TextField(max_length=500)
    long_description = RichTextUploadingField()
        # models.TextField(max_length=2000)
    product_image = models.ImageField()
    product_thumbnail = models.ImageField(null=True)
    product_icon = models.ImageField(null=True)

    def __str__(self):
        return self.name


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.project.name


class TeamMember(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=60)
    linkedin_profile_link = models.CharField(max_length=250, null=True, blank=True)
    facebook_profile_link = models.CharField(max_length=250, null=True, blank=True)
    instagram_profile_link = models.CharField(max_length=250, null=True, blank=True)
    twitter_profile_link = models.CharField(max_length=250, null=True, blank=True)
    profile_image = models.ImageField()


class Publication(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(max_length=250)
    image = models.ImageField()
    link = models.CharField(max_length=250)


