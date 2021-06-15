from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from .forms import ProfileForm
from .models import UserProfile
# Create your views here.


''' def store_file(file):
    with open("temp/image.jpg", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk) '''


class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"


class UserProfileView(ListView):
    template_name = "profiles/user_profile.html"
    model = UserProfile
    context_object_name = "profiles"
