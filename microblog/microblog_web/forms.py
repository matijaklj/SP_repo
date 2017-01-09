from django import forms

class LoginForm(forms.Form):
  username = forms.CharField(label='Username:', max_length=100)
  password = forms.CharField(max_length=100, widget=forms.PasswordInput)

class RegisterForm(forms.Form):
  username = forms.CharField(label='Username:', max_length=100)
  displayName = forms.CharField(label="Display name:", max_length=30, required=False)
  email = forms.CharField(label='email:', max_length=100)
  password1 = forms.CharField(max_length=100, widget=forms.PasswordInput)
  password2 = forms.CharField(max_length=100, widget=forms.PasswordInput)

class NewPostForm(forms.Form):
  content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
  # TODO location, image, links...
