from django.contrib import admin

# Register your models here.
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'position', 'salary')
    search_fields = ('name', 'email', 'position')
    # list_filter = ('position')
