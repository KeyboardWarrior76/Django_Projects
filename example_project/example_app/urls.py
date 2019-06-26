from django.urls import path
from example_app import views

urlpatterns = [
    path("", views.ExampleView.as_view())
]