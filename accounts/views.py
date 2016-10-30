from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from .forms import UserProfileForm, ExtendedUserCreationForm
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied
from django.contrib.auth import authenticate, login
# using snippets from https://blog.khophi.co/extending-django-user-model-userprofile-like-a-pro/

@login_required
def edit_user(request, pk):
    user = User.objects.get(pk=pk)
    user_form = UserProfileForm(instance=user)
 
    ProfileInlineFormset = inlineformset_factory(User, UserProfile, fields=( 'bio', 'phone', 'city', 'country',))
    formset = ProfileInlineFormset(instance=user)
 
    if request.user.is_authenticated() and request.user.id == user.id:
        if request.method == "POST":
            user_form = UserProfileForm(request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)
 
            if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)
 
                if formset.is_valid():
                    created_user.save()
                    formset.save()
                    return HttpResponseRedirect('/')
 
        return render(request, "registration/profile_update.html", {
            "noodle": pk,
            "noodle_form": user_form,
            "formset": formset,
        })
    else:
        raise PermissionDenied


def logged_out(request):
    return render(request, "logged_out.html")

def signup(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user  = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request,new_user)
            return HttpResponseRedirect("/")
    else:
        form = ExtendedUserCreationForm()
    return render(request, "signup.html", {
        'form': form,
    })