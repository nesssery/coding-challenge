from rest_framework import generics
from stores.models import CustomUser, UserBadge
from api.serializers import UserBadgeSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class UserBadgeList(APIView):
    serializer_class = UserBadgeSerializer
    def get(self, request, format=None, *args, **kwargs):
        userBadges = UserBadge.objects.values('user').distinct()
        userBadgesList = []

        for user_badge in userBadges:
            userId = user_badge['user']
            userBadges = UserBadge.objects.filter(user=userId)
            serializedBadges = self.serializer_class(userBadges, many=True)
            userData = {
                'userId': userId,
                'userInfos': serializedBadges.data
            }
            if userData not in userBadgesList:
                userBadgesList.append(userData)
        return Response(userBadgesList, status=status.HTTP_200_OK)