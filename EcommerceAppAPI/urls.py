from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('products/', views.products),
    path('products/<int:id>', views.single_product),
    path('secret', views.secret),
    path('api-token-auth', obtain_auth_token)
]