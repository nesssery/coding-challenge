from django.urls import path
from api.views import UserBadgeList

urlpatterns = [
    path('users-badges/', UserBadgeList.as_view(), name='users-badges-list'),
]