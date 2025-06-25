# api/views.py

from rest_framework import viewsets, permissions
from .models import Category, MenuItem, Table, Order
from .serializers import (
    CategorySerializer,
    MenuItemSerializer,
    TableSerializer,
    OrderSerializer
)
from .permissions import IsOwnerOrAdmin

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated]

class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [permissions.IsAuthenticated]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()  # 👈 add this line
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated,IsOwnerOrAdmin]

    def get_queryset(self):
        return Order.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

# api/views.py

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
class CookieTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            data = response.data
            refresh = data.get('refresh')
            access = data.get('access')
            response.set_cookie(
                key=settings.SIMPLE_JWT['AUTH_COOKIE'],
                value=access,
                httponly=True,
                secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE'],
                path=settings.SIMPLE_JWT['AUTH_COOKIE_PATH'],
                # domain=settings.SIMPLE_JWT.get('AUTH_COOKIE_DOMAIN'), # optional
            )
            response.set_cookie(
                key=settings.SIMPLE_JWT['AUTH_COOKIE_REFRESH'],
                value=refresh,
                httponly=True,
                secure=settings.SIMPLE_JWT['AUTH_COOKIE_REFRESH_SECURE'],
                samesite=settings.SIMPLE_JWT['AUTH_COOKIE_REFRESH_SAMESITE'],
                path=settings.SIMPLE_JWT['AUTH_COOKIE_REFRESH_PATH'],
                # domain=settings.SIMPLE_JWT.get('AUTH_COOKIE_REFRESH_DOMAIN'), # optional
            )
            response.data = {'message': 'Login successful'}
        return response

from django.conf import settings
from django.http import JsonResponse

def logout_view(request):
    response = JsonResponse({'message': 'Logged out'})
    response.delete_cookie(settings.SIMPLE_JWT['AUTH_COOKIE'])
    response.delete_cookie(settings.SIMPLE_JWT['AUTH_COOKIE_REFRESH'])
    return response

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user_view(request):
    user = request.user
    return Response({
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "is_staff": user.is_staff,
        "is_superuser": user.is_superuser,
    })
