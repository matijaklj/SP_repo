from django import forms
from microblog_web.models import Profile
from django.forms import ModelForm

class LoginForm(forms.Form):
  username = forms.CharField(label='Username:', max_length=100)
  password = forms.CharField(max_length=100, widget=forms.PasswordInput)

class RegisterForm(forms.Form):
  username = forms.CharField(label='Username:', max_length=100)
  displayName = forms.CharField(label="Display name:", min_length=5, max_length=30, required=False)
  email = forms.CharField(label='email:', max_length=100)
  password1 = forms.CharField(max_length=100, widget=forms.PasswordInput)
  password2 = forms.CharField(max_length=100, widget=forms.PasswordInput)

class NewPostForm(forms.Form):
    content = forms.CharField(required=True,widget=forms.Textarea)
    location_lat = forms.CharField(required=False)
    location_lon = forms.CharField(required=False)

class SearchForm(forms.Form):
    search_str = forms.CharField(required=True, max_length=100)

"""
class EditProfileForm(forms.Form):
    displayName = forms.CharField(label="Display name:", min_length=5, max_length=30, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label="Describtion:", max_length=150, required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}))
    profile_img = forms.FileField(label="Profile image:", required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    cover_img = forms.FileField(label="Cover image:", required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
"""
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['displayName', 'description', 'coverImage', 'profileImage']
        widgets = {
            'displayName': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'coverImage': forms.FileInput(attrs={'class': 'form-control'}),
            'profileImage': forms.FileInput(attrs={'class': 'form-control'})
        }
