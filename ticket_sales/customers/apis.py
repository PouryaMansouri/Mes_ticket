import random

from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import User
from customers.models import Customer
from utils import send_otp_code
from django.utils.translation import gettext_lazy as _


class OTPAPIView(APIView):
    def post(self, request):
        phone = request.POST.get('phone', None)
        if Customer.objects.filter(user__phone=phone).exists():
            verify_code = random.randint(1000, 9999)
            send_otp_code(phone, verify_code)
            user = User.objects.get(phone=phone)
            user.set_password(str(verify_code))
            user.save()
            return Response(status=200)
        else:
            return Response(
                data=
                {
                    'message': _('You haven\'t registered yet with this phone number!')
                },
                status=400
            )
