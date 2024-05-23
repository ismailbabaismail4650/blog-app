from django.urls import path
#from django.contrib.auth import views as auth_views
from . import views
from .views import  MyloginViews, Registerpage, Editpage,ChangePassword,ProfilePage,EditProfilePage, CreateProfileView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/',MyloginViews.as_view(), name="login"),
    path('logout/', views.Mylogout, name='logout'),
    path('register/',Registerpage.as_view(), name="register"),
    path('edit/',Editpage.as_view(), name="edit"),
    path('password/',ChangePassword.as_view(), name="password"),
    path('<int:pk>/profile/',ProfilePage.as_view(), name="user_profile"),
    path('<int:pk>/profiles/',EditProfilePage.as_view(), name="user_bio"),
    path('create_profile/',CreateProfileView.as_view(), name="create_profile")
   
    
]
   