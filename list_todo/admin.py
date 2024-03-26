from django.contrib import admin

from .models import Category, ListToDo


@admin.register(ListToDo)
class ListToDoAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'add_date',
        'author',
        'category',
        'is_ready',
    )
    list_display_links = (
        'name',
        'category',
    )
    list_filter = (
        'category',
        'author',
        'is_ready',
    )
    list_editable = (
        'description',
        'author',
        'is_ready',
    )
    search_fields = (
        'name',
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'slug',
    )
    list_editable = (
        'description',
        'slug'
    )
    search_fields = (
        'name',
    )
