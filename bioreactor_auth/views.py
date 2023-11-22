from django.contrib.auth import authenticate, login, logout
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
import uuid

from .serializers import UserSerializer
from .models import DeviceAuthenticationToken


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = self.request.data.get('username')
        password = self.request.data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise ValidationError('Incorrect username or password!')
        if not user.is_active:
            raise ValidationError('The user has been set as inactive!')
        login(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
    permission_classes = []

    def get(self, *args, **kwargs):
        logout(self.request)
        return Response(status=HTTP_200_OK)


class GetDeviceAuthenticationTokenView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        name = self.request.query_params.get('name')
        if name:
            try:
                device_token = DeviceAuthenticationToken.objects.get(name=name)
            except DeviceAuthenticationToken.DoesNotExist:
                token = uuid.uuid4()
                while DeviceAuthenticationToken.objects.filter(token=token).count():
                    token = uuid.uuid4()
                device_token = DeviceAuthenticationToken.objects.create(name=name, token=token,
                                                                        created_by=self.request.user)
        else:
            raise ValidationError('No name passing')
        return Response(data=device_token.token)
