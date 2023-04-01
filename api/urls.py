from django.urls import path, include
from rest_framework import routers
from .views import ResumeViewSet

router = routers.DefaultRouter()
router.register('resume', ResumeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]