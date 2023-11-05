from django.urls import path
from stores.views import HomeView, EditorView, DetailView
urlpatterns = [
    path('', HomeView.as_view(), name="home-view"),
    path('model-3d/<str:pk>/', DetailView.as_view(), name="detail-view"),
    path('accounts/user/editor/', EditorView.as_view(), name='account-user-editor'),
]