from django.contrib import admin

from .models import (
    Resource,
    Category,
    Company,
    UserCompany,
    Project,
    Announcement,
    AnnouncementProject,
    Requirement,
    ResourcesBag,
)

admin.site.register(Resource)
admin.site.register(Category)
admin.site.register(Company)
admin.site.register(UserCompany)
admin.site.register(Project)
admin.site.register(AnnouncementProject)
admin.site.register(Announcement)
admin.site.register(Requirement)
admin.site.register(ResourcesBag)
