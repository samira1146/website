from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('signUp/', views.user_sign_up, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('designer/', views.designer_list, name='designer'),
    path('jornal/', views.jornal_list, name='jornal')

]