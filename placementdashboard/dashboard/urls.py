from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'Placement Dashboard'

urlpatterns = [
    path(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^welcome/$',views.index,name='index'),
    url('csv', views.getfile, name = 'download_csv')
]