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
    template_name = 'list_todo/index.html'


class ToDoListView(LoginRequiredMixin, ListView):
    model = ListToDo
    context_object_name = 'todo_list'
    ordering = 'is_ready'
    paginate_by = 12

    def get_queryset(self):
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
    model = ListToDo
    form_class = ListToDoForm
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateToDoView(LoginRequiredMixin, UpdateView):
    model = ListToDo
    fields = '__all__'
    context_object_name = 'todo'
    success_url = reverse_lazy('list')


class DeleteToDoView(LoginRequiredMixin, DeleteView):
    model = ListToDo
    context_object_name = 'todo'
    success_url = reverse_lazy('list')

    def test_func(self):
        return self.request.user.is_superuser


class DetailToDoView(LoginRequiredMixin, DetailView):
    model = ListToDo
    context_object_name = 'todo'

    def post(self, request, *args, **kwargs):
        for key, value in request.POST.items():
            if key.startswith('task-'):
                task_pk = int(key.replace('task-', ''))
                task = ListToDo.objects.get(pk=task_pk)
                task.is_ready = not task.is_ready
                task.save()
        return super().get(request, *args, **kwargs)


class ListPeopleView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = User
    template_name = 'list_todo/list_people.html'
    context_object_name = 'users'

    def test_func(self):
        return self.request.user.is_superuser


def page_not_found(request, exception):
    return render(request, 'pages/404.html', status=404)


def csrf_failure(request, reason=''):
    return render(request, 'pages/403csrf.html', status=403)
