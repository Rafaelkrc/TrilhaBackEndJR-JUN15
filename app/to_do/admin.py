from django.contrib import admin
from app.to_do.models import ToDo


@admin.register(ToDo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'do_in', 'is_finished')
