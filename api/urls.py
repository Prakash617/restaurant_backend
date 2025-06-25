# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, MenuItemViewSet, TableViewSet, OrderViewSet
from .views import CookieTokenObtainPairView,logout_view

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('menu-items', MenuItemViewSet)
router.register('tables', TableViewSet)
router.register('orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/user/', current_user_view, name='current_user'),
    path('auth/login/', CookieTokenObtainPairView.as_view(), name='cookie_token_obtain_pair'),
    path('auth/logout/', logout_view),

]
