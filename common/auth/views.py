from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.http import HttpResponseRedirect
# from django_registration.backends.one_step.views import RegistrationView
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from rest_framework import generics

from . import forms as f
from .models import CustomUser
from .serializers import UserSerializer

# from django.contrib.auth.views import LoginView, LogoutView

# from django.http import JsonResponse
# from django.views.decorators.http import require_POST

# from .models import Contact, Profile

# from django.views.generic import ListView
# from django.views.generic.edit import FormView

User = get_user_model()


class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class SignUp(View):

    def get(self, request):
        form = f.SignUp()
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request):
        form = f.SignUp(request.POST)
        if form.is_valid():
            user = form.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return redirect('/')
        return render(request, 'registration/signup.html', {'form': form})


class Login(LoginView):
    form_class = f.Login
    next_page = '/'


class Logout(LogoutView):
    next_page = '/'


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = f.UserEditForm(instance=request.user, data=request.POST)
        # profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid():
            user_form.save()
            # profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = f.UserEditForm(instance=request.user)
        # profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'account/edit.html', {'user_form': user_form})


def register(request):
    if request.method == 'POST':
        user_form = f.UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            # Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = f.UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


@login_required
def user_list(request):
    users = User.objects.filter(is_active=True)
    return render(request, 'account/user/list.html', {'section': 'people', 'users': users})


@login_required
def user_detail(request, username):
    user = get_object_or_404(User, username=username, is_active=True)
    return render(request, 'account/user/detail.html', {'section': 'people', 'user': user})
