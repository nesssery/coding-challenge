from django.db import models
from users.models import CustomUser
from django.utils import timezone


class Badge(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    dateAdded = models.DateTimeField(default=timezone.now, blank=True, null=True, verbose_name="La date et l'heure d'ajout")
    dateUpdated = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="La date et l'heure de mise à jour")

    def __str__(self):
        return self.name


    class Meta:
        ordering = ('-dateAdded',)
        verbose_name = "Les badges"
        verbose_name_plural = "Les badges"


class UserBadge(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE, null=True, blank=True)
    dateAdded = models.DateTimeField(default=timezone.now, blank=True, null=True, verbose_name="La date et l'heure d'ajout")
    dateUpdated = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="La date et l'heure de mise à jour")

    def __str__(self):
        return f"{self.user.email} - {self.badge.name}"


    class Meta:
        ordering = ('-dateAdded',)
        verbose_name = "Les badges attribués"
        verbose_name_plural = "Les badges attribués"




def getModel3deFilepath(self, filename):
    return f'Model3dImages/{self.title[:16].replace(" ", "_")}/{"image.png"}'


class Model3d(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to=getModel3deFilepath, null=True, blank=True, verbose_name="L'image 3D")
    title = models.CharField(max_length=256, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    views = models.IntegerField(default=0, null=True, blank=True)
    dateAdded = models.DateTimeField(default=timezone.now, blank=True, null=True, verbose_name="La date et l'heure d'ajout")
    dateUpdated = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="La date et l'heure de mise à jour")


    def __str__(self):
        return self.title

    def getModel3dFilepath(self):
        return str(self.image)[str(self.image).index(f'Model3dImages/{self.title[:16].replace(" ", "_")}/'):]

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    class Meta:
        ordering = ('-dateAdded',)
        verbose_name = "Les Model3d"
        verbose_name_plural = "Les Model3d"
