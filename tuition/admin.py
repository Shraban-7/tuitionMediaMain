from django.contrib import admin
from .models import TuitionPost, District, Area, Style, Medium, PerDay, Gender


# Register your models here.
@admin.register(TuitionPost)
class TuitionPostAdmin(admin.ModelAdmin):
    list_display = (
        'fullname', 'district', 'area', 'salary', 'address', 'created_at', 'school_college', 'mobile', 'email',
        'subjects')


admin.site.register(Gender)
admin.site.register(PerDay)
admin.site.register(Medium)
admin.site.register(Style)
admin.site.register(Area)
admin.site.register(District)
