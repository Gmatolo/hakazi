from django.shortcuts import redirect, render

from .forms import EmailForm


def get_user_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            request.session['email'] = email
            return redirect('home')
    else:
        form = EmailForm()
    return render(request, 'get_user_emailform.html', {'form': form})