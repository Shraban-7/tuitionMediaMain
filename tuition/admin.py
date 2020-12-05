from django.contrib import admin
from .models import TuitionPost


# Register your models here.
@admin.register(TuitionPost)
class TuitionPostAdmin(admin.ModelAdmin):
    list_display = ('fullname','district','select_area','salary','address','created_at','school_college','mobile','email','subjects')
