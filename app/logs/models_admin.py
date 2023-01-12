from django.contrib import admin

class LogsAdmin(admin.ModelAdmin):
    list_display = ('type', 'msg', 'created_at')