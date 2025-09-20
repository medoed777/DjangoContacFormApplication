from django.contrib import admin
from blogs.models import Blogs


@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ("id", "head", "content", "is_active", "views")
    list_filter = ("id",)
