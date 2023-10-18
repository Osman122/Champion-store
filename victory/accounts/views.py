from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.models import  User
from accounts.forms import  CustomizedUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView,DeleteView
from django.views.generic import DetailView


class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'accounts/profile.html'
    context_object_name = 'user_profile'

    def get_object(self, queryset=None):
        return self.request.user

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'accounts/profile_edit.html'
    form_class = CustomizedUserCreationForm
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user

class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'accounts/profile_delete.html'
    success_url = reverse_lazy('logout')

    def get_object(self, queryset=None):
        return self.request.user


class CreateCustomUser(CreateView):
    model = User
    template_name = 'accounts/registration.html'
    form_class = CustomizedUserCreationForm
    
    success_url = reverse_lazy("login")