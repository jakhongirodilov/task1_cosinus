from django.urls import reverse_lazy
from django.shortcuts import redirect,render
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .forms import UserCreationForm, UserChangeForm
from .models import User

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"

def logout_view(request):
    logout(request)
    return redirect('home')

def profile_view(request, id):
    user = User.objects.get(id=id)
    return render(request, 'profile.html', {'user': user})

@login_required()
def update_profile(request):
    user = request.user

    if request.method == "POST":
        form = UserChangeForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile', id=user.id)
    else:
        form = UserChangeForm(instance=user)

    return render(request, 'profile_update.html', {'form': form})