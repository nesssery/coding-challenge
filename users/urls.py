from django.contrib.auth import views
from django.urls import path
from users.views import CustomSignupView, ConfirmationSignUpView, CustomLoginView

urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    path('accounts/login/', CustomLoginView.as_view(), name='account_login'),
    path('accounts/signup/confirmation/', ConfirmationSignUpView.as_view(), name='confirmation-signup'),
]
