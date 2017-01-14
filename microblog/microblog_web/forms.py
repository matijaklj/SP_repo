from django import forms
from microblog_web.models import Profile
from django.forms import ModelForm

class LoginForm(forms.Form):
    """
    The login form

    class attributes:
        - username -- the user username
        - password -- the user password
    """
    username = forms.CharField(label='Username:',min_length=6, max_length=100)
    password = forms.CharField(min_length=6, max_length=100, widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    """
    The register form

    class attributes:
        - username -- the user username
        - displayName -- the user display name (not required, default is the username)
        - email -- the user email
        - password1 -- the first password input
        - password1 -- the second password input
    """
    username = forms.CharField(label='Username:',min_length=6,  max_length=100)
    displayName = forms.CharField(label="Display name:", min_length=5, max_length=30, required=False)
    email = forms.CharField(label='email:', max_length=100)
    password1 = forms.CharField(min_length=6, max_length=100, widget=forms.PasswordInput)
    password2 = forms.CharField(min_length=6, max_length=100, widget=forms.PasswordInput)

class NewPostForm(forms.Form):
    """
    The new post form

    class attributes:
        - content -- the content of the post, the text
        - location_lat -- latitude of the location (not required)
        - location_lon -- longitude of the location (not required)
    """
    content = forms.CharField(required=True,widget=forms.Textarea)
    location_lat = forms.CharField(required=False)
    location_lon = forms.CharField(required=False)

class SearchForm(forms.Form):
    """
    The search form

    class attributes:
        - search_str -- the search keyword
    """
    search_str = forms.CharField(required=True, max_length=100)

class DeletePost(forms.Form):
    """
    The delete post form

    class attributes:
        - post_id -- the id of the post to be deleted
    """
    post_id = forms.CharField(required=True)

class DeleteProfile(forms.Form):
    """
    The delete profile form

    class attributes:
        - profile_id -- the id of the profile to be deleted
    """
    profile_id = forms.CharField(required=True)

class ProfileForm(ModelForm):
    """
    The edit profile form

    this is a ModelForm, it has a Meta class,
    with additional data about the types of input
    and label strings.
    """
    class Meta:
        model = Profile
        fields = ['displayName', 'description', 'coverImage', 'profileImage']
        widgets = {
            'displayName': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'coverImage': forms.FileInput(attrs={'class': 'form-control'}),
            'profileImage': forms.FileInput(attrs={'class': 'form-control'})
        }
