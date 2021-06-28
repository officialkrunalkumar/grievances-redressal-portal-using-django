from django.contrib import admin

# Register your models here.
from .models import Complaint, Feedback


class ComplaitAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'complaint_to',
                    'complaint_for', 'user_role', 'user')


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'rating', 'description')


admin.site.register(Complaint, ComplaitAdmin)
admin.site.register(Feedback, FeedbackAdmin)
