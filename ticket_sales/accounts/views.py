from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .models import User
from .forms import RegistrationForm, LoginForm
from django.views import View


class UserRegisterView(View):
    form_class = RegistrationForm
    template_name = 'accounts/register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('events:index')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form_register': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            form.save(commit=False)
            new_user = User(
                phone_number=cd['phone_number'],
                email=cd['email'],
                national_code=cd['national_code'],
                first_name=cd['first_name'],
                last_name=cd['last_name']
            )
            new_user.set_password('password')
            new_user.save()
            return redirect('events:index')
        return render(request, self.template_name, {'form_register': form})

        #     cd = form.cleaned_data
        #     User.objects.create_user(
        #         phone_number=cd['phone_number'],
        #         email=cd['email'],
        #         password=cd['password'],
        #         first_name=cd['first_name'],
        #         last_name=cd['last_name']
        #     )
        #     return redirect('events:index')
        # return render(request, self.template_name, {'form_register': form})


class UserLoginView(View):
    form_class = LoginForm
    template_name = 'accounts/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('events:index')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form_login': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                phone_number=cd['phone_number'],
                password=cd['password'], )
            if user is not None:
                login(request, user)
                return redirect('events:index')
            return render(request, self.template_name, {'form_login': form})
        return render(request, self.template_name, {'form_login': form})


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('events:index')

    def post(self):
        pass
