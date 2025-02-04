from rest_framework.routers import DefaultRouter
from stage0_API.user_api.views import get_user_details

from django.urls import path, include

# router = DefaultRouter()
# router.register(r"user_details", User_detailsVi, basename= "user_details")

urlpatterns = [
    path("", get_user_details)
    # path("", include(router.urls)),
] 
