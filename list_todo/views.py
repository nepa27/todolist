from django.views.generic import (CreateView, DetailView, DeleteView,
                                  ListView, TemplateView, UpdateView)


class MainPageView(TemplateView):
    template_name = 'list_todo/index_2.html'


class ToDoListView(ListView):
    pass


class AddToDoView(CreateView):
    pass


class UpdateToDoView(UpdateView):
    pass


class DeleteToDoView(DeleteView):
    pass


class DetailToDoView(DetailView):
    pass
