from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoginView, DashboardView, StudentAchievementViewSet

router = DefaultRouter()
router.register(r'achievements', StudentAchievementViewSet, basename='achievement')

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name='login'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('', include(router.urls)),
]