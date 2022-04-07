from django.urls import path,include
from .views import LandingPageView,AboutPageView,HelpPageView,PortalPageView,RegistrationPageView
<<<<<<< Updated upstream
<<<<<<< HEAD
from . import views
=======
from django.conf.urls import url
from . import views

>>>>>>> cfce81419ccaaac94b211d8a94e4f49355188135
=======
from . import views
>>>>>>> Stashed changes
urlpatterns = [
   path('', LandingPageView.as_view(),name = 'home'),
   path('about/', AboutPageView.as_view(),name = 'about'),
   path('help/', HelpPageView.as_view(),name = 'help'),
   path('portalpage/', PortalPageView.as_view(),name = 'portalpage'),
<<<<<<< Updated upstream
<<<<<<< HEAD
=======
>>>>>>> Stashed changes
   path("register/", views.register_request, name="register"),
   path('registeration/', RegistrationPageView.as_view(),name = 'registeration'),
=======
   path('register/', RegistrationPageView.as_view(),name = 'register'),


>>>>>>> cfce81419ccaaac94b211d8a94e4f49355188135
]
