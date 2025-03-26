from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.Login, name='login' ),
    path('logout/', views.logout, name='logout'),
    path('check-auth/', views.check_authentication, name='check-auth'),
    path('not-auth/', views.not_authenticated, name='not-auth')
]