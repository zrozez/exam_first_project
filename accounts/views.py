from django.contrib.auth.models import User
from accounts.forms import CreateLoginForm, LoginForm
from django.shortcuts import redirect, render, reverse
from django.views import View
from django.contrib.auth import authenticate, get_user_model, login, logout

from accounts.forms import LoginForm

User = get_user_model()

class LoginView(View):

    def get(self, request):

        if request.user.is_authenticated:
            return redirect(reverse('posts_list_url'))

        login_form = LoginForm()

        return render(request, 'accounts/login.html', context={'login_form':login_form })

    def post(self, request):
        
        bound_form = LoginForm(request.POST)
        if bound_form.is_valid():
            username = bound_form.cleaned_data.get('username')
            password = bound_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect(reverse('posts_list_url'))
            
            
        return render(request, 'accounts/login.html', context={'bound_form':bound_form})

class CreateUserView(View):

    def get(self, request):
        registration_form = CreateLoginForm()
        return render(request, 'accounts/register.html', context={'registration_form':registration_form})

    def post(self, request):
        
        bound_form = CreateLoginForm(request.POST)
        
        if bound_form.is_valid():
            username = bound_form.cleaned_data.get('username')
            password = bound_form.cleaned_data.get('password')
        
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, password=password)

            login(request, user)
            return redirect(reverse('post_create_url'))
        
        return render(request, 'accounts/register.html', context={'registration_form':bound_form})


def logout_view(request):
    logout(request)
    return redirect(reverse('login_url'))     

