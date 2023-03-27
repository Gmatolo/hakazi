from django.db import models


class Resume(models.Model):
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/%Y/%m/%d')

    def __str__(self):
        return f'Resume for {self.email}'