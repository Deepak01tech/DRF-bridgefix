from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns=[
    path('get-token/',obtain_auth_token,name='api_token_auth'),
    path('profile/',views.user_profile,name='user_profile'),
    path('admin-panel/',views.admin_panel,name='admin_panel'),
]