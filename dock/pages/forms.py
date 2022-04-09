from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#from .models import Profile

class NewUserForm(UserCreationForm):
    #add fields/attributes related to the user
	username = forms.CharField(required=True)
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	email = forms.EmailField(required=True)
	class Meta:
		model = User
		fields = ("username", "first_name","last_name","email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user