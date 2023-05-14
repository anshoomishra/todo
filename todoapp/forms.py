from .models import Task
from django.forms import ModelForm


class TaskCreationForm(ModelForm):
    class Meta:
        model = Task
        fields = ("title", "description","is_completed","age","completion_date","is_active","priority","user")


class TaskChangeForm(ModelForm):
    class Meta:
        model = Task
        fields = ("title", "description","is_completed","age","completion_date","is_active","priority","user")