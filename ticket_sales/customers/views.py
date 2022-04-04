import random

from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, FormView
from django.views.generic.edit import ModelFormMixin

from core.models import User
from customers.forms import VerifyPhoneForm
from customers.models import Customer
from utils import send_otp_code


class UserRegister(CreateView):
    model = User
    fields = ['first_name', 'last_name', 'national_code', 'phone']
    success_url = reverse_lazy('customers:verify-phone')
    template_name = 'user-register.html'

    def get_initial(self):
        init = super(UserRegister, self).get_initial()
        init.update({'request': self.request})
        return init

    def form_valid(self, form):
        verify_code = random.randint(1000, 9999)
        send_otp_code(form.cleaned_data['phone'], verify_code)
        self.request.session['user_register_info'] = {
            'first_name': form.cleaned_data['first_name'],
            'last_name': form.cleaned_data['last_name'],
            'national_code': form.cleaned_data['national_code'],
            'phone': form.cleaned_data['phone'],
            'password': str(verify_code)
        }
        self.object = User(
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            national_code=form.cleaned_data['national_code'],
            phone=form.cleaned_data['phone'],
        )
        return super(ModelFormMixin, self).form_valid(form)


class MyLoginView(LoginView):
    template_name = 'user-login.html'


class VerifyPhoneAndCreateCustomer(FormView):
    form_class = VerifyPhoneForm
    success_url = reverse_lazy('events:index')
    template_name = 'user-verify-phone.html'

    def get_form_kwargs(self):
        kw = super(VerifyPhoneAndCreateCustomer, self).get_form_kwargs()
        kw['request'] = self.request
        return kw

    def form_valid(self, form):
        user = User.objects.create_user(**self.request.session['user_register_info'])
        Customer.objects.create(user=user)
        login(self.request, user)
        return super().form_valid(form)
