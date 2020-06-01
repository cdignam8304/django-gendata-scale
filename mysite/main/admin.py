from django.contrib import admin
from .models import Generic, Schema, Report

# Register your models here.

admin.site.register(Generic)
admin.site.register(Schema)
admin.site.register(Report)
