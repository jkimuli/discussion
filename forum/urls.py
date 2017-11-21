from django.conf.urls import url
from . import views

 
urlpatterns = [

    url(r'^$',views.home,name='index'),

    url(r'^board/(?P<name>\w+)/new/$',views.topic_create,name='topic_create'),
    url(r'^board/(?P<name>\w+)/topics/$',views.board_topics,name='board_details'),

    url(r'^board/(?P<name>\w+)/topics/(?P<topic_pk>\d+)/$',views.topic_posts,name='topic_details'),
    url(r'^board/(?P<name>\w+)/topics/(?P<topic_pk>\d+)/reply/$',views.topic_reply,name='topic_reply'),


]