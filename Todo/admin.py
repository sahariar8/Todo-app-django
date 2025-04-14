from django.contrib import admin
from .models import Todo

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_completed', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('is_completed',)
    ordering = ('-created_at',)
    list_per_page = 10

admin.site.register(Todo, TodoAdmin)
