from django.conf.urls import patterns, url

from home import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),

    url(r'^show-textlist/$', views.show_textlist, name='show_textlist'),
    url(r'^textlist/$', views.TextList.as_view()),
    url(r'^test/$', views.test, name='test'),

)