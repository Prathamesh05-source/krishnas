
from django.contrib import admin
from django.urls import include, path

# urls
urlpatterns = [
    path('api/v1/clients/', include('client.urls')),
    path('api/v1/auth/', include('authentication.urls')),
    path('admin/', admin.site.urls),
]
