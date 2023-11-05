import os
from stores.models import Model3d, UserBadge, Badge
from django.db.models import Sum
from django.db.models import Count
from users.models import CustomUser
from django.utils import timezone


currentDate = timezone.now()

oneYearAgo = currentDate - timezone.timedelta(days=365)

oneYearAgoUsers = CustomUser.objects.filter(date_joined__lte=oneYearAgo)
print('Hello', oneYearAgoUsers)


def runUpdate():
    user_views = Model3d.objects.values('user__username').annotate(total_views=Sum('views'))
    user_counts = CustomUser.objects.annotate(num_models=Count('model3d'))
    users_with_more_than_5_objects = user_counts.filter(num_models__gt=4)


    for user_data in user_views:
        print("____________________L'objet________________", user_data)
        username = user_data['user__username']
        totalViews = user_data['total_views']
        if totalViews >= 1000:
            user = CustomUser.objects.get(username=username)
            badge = Badge.objects.get(name="Star")
            print("________Nom d'utilisateur_____", username, "______Nombre de vue_____", totalViews)
            userBadge, created = UserBadge.objects.get_or_create(user=user, badge=badge)
            if user.badgeList is None:
                user.badgeList = []

            if "Star" not in user.badgeList:
                user.badgeList.append("Star")
            user.save()
            print("Badge créé avec succès", userBadge)

    
    for user in users_with_more_than_5_objects:
        user = CustomUser.objects.get(username=user)
        badge = Badge.objects.get(name="Collector")
        print("________Nom d'utilisateur_____", user, "______Badge_____", badge)
        userBadge, created = UserBadge.objects.get_or_create(user=user, badge=badge)
        if user.badgeList is None:
                user.badgeList = []
        if "Collector" not in user.badgeList:
                user.badgeList.append("Collector")
        user.save()


    for user in oneYearAgoUsers:
       badge = Badge.objects.get(name="Pionneer")
       userBadge, created = UserBadge.objects.get_or_create(user=user, badge=badge)
       print("________Nom d'utilisateur_____", user, "______Badge_____", badge)
       if user.badgeList is None:
                user.badgeList = []
       if "Pionneer" not in user.badgeList:
                user.badgeList.append("Pionneer")

       user.save()






        
        


