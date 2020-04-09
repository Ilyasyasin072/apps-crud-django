from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


def registration(request):
    # post
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created! you have login!{username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})


# required login for profile
@login_required
def profile(request):
    user_form = UserUpdateForm()
    profile_form = ProfileUpdateForm()

    context = {
        'user_form': user_form,
        'profile_form' : profile_form
    }

    if user_form.is_valid():
        user_form.save()
        username = user_form.cleaned_data.get('username')
        messages.success(request, f'Account has been created! you have login!{username}')
    if profile_form.is_valid():
        profile_form.save()
        username = profile_form.cleaned_data.get('username')
        messages.success(request, f'Account has been created! you have login!{username}')

        return redirect('profile')
    return render(request, 'users/profile.html', context)




