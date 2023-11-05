from django.contrib import admin
from stores.models import Model3d, Badge, UserBadge




@admin.register(Model3d)
class Model3dAdmin(admin.ModelAdmin):
    model = Model3d
    list_display = ("id", "title", "description", 'image')
    list_filter = ("title", "dateAdded",)
    search_fields = ("title", "title",)
    save_on_top = True



@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    model = Badge
    list_display = ("id", "name", "description",)
    list_filter = ("name", "dateAdded",)
    search_fields = ("name", "description",)
    save_on_top = True


@admin.register(UserBadge)
class UserBadgeAdmin(admin.ModelAdmin):
    model = UserBadge
    list_display = ("id", "user", "badge",)
    list_filter = ("user", "dateAdded",)
    search_fields = ("user", "badge",)
    save_on_top = True
