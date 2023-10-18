from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class CustomizedUserCreationForm(UserCreationForm):
  first_name = forms.CharField(label="First Name", required=True)
  last_name = forms.CharField(label="Last Name", required=True)
  email = forms.EmailField(label="Email", required=True)
  class Meta:
    model = User
    fields = ("first_name", "last_name","email", "username", "password1", "password2")

  def validate_username(value):
 	  if len(value) < 4:
	    raise ValidationError("Username Must Be At Least 5 Characters Long.") 

  password1 = forms.CharField(label="Password",widget=forms.PasswordInput(),help_text="") 



  password2 = forms.CharField(
	 label="Password Confirmation",
	 widget=forms.PasswordInput(),
	 help_text=""
	)
  username = forms.CharField(help_text="")
  
  def clean_username(self):
   username = self.cleaned_data['username']
   if self.instance.username == username:
       return username

   if User.objects.filter(username=username).exists():
	    raise forms.ValidationError("Username Already Exists.")

   return username 