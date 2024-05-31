from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, UserChangeForm
from .models import CustomUser, Profile


# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = ('username', 'email')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)