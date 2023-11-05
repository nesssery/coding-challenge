from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField




def getProfileImageFilePath(self, filename):
    return f'profileImages/{self.username}/{"profileImage.png"}'


def getDefaultProfileImage():
    return "defaultImage/profile.png"


class CustomUser(AbstractUser):
    username = models.CharField(max_length=256, null=True, blank=True, unique=True)
    email = models.CharField(max_length=256, null=True, blank=True, unique=True)
    phone = models.CharField(max_length=256, blank=True, null=True)
    badgeList = ArrayField(models.CharField(max_length=256), blank=True, null=True)
    profileImage = models.ImageField(upload_to=getProfileImageFilePath, default=getDefaultProfileImage, null=True, blank=True)
   


    def getProfileImagFilename(self):
        return str(self.profileImage)[str(self.profileImage).index(f'profileImages/{self.username}/'):]
        



