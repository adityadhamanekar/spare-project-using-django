from django.contrib import admin
from .models import Employee, Supplier

# Register your models here.

class SupplierAdmin(admin.ModelAdmin):
    list_display = ['supplierName', 'province', 'city', 'phone_number']
    search_fields = ['supplierName', 'province', 'city', 'phone_number']

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'gender', 'phone_number', 'email', 'role']
    search_fields = ['firstname', 'lastname', 'gender', 'phone_number', 'email', 'role']


admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Supplier, SupplierAdmin)