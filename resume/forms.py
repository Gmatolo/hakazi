from django import forms

from .models import Resume


class EmailForm(forms.Form):
    email = forms.EmailField()

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('resume',)


    def clean_resume(self):
        resume = self.cleaned_data['resume']
        if resume:
            if resume.size > 5 * 1024 * 1024:  # 5MB limit
                raise forms.ValidationError("File size should not exceed 5 MB.")
            return resume
        else:
            raise forms.ValidationError("Please upload a resume file.")