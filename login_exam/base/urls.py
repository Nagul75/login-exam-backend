from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_pokemon, name='get_pokemon'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login' ),
    path('logout/', views.user_logout, name='logout'),
    path('check-auth/', views.check_authentication, name='check-auth'),
    path('not-auth/', views.not_authenticated, name='not-auth')
]