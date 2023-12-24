import rest_framework.urls
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include("api.urls")),
    path("api-auth/", include("rest_framework.urls")),

    path("", include('products.urls')),
    path('users/', include("users.urls")),
    path('users/', include("django.contrib.auth.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)