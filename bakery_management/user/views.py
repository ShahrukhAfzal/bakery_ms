from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.response import Response
from knox.models import AuthToken

from user.serializers import UserSerializer, CreateUserSerializer


class RegisterAPI(generics.GenericAPIView):
    """
    User can register through this api
    """
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        _, token = AuthToken.objects.create(user)

        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()
                                ).data,
            "token": token
        })

