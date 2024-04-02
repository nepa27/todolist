from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin)
from django.views.generic import CreateView, UpdateView

from .forms import CustomUserCreationForm

User = get_user_model()


class UserCreateView(CreateView):
    template_name = 'registration/registration_form.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    fields = ('username',)
    template_name = 'users/user_edit.html'
    success_url = reverse_lazy('index')

    def test_func(self):
        return self.request.user.pk == self.kwargs['pk']
