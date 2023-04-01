from rest_framework import viewsets
from rest_framework.response import Response
from  resume.models import Resume
from .serializers import ResumeSerializer


class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        if email:
            request.session['email'] = email
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        email = self.request.session.get('email')
        if email:
            serializer.save(email=email)
            del self.request.session['email']

    def list(self, request, *args, **kwargs):
        queryset = self.queryset.filter(email=request.session.get('email'))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)