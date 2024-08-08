from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import UserEditForm

User = get_user_model()


@login_required
def edit(request):
    if request.method == 'POST':
        form = UserEditForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        form = UserEditForm(instance=request.user)
    return render(request, 'account/edit.html', {'form': form})
