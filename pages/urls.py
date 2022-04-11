from django.urls import path,include
from .views import LandingPageView,ClubsPageView,AboutPageView,HelpPageView,PortalPageView,RegistrationPageView
from . import views

urlpatterns = [
   path('', LandingPageView.as_view(),name = 'home'),
   path('about/', AboutPageView.as_view(),name = 'about'),
   path('help/', HelpPageView.as_view(),name = 'help'),
   path('portalpage/', PortalPageView.as_view(),name = 'portalpage'),
   path("register/", views.register_request, name="register"),
   #path('registeration/', RegistrationPageView.as_view(),name = 'registeration'),
   path('clubs/', ClubsPageView.as_view(),name = 'clubs'),
]