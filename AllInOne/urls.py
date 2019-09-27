from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.Home, name='base'),
    url(r'^SignUp/$', views.SignUp, name = 'signup'),
    url(r'^Login/$', views.Login, name = 'login'),
    url(r'^Logout/$', views.Logout, name = 'logout'),
    url(r'^ChangePassword/$', views.ChangePassword, name = 'changepassword')

  ]
