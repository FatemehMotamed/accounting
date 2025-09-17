from django.contrib import admin
from jalali_date import datetime2jalali
from jalali_date.admin import ModelAdminJalaliMixin

from .models import *

admin.site.register(Class)
admin.site.register(ClassTime)
admin.site.register(Student)


@admin.register(Session)
class SessionAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ("class_time", "get_jalali_created")

    def get_jalali_created(self, obj):
        return datetime2jalali(obj.created_at).strftime("%Y/%m/%d _ %H:%M")

    get_jalali_created.short_description = "تاریخ ایجاد"
