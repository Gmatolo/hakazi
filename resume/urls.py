from django.urls import path

from .views import *

urlpatterns = [
    path('', get_user_email, name='get-user-email'),
    path('upload/', upload_resume, name='upload-resume'),

]