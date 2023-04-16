from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCreateClientAPIView.as_view(), name='get_post_clients'),
    path('<int:pk>/', views.RetrieveUpdateDestroyClientAPIView.as_view(), name='get_delete_update_client'),
]