from django.urls import path

from . import views

app_name = 'complaints'


urlpatterns = [
    path('add_complaint', views.add_complaint, name="add_complaint")
]
