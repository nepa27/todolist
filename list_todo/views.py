from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin)
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DetailView, DeleteView,
                                  ListView, TemplateView, UpdateView)
from django.shortcuts import render

from .forms import ListToDoForm
from .models import ListToDo


class MainPageView(TemplateView):
    template_name = 'list_todo/index.html'


class ToDoListView(LoginRequiredMixin, ListView):
    model = ListToDo
    context_object_name = 'todo_list'
    ordering = '-add_date'
    paginate_by = 10


class AddToDoView(LoginRequiredMixin, CreateView):
    model = ListToDo
    form_class = ListToDoForm
    success_url = reverse_lazy('list')


class UpdateToDoView(LoginRequiredMixin, UpdateView):
    model = ListToDo
    success_url = reverse_lazy('list')


class DeleteToDoView(LoginRequiredMixin, DeleteView):
    model = ListToDo
    success_url = reverse_lazy('list')


class DetailToDoView(LoginRequiredMixin, DetailView):
    model = ListToDo
    context_object_name = 'todo'


def ready_ex(request):
    pass


def not_ready_ex(request):
    pass


def page_not_found(request, exception):
    return render(request, 'pages/404.html', status=404)


def csrf_failure(request, reason=''):
    return render(request, 'pages/403csrf.html', status=403)