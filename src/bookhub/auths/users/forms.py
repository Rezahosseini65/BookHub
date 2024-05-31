from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    """Custom form for user creation."""
    class Meta:
        model = get_user_model()
        fields = ['username', 'email']


class CustomUserChangeForm(UserChangeForm):
    """Custom form for user modification."""
    class Meta:
        model = get_user_model()
        fields = ['username', 'email']