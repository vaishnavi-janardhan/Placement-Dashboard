from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'Placement Dashboard'

urlpatterns = [
    path('', views.user_login, name='user_login'),
    # url(r'^user_login/$',views.user_login,name='user_login'),
    url('csv', views.getfile, name = 'download_csv'),
    url('getSelfPlaced', views.getSelfPlaced, name = 'getSelfPlaced')
]
