from django.urls import path
from . import views 

urlpatterns = [
    path("", views.home, name="home"),
    path("user/<str:email>/", views.get_user, name="get_user"),
    path("user/", views.create_user, name="create_user")
]  