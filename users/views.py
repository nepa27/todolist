from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin)
from django.views.generic import UpdateView


User = get_user_model()


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    fields = ('username', )
    template_name = 'users/user_edit.html'
    # success_url = reverse_lazy('list_todo:profile')

    def test_func(self):
        return self.request.user.pk == self.kwargs['pk']
