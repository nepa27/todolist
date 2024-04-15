from django.urls import path

from .views import ProfileView, UserCreateView, UserUpdateView


urlpatterns = [
    path('auth/registration/', UserCreateView.as_view(), name='registration'),
    path('user/edit/<int:pk>/', UserUpdateView.as_view(), name='user_edit'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
]
