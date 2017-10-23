from django.conf.urls import url
from . import views

 
urlpatterns = [

    url(r'^$',views.home,name='index'),
    url(r'^board/(?P<name>\w+)/new/$',views.topic_create,name='topic_create'),
    url(r'^board/(?P<name>\w+)/$',views.board_topics,name='board_details'),


]