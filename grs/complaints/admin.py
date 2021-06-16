from django.contrib import admin

# Register your models here.
from .models import Complaint


class ComplaitAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'complaint_to', 'complaint_for', 'user_role')

admin.site.register(Complaint, ComplaitAdmin) 