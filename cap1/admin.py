from django.contrib import admin
from .models import User, Tag, Location, Post, Category


class AdminSite(admin.AdminSite):
    site_header = "TRAVEL ADVISOR"

# Register your models here.


admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Location)
admin.site.register(Post)
admin.site.register(Category)
