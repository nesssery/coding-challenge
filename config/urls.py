from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

handler404 = "stores.views.handler404view"
handler500 = "stores.views.handler500view"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("stores.urls")),
    path('accounts/', include('allauth.urls')),
    path('users/', include('users.urls')),
    path('api-v1/', include('api.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
