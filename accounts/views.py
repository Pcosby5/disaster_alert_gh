from rest_framework import viewsets, permissions
from .models import User
from .serializers import UserSerializer, UserRegisterSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class UserRegisterViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        operation_description="Register a new user account",
        request_body=UserRegisterSerializer,
        responses={201: openapi.Response('User created successfully')}
    )
    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
