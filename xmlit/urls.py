from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView,TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^', 'MyView.upload', name='upload'),
    # url(r'^blog/', include('blog.urls')),
    # ('^/$', TemplateView.as_view(template_name='index.html')),

    url(r'^$', RedirectView.as_view(url='/home')),
    url(r'^contact$', TemplateView.as_view(template_name="contact.html")),

    url(r'^home/', include('home.urls')),
    url(r'^update/', include('update.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    # (r'^accounts/profile/$', 'django.contrib.auth.views.profile'),

)
