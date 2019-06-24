from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'Placement Dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]