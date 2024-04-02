from django.forms import ModelForm

from .models import ListToDo


class ListToDoForm(ModelForm):
    class Meta:
        model = ListToDo
        fields = (
            'name',
            'author',
            'description',
            'category',
            'is_ready',
        )
