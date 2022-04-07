from django.views.generic import TemplateView
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

#https://ordinarycoders.com/blog/article/django-user-register-login-logout
# Create your views here.
""" from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile
from feed.models import Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.conf import settings
from django.http import HttpResponseRedirect
from .models import Profile, FriendRequest
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
import random
User = get_user_model()
 """
class LandingPageView(TemplateView):
    template_name = 'home.html' 

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

# #view list of friends
# def friend_list(request):
#     friend = request.user.profile
#     friends = friend.friends.all()
#     context={
#     'friends': friends
#     }
#     return render(request, "users/friendlist.html", context)

# #send friend request
# #send a request, take the ID of the user to send a friend request 
# @login_required
# def send_friend_request(request, id):
#     user = get_object_or_404(User, id=id)
#     frequest, created = FriendRequest.objects.get_or_create(
#             from_user=request.user,
#             to_user=user)
#     return HttpResponseRedirect('/users/{}'.format(user.profile.slug))


# #accept friend request
# @login_required
# def accept_friend_request(request, id):
#     from_user = get_object_or_404(User, id=id)
#     frequest = FriendRequest.objects.filter(from_user=from_user, to_user=request.user).first()
#     user1 = frequest.to_user
#     user2 = from_user
#     user1.profile.friends.add(user2.profile)
#     user2.profile.friends.add(user1.profile)
#     if(FriendRequest.objects.filter(from_user=request.user, to_user=from_user).first()):
#         request_rev = FriendRequest.objects.filter(from_user=request.user, to_user=from_user).first()
#         request_rev.delete()
#     frequest.delete()
#     return HttpResponseRedirect('/users/{}'.format(request.user.profile.slug))

# #delete friend request
# @login_required
# def delete_friend_request(request, id):
#     from_user = get_object_or_404(User, id=id)
#     frequest = FriendRequest.objects.filter(from_user=from_user, to_user=request.user).first()
#     frequest.delete()
#     return HttpResponseRedirect('/users/{}'.format(request.user.profile.slug))
