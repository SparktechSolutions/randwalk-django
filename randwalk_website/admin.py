from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header = "Randwalk Research Admin Panel"
admin.site.register(Service)
admin.site.register(Slider)
admin.site.register(Testimonial)


class ProjectImageAdmin(admin.StackedInline):
    model = ProjectImage


@admin.register(Project)
class PostAdmin(admin.ModelAdmin):
    inlines = [ProjectImageAdmin]

    class Meta:
        model = Project


@admin.register(ProjectImage)
class PostImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(TeamMember)
admin.site.register(Publication)
admin.site.register(Conference)
