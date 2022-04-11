from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import TemplateView

from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
# Create your views here.
""" from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile
#from feed.models import Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.conf import settings
from django.http import HttpResponseRedirect
from .models import Profile, FriendRequest


from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
import random
User = get_user_model() """

class LandingPageView(TemplateView):
    template_name = 'home.html' 

class ClubsPageView(TemplateView):
    template_name = 'clubs.html' 

class AboutPageView(TemplateView):
    template_name = 'about.html' 

class HelpPageView(TemplateView):
    template_name = 'help.html' 

class PortalPageView(TemplateView):
    template_name = 'portalpage.html' 
    
class RegistrationPageView(TemplateView):
    template_name = 'registeration.html' 
    
class ResetpasswordView(TemplateView):
    template_name = 'password_reset_form.html'

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful.")
			return redirect("/portalpage/")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="registration/register.html", context={"register_form":form})
  