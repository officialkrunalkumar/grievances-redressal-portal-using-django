from django.urls import path

from . import views

app_name = 'complaints'


urlpatterns = [
    path('add_complaint', views.add_complaint, name="add_complaint"),
    path('delete_complaint/<int:id>', views.delete_complaint, name="delete_complaint"),
    path('update_complaint/<int:id>', views.update_complaint, name="update_complaint"),
]
