from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import EmailForm, ResumeForm


def get_user_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            request.session['email'] = email
            return redirect('upload-resume')
    else:
        form = EmailForm()
    return render(request, 'homepage/get_user_emailform.html', {'form': form})



def upload_resume(request):
    email = request.session.get('email')
    if email:
        if request.method == 'POST':
            form = ResumeForm(request.POST, request.FILES)
            if form.is_valid():
                resume = form.save(commit=False)
                resume.email = email
                resume.save()
                del request.session['email']
                messages.success(request, "We'll analyze and send the resume report there.")
                return redirect('home')
        else:
            form = ResumeForm()
        return render(request, 'resume/upload_resume.html', {'form': form})
    else:
        return redirect('home')