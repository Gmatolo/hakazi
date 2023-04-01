from django.urls import path

from .views import get_user_email, resume_upload_complete, upload_resume

urlpatterns = [
    path('get_user_email/', get_user_email, name='get_user_email'),
    path('upload_resume/', upload_resume, name='upload_resume'),
    path('resume_upload_complete/', resume_upload_complete, name='resume_upload_complete'),
]