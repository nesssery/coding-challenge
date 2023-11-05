from django.contrib.auth import get_user_model
from allauth.account.views import SignupView, LoginView
from django.shortcuts import render
from django.views.generic import View
from users.forms import CustomLoginForm


User = get_user_model()


class CustomLoginView(LoginView):
    form_class = CustomLoginForm

class CustomSignupView(SignupView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Ajoutez ici d'autres données au contexte si nécessaire
        return context

class ConfirmationSignUpView(View):
    def get(self, request):
        context = {}
        return render(request, 'pages/conformation_signup.html', context)

