from django.urls import path

from customers.views import UserRegister, Login, VerifyPhoneAndCreateCustomer

app_name = 'customers'
urlpatterns = [
    path('register', UserRegister.as_view(), name='register'),
    path('login', Login.as_view(), name='login'),
    path('verify-phone', VerifyPhoneAndCreateCustomer.as_view(), name='verify-phone'),
]
