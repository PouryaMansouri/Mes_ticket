from django.contrib.auth.views import LogoutView
from django.urls import path

from customers.views import UserRegister, VerifyPhoneAndCreateCustomer, MyLoginView
from customers.apis import OTPAPIView

app_name = 'customers'
urlpatterns = [
    path('register', UserRegister.as_view(), name='register'),
    path('login', MyLoginView.as_view(), name='login'),
    path('verify-phone', VerifyPhoneAndCreateCustomer.as_view(), name='verify-phone'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('otpapiview/', OTPAPIView.as_view(), name='otpapiview'),
]
