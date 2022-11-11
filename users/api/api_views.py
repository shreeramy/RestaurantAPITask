from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from base.utils import getotp, send_otp, verify_otp

from ..models import User
from .serializers import UserCreateSerializer, EmployeeCreateSerializer
from restrant.models import Restraunt
from base.messages import Messages


class UserCreateView(APIView):
    serializer_class = UserCreateSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            email = request.data['email'].lower()
            user = User.objects.filter(email=email).first()
            if user is None or user.is_active:
                serializer = self.serializer_class(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    otp = getotp()
                    send_otp(context={"otp":otp['otp'], "email":email},
                             email=email, subject=Messages.OTP_MESSAGE)
                    response_data = {}
                    response_data ['message'] = Messages.OTP_SEND
                    response_data ['secret'] = otp['secret']
                    return Response(response_data, 
                                    status=status.HTTP_201_CREATED)
                return Response(serializer.errors, 
                                status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer = self.serializer_class(user, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    otp = getotp()
                    send_otp(context={"otp":otp['otp'], "email":email},
                             email=email, subject=Messages.OTP_MESSAGE)
                    response_data = {}
                    response_data ['message'] = Messages.OTP_SEND
                    response_data ['secret'] = otp['secret']
                    return Response(response_data, 
                                    status=status.HTTP_201_CREATED)
                return Response(serializer.errors, 
                                status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.\
                            HTTP_500_INTERNAL_SERVER_ERROR)

class UserOTPView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        email = request.data['email'].lower()
        user = User.objects.filter(email=email).first()
        restrant = Restraunt.objects.filter(owner=user).first()
        if user:
            verify = verify_otp(otp=request.data['otp'],
                           secret=request.data['secret'])
            if verify:
                user.is_active = True
                user.is_restraunt = True
                user.save()
                restrant.is_verify = True
                restrant.save()
                return Response(Messages.ACCOUNT_CREATE, 
                                status=status.HTTP_202_ACCEPTED)
            return Response(Messages.OTP_FAILED, 
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(Messages.USER_NOT_FOUND, 
                        status=status.HTTP_404_NOT_FOUND)


class EmployeeCreateView(APIView):
    serializer_class = EmployeeCreateSerializer

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(Messages.EMPLOYEE_CREATE, 
                                status=status.HTTP_201_CREATED)
            return Response(serializer.errors, 
                            status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.\
                            HTTP_500_INTERNAL_SERVER_ERROR)