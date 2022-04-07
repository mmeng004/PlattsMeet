from django.urls import path,include
from .views import LandingPageView,AboutPageView,HelpPageView,PortalPageView,RegistrationPageView
from django.conf.urls import url
from . import views

urlpatterns = [
   path('', LandingPageView.as_view(),name = 'home'),
   path('about/', AboutPageView.as_view(),name = 'about'),
   path('help/', HelpPageView.as_view(),name = 'help'),
   path('portalpage/', PortalPageView.as_view(),name = 'portalpage'),
   path('register/', RegistrationPageView.as_view(),name = 'register'),


]
