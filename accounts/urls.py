__author__ = 'julius'

from accounts import views
from django.conf.urls import url
from django.contrib.auth.views import LogoutView,LoginView


urlpatterns = [

    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^login/$', LoginView.as_view(template_name='login.html'), name='login'),

]
