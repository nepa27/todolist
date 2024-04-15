from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin)
from django.views.generic import CreateView, UpdateView, DetailView

from .forms import CustomUserCreationForm
from list_todo.models import ListToDo

User = get_user_model()


class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = context['user']
        todos = ListToDo.objects.filter(
            author=user.id,
        )
        context['count_todos'] = todos.count()
        context['count_uncomplete'] = todos.filter(is_ready=False).count()
        context['count_complete'] = todos.filter(is_ready=True).count()
        return context


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
