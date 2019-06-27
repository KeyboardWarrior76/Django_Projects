from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register("hello", views.HelloViewSet, base_name="hello-viewset")
router.register("profiles", views.UserProfileViewSet)

urlpatterns = [
    path("hello/", views.HelloApiView.as_view()),
    path("", include(router.urls)),
]