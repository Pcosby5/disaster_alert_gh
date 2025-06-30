from rest_framework.routers import DefaultRouter
from .views import UserViewSet, UserRegisterViewSet
from django.urls import path

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('register/', UserRegisterViewSet.as_view({'post': 'register'})),
]

urlpatterns += router.urls
