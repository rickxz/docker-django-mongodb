from django.contrib import admin

from logs.models import Log
from logs.models_admin import LogsAdmin
# Register your models here.
admin.site.register(Log, LogsAdmin)
