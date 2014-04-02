from django.conf.urls import patterns, url

from update import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^upload_slide/$', views.upload_slide, name='upload_slide'),
    url(r'^edit/(\d{1,2})/$', views.edit, name='edit'),
    # url(r'^TextUpdate/$', views.TextUpdate.as_view()),
)