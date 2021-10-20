from django.contrib import admin

# Register your models here.
from .models import CollegeDate

@admin.register(CollegeDate)
class CollegeDateAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','username','mobile','email','college','city','fees','addmision_numbers']
    list_editable = ['username','mobile','email','college','city']
    search_fields = ['email']