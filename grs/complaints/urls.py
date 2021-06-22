from django.urls import path

from . import views

app_name = 'complaints'


urlpatterns = [
    path('add_complaint', views.add_complaint, name="add_complaint"),
    path('my_complaint', views.my_complaints, name="my_complaints"),
    path('delete_complaint/<int:id>', views.delete_complaint,
         name="delete_complaint"),
    path('update_complaint/<int:id>', views.update_complaint,
         name="update_complaint"),
    path('add_feedback/<int:id>', views.add_feedback, name="add_feedback"),
]
