from django.shortcuts import render, redirect
from django.contrib import messages
<<<<<<< HEAD
from django.contrib.auth.decorators import login_required
=======
>>>>>>> b49511d9d398057b965a781d337063c95f7ca0f5
from .forms import UserRegisterForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
<<<<<<< HEAD
            messages.success(
                request, f"Your account has been created! You can now login"
            )
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request):
    return render(request, "users/profile.html")
=======
            messages.success(request, f"Account created for {username}!")
            return redirect("blog-home")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})
>>>>>>> b49511d9d398057b965a781d337063c95f7ca0f5
