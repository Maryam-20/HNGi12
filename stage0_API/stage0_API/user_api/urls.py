from rest_framework.routers import DefaultRouter
from .views import User_detailsView

from django.urls import path, include

router = DefaultRouter()
router.register(r"user_details", User_detailsView, basename= "user_details")

urlpatterns = [
    # path("", include(router.urls)),
] + router.urls
