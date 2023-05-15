from django.contrib.auth.hashers import make_password
from django.forms import ModelForm

from apps.models import User


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'phone', 'password')

    def clean_password(self):
        password = self.data.get('password')
        return make_password(password)