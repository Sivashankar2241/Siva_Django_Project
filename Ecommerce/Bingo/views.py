from django.shortcuts import render
from django.http import HttpResponse

from .utils import upload_file
from .forms import signupForm

# Create your views here.


def ecomp(request):
    if request.method == 'POST':
        signup = signupForm(request.POST, request.FILES)
        if signup.is_valid():
            upload_file(request.FILES['profile_image'])
            return render(request, "login.html")
        else:
            return render(request, 'signup.html', {'form': signup})
    else:
        signup = signupForm()

    return render(request, "signup.html", {"form": signup})