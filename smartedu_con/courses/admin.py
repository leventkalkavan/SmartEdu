from django.contrib import admin
from . models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name","avaible")
    list_filter = ("avaible",)
    search_fields = ("name", "description")