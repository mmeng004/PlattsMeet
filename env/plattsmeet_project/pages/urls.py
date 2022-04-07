from django.urls import path,include
from .views import LandingPageView,AboutPageView,HelpPageView,PortalPageView,RegistrationPageView
<<<<<<< HEAD
from . import views
=======
<<<<<<< HEAD
from . import views
=======
from django.conf.urls import url
from . import views

>>>>>>> cfce81419ccaaac94b211d8a94e4f49355188135
>>>>>>> parent of 34061f5 (Merge)
urlpatterns = [
   path('', LandingPageView.as_view(),name = 'home'),
   path('about/', AboutPageView.as_view(),name = 'about'),
   path('help/', HelpPageView.as_view(),name = 'help'),
   path('portalpage/', PortalPageView.as_view(),name = 'portalpage'),
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> parent of 34061f5 (Merge)
   path("register/", views.register_request, name="register"),
   path('registeration/', RegistrationPageView.as_view(),name = 'registeration'),
]
