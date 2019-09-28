from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$',views.Home, name='base'),
    url(r'^SignUp/$', views.SignUp, name = 'signup'),
    url(r'^Login/$', views.Login, name = 'login'),
    url(r'^Logout/$', views.Logout, name = 'logout'),
    url(r'^ChangePassword/$', views.ChangePassword, name = 'changepassword'),
    url(r'^Upload/$', views.Upload, name = 'upload')
  ]
urlpatterns += staticfiles_urlpatterns()
