from django.views.generic import CreateView, TemplateView


class UserRegister(CreateView):
    pass


class Login(TemplateView):
    template_name = 'user-login.html'


class VerifyPhoneAndCreateCustomer(CreateView):
    pass
