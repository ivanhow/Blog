from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

from app.models import UserProfile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'My email'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'My first name'}))
    last_name = forms.CharField(max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'My last name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class CreateProfilePageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('biography', 'profile_image', 'website_url')  # Hide user choice

        widgets = {
            'biography': forms.Textarea(attrs={'class': 'form-control'}),
            'website_url': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EditProfilePageForm(UserChangeForm):
    biography = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    profile_image = forms.ImageField()
    website_url = forms.CharField(max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = UserProfile
        fields = ('biography', 'profile_image', 'website_url')