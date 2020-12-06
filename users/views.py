from django.contrib.auth.views import PasswordChangeView
from django.db import models
from django.shortcuts import get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.views.generic import DetailView

from app.models import UserProfile
from users.forms import SignUpForm, EditProfileForm


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user


class ProfilePageView(DetailView):
    model = UserProfile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = UserProfile.objects.all()
        context = super(ProfilePageView, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(UserProfile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context


class EditProfilePageView(generic.UpdateView):
    model = UserProfile
    template_name = 'registration/edit_profile_page.html'
    fields = ['biography', 'profile_image', 'website_url']
    success_url = reverse_lazy('home')
