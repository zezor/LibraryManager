from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, UserViewSet
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
