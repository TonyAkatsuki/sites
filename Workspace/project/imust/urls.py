from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Login, name='Login'),
    url(r'^Login.html/$', views.quit, name='quit'),
    url(r'^S_Forum-comment.html/$', views.forumComment, name='forumComment'),
    url(r'^S_Forum-comment.html$', views.forumComment, name='forumComment'),
    url(r'^S_Forum-publish.html$', views.forumPublish, name='forumPublish'),
    url(r'^S_Forum-publish.html/$', views.forumPublish, name='forumPublish'),
    url(r'^S_Forumhome.html$', views.forumhome, name='forumhome'),
    url(r'^S_Forumhome.html/$', views.forumhome, name='forumhome'),
    url(r'^S_Home.html$', views.home, name='home'),
    url(r'^S_Home.html/$', views.home, name='home'),
    url(r'^S_News.html$', views.news, name='news'),
    url(r'^S_News.html/$', views.news, name='news'),
    url(r'^S_Time.html$', views.time, name='time'),
    url(r'^S_Time.html/$', views.time, name='time'),
    url(r'^postAr$', views.submitAr, name='submitAr'),
    url(r'^postAr/$', views.submitAr, name='submitAr'),
    url(r'^postCo/$', views.submitCo, name='submitCo'),
    url(r'^refresh$', views.refreshNew, name='refreshNew'),
    url(r'^refresh/$', views.refreshNew, name='refreshNew'),
    url(r'^login$', views.login, name='login'),
]