from rest_framework import serializers
from stores.models import UserBadge

class UserBadgeSerializer(serializers.ModelSerializer):
    badgeName = serializers.CharField(source='badge.name', read_only=True)
    userEmail = serializers.CharField(source='user.email', read_only=True)
    userUsername = serializers.CharField(source='user.username', read_only=True)
    userPhone = serializers.CharField(source='user.phone', read_only=True)


    class Meta:
        model = UserBadge
        fields = ["badgeName", "userEmail", "userUsername", "userPhone"]
