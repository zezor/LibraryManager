from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BorrowViewSet, UserViewSet

router = DefaultRouter()
router.register('books', BookViewSet)
router.register('borrow', BorrowViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
