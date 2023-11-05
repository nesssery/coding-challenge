from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import CustomUser
from django.forms import ModelForm
from django import forms
from allauth.account.forms import LoginForm, SignupForm


class CustomLoginForm(LoginForm):
    login = forms.CharField(
        max_length=256,
        label="Nom d'utilisiteur",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Nom d'utilisiteur"})
    )
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'})


class CustomUserCreationForm(SignupForm):
    username = forms.CharField(
        max_length=256,
        label="Nom d'utilisiteur",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Nom d'utilisiteur"})
    )

    email = forms.CharField(
        max_length=256,
        label="Email",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    phone = forms.CharField(
        max_length=256,
        label="Téléphone",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Téléphone'})
    )

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def save(self, request):
        user = super(CustomUserCreationForm, self).save(request)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']
        user.save()
        return user


class CustomCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone']


class UpdateUserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone']

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
