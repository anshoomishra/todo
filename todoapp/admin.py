from django.contrib import admin
from .models import Task
from django.contrib import admin
from .forms import TaskChangeForm,TaskCreationForm


class CustomTaskAdmin(admin.ModelAdmin):
    form = TaskChangeForm
    add_form = TaskCreationForm
    model = Task
    list_display = (
        "title",
        "created_at",

    )

    fieldsets = (
        (None, {"fields": ("title", "description","age","is_completed","completion_date","is_active","priority","user")}),

    )


admin.site.register(Task,CustomTaskAdmin)