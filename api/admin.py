from django.contrib import admin
from .models import Category, MenuItem, Table, Order, OrderItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'price', 'available']
    list_filter = ['category', 'available']
    search_fields = ['name', 'description']


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'status']
    list_filter = ['status']
    search_fields = ['number']  # ✅ Add this line

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'table', 'created_by', 'created_at', 'status']
    list_filter = ['status', 'created_at']
    inlines = [OrderItemInline]
    date_hierarchy = 'created_at'
    autocomplete_fields = ['table', 'created_by']

