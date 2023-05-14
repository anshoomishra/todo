from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = (
        "username",
        "email",

    )

    fieldsets = (
        (None, {"fields": ("username","email", "password")}),
        ("Permissions", {"fields": ("is_staff", "groups", "user_permissions")}),
    )


admin.site.register(CustomUser, CustomUserAdmin)