from django.urls import path 
from . import views


urlpatterns = [
    path('', views.index, name = "index"),
    path('home/', views.home, name = "home"), # not coded yet
    path('login/', views.login_view, name = "login"),
    path('register/', views.register_view, name = "register"),
    path('logout/', views.logout_view, name = "logout"),
]