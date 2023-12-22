from django.contrib import admin
from .models import Department, Course, Purpose, Material, Order

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'department']

@admin.register(Purpose)
class PurposeAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'dob', 'age', 'gender', 'phone_number', 'mail_id', 'address', 'department', 'course', 'purpose']
    filter_horizontal = ['materials_provide']
