from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Tag)
admin.site.register(UserProfile)


class CourseTagInline(admin.TabularInline):
    model = Course.tags.through


class CourseAdmin(admin.ModelAdmin):
    inlines = [CourseTagInline]


class SeriesTagInline(admin.TabularInline):
    model = Series.tags.through


class SeriesAdmin(admin.ModelAdmin):
    inlines = [SeriesTagInline]


admin.site.register(Course, CourseAdmin)
admin.site.register(Series, SeriesAdmin)
