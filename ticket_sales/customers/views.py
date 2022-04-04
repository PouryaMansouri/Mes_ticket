from django.views.generic import CreateView, TemplateView


class UserRegister(CreateView):
    pass


class Login(TemplateView):
    pass


class VerifyPhoneAndCreateCustomer(CreateView):
    pass
