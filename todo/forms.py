from django import forms

from todo.models import Todo


class AddTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'


