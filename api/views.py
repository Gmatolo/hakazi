from django.contrib import messages
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from resume.forms import EmailForm, ResumeForm
from resume.models import Resume

from .serializers import ResumeSerializer


@api_view(['POST']) 
@permission_classes([AllowAny])
def get_user_email(request):
    form = EmailForm(request.data)
    if form.is_valid():
        email = form.cleaned_data['email']
        request.session['email'] = email
        return Response({'success': True})
    else:
        return Response({'success': False, 'errors': form.errors})
        

@api_view(['POST'])
@permission_classes([AllowAny])
def upload_resume(request):
    email = request.session.get('email')
    if email:
        form = ResumeForm(request.data, request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.email = email
            resume.save()
            del request.session['email']
            serializer = ResumeSerializer(resume)
            return Response({'success': True, 'resume': serializer.data})
        else:
            return Response({'success': False, 'errors': form.errors})
    else:
        return Response({'success': False, 'errors': 'Email not found.'})

@api_view(['GET'])
@permission_classes([AllowAny])
def resume_upload_complete(request):
    return Response({'message': "Resume uploaded successfully."})