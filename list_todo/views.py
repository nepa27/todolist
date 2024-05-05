"""views.py."""

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin)
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DetailView, DeleteView,
                                  ListView, TemplateView, UpdateView)
from django.shortcuts import render

from .forms import ListToDoForm
from .models import ListToDo

User = get_user_model()


class MainPageView(TemplateView):
    """Отображает главную страницу."""

    template_name = 'list_todo/index.html'


class ToDoListView(LoginRequiredMixin, ListView):
    """Отображает страницу с задачами пользователя."""

    model = ListToDo
    context_object_name = 'todo_list'
    ordering = 'is_ready'
    paginate_by = 12

    def get_queryset(self):
        """Получает список задач для конкретного пользователя."""
        if not self.request.user.is_superuser:
            return ListToDo.objects.filter(
                author=self.request.user
            ).order_by('is_ready')
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = (queryset.filter(
                name__icontains=query
            ))
        return queryset


class AddToDoView(LoginRequiredMixin, CreateView):
    """Отображает страницу добавления задачи."""

    model = ListToDo
    form_class = ListToDoForm
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        """Подставляет в автора имя пользователя."""
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateToDoView(LoginRequiredMixin, UpdateView):
    """Отображает страницу обновления задачи."""

    model = ListToDo
    fields = '__all__'
    context_object_name = 'todo'
    success_url = reverse_lazy('list')


class DeleteToDoView(LoginRequiredMixin, DeleteView):
    """Отображает страницу удаления задачи."""

    model = ListToDo
    context_object_name = 'todo'
    success_url = reverse_lazy('list')

    def test_func(self):
        """Проверяет, что пользователь - админ."""
        return self.request.user.is_superuser


class DetailToDoView(LoginRequiredMixin, DetailView):
    """Отображает страницу конкретной задачи."""

    model = ListToDo
    context_object_name = 'todo'

    def post(self, request, *args, **kwargs):
        """По нажатию на чек-бокс меняет поле is_ready."""
        for key, value in request.POST.items():
            if key.startswith('task-'):
                task_pk = int(key.replace('task-', ''))
                task = ListToDo.objects.get(pk=task_pk)
                task.is_ready = not task.is_ready
                task.save()
        return super().get(request, *args, **kwargs)


class ListPeopleView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """Отображает страницу списка пользователей."""

    model = User
    template_name = 'list_todo/list_people.html'
    context_object_name = 'users'

    def test_func(self):
        """Проверяет, что пользователь - админ."""
        return self.request.user.is_superuser


def page_not_found(request, exception):
    """Отображает страницу 404."""
    return render(request, 'pages/404.html', status=404)


def csrf_failure(request, reason=''):
    """Отображает страницу 404."""
    return render(request, 'pages/403csrf.html', status=403)
