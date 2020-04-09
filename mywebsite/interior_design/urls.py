from django.urls import path,re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('signUp/', views.user_sign_up, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('designers/', views.designer_list, name='designer'),
    re_path('designer/(?P<id>[0-9]+)/$', views.designer_page, name='designer_pagesPages'),
    re_path('designer/(?P<name>[\w-]+)/(?P<id>[0-9]+)/(?P<title>[\w|\W]+)/$', views.article, name='designer_article'),
    path('jornal/', views.jornal_list, name='jornal')

]