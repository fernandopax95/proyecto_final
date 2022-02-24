from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from simple_history import register
from captcha.fields import CaptchaField


register (User, app= __package__)


class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'

class FormularioRegistro(UserCreationForm):
    username = forms.CharField( max_length=50)
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
  

    class Meta:
        model = User
        fields = ('username', 'nombre', 'apellido', 'email','password1','password2')


class AxesCaptchaForm(forms.Form):
    captcha = CaptchaField()