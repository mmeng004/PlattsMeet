from django.views.generic import TemplateView
# Create your views here.


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
