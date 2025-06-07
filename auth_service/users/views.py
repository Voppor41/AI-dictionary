from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegisterSerializer, LoginSerializer
from .models import CustomUser

class RegisterView(generics.CreateAPIView):
    queryset =CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny, )

    def get(self, request, *args, **kwargs):
        return Response({"message": "Страница регистрации работает!"})

    def perfome_create(self, serializer):
        user = serializer.save()

        return user

class LoginView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)

            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)