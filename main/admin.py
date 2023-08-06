from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group

# Register your models here.
admin.site.unregister(Group)
admin.site.register(About_me)
admin.site.register(Expericence)
admin.site.register(Portfolio)
admin.site.register(Service)
admin.site.register(Contact)
admin.site.register(Skill)
admin.site.register(Testimonial)