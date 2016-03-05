from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from api import views

#router = routers.SimpleRouter()
#router.register(r'words', views.WordList.as_view())

urlpatterns = [
    url(r'^words/limit/(?P<limit>[0-9]+)/page/(?P<page>[0-9]+)/$', views.WordList.as_view()),
    url(r'^words/limit/page/(?P<page>[0-9]+)/(?P<limit>[0-9]+)/$', views.WordList.as_view()),

    url(r'^homo/(?P<word>[a-zA-Z]+)/$', views.HomoList.as_view()),

    url(r'^levels/$', views.LevelList.as_view()),
    url(r'^level/(?P<id>[0-9]+)/$', views.LevelDetail.as_view()),

    url(r'^sentences/$', views.SentenceList.as_view()),
    url(r'^sentence/(?P<id>[0-9]+)/$', views.SentenceDetail.as_view()),

    url(r'^notes/$', views.NoteList.as_view()),
    url(r'^note/(?P<id>[0-9]+)/$', views.NoteDetail.as_view()),

    url(r'^user/(?P<uid>[0-9]+)/$', views.UserProfile.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^register/$', views.Register.as_view()),
    url(r'^login/$', views.Login.as_view()),
    url(r'^loginout/$', views.LoginOut.as_view()),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
]