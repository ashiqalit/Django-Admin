import django_filters
from django.forms import ModelForm
from django.contrib.auth.models import User

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')