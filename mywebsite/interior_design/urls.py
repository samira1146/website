from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('designer/', views.designer_list, name='designer'),
    path('jornal/', views.jornal_list, name='jornal')

]