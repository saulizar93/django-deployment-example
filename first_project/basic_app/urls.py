from django.urls import path
from . import views

#template tagging
app_name = 'basic_app'


urlpatterns = [
    path('', views.index),
    path('other', views.other, name='other'),
    path('relative',views.relative, name='relative'),
    path('home', views.index2, name='index2'),
    path('register', views.register, name='register'),
    path('user_login', views.user_login, name='user_login'),
]
