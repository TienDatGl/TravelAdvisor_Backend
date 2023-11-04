from django.contrib import admin
from .models import User, Tag, Location, Post, Category, Trip, TripItem



class AdminSite(admin.AdminSite):
    site_header = "TRAVEL ADVISOR"

# Register your models here.

class TripItemInline(admin.StackedInline):
    model=TripItem
    extra=1

class TripAdmin(admin.ModelAdmin):
    inlines = [TripItemInline]


admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Location)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Trip, TripAdmin)
admin.site.register(TripItem)
