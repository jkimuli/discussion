__author__ = 'julius'

from accounts import views
from django.conf.urls import url
from django.contrib.auth.views import (LogoutView, LoginView, PasswordResetView,
                                       PasswordResetDoneView, PasswordResetConfirmView,
                                       PasswordResetCompleteView, PasswordChangeView,
                                       PasswordChangeDoneView)


urlpatterns = [

    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^login/$', LoginView.as_view(template_name='login.html'), name='login'),

    #Password Reset Views

    url(r'^reset/$', PasswordResetView.as_view(template_name='password_reset.html',
                                               email_template_name='password_reset_email.html',
                                               subject_template_name='password_reset_subject.txt'),
        name='password_reset'),

    url(r'^reset/done/$', PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),

    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),

    url(r'^reset/complete/$', PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),


    # Password Change Urls

    url(r'^password_change/$', PasswordChangeView.as_view(template_name='password_change.html'),
          name='password_change'),

    url(r'^password_change/done/$', PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
           name='password_change_done.html'),

]
