from django.forms import DateTimeInput, ModelForm

from .models import ListToDo


class ListToDoForm(ModelForm):
    class Meta:
        model = ListToDo
        fields = (
            'name',
            'description',
            'category',
            'is_ready',
            'ready_date'
        )
        widgets = {
            'ready_date': DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%d %H:%M',
            )
        }

