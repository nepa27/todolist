from django.urls import path

from .views import UserCreateView, UserUpdateView


urlpatterns = [
    path('auth/registration/', UserCreateView.as_view(), name='registration'),
    path('user/edit/<int:pk>/', UserUpdateView.as_view(), name='user_edit'),
]
