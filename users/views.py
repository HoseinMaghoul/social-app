from django.shortcuts import render , redirect, get_object_or_404
from django.views import View
from . forms import UserRegistrationForm, UserLoginForm, ProfileImageForm
from . models import CustomUser
from django.contrib  import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class UserRegister(View):
    form_class = UserRegistrationForm
    template_name = 'users/register.html'


    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form':form})

    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            CustomUser.objects.create_user(username=cd['username'], email=cd['email'], password=cd['password'])
            messages.success(request, 'registraion successfuly', 'info')
            return redirect('core:home')
        return render(request, self.template_name, {'form':form})



class UserLogin(View):
    form_class = UserLoginForm
    template_name = 'users/login.html'


    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form':form})

    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'you login successfuly', 'info')
                return redirect('core:home')
            return render(request, self.template_name, {'form':form})



class UserLogout(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'you logout successfuly', 'info')
        return redirect('core:home')
        


class UserDashboard(LoginRequiredMixin, View):
    template_name = 'users/dashboard.html'
    form_class = ProfileImageForm

    def get(self, request, username):
        user = get_object_or_404(CustomUser, username=username)
        return render(request, self.template_name, {'user':user, 'form':self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'upload successfuly', 'info')
            return redirect('users:dashboard', request.user.username)
