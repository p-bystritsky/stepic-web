from django.conf.urls import patterns, include, url

import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.test, name='root'),
    url(r'^login/$', views.test, name='login'),
    url(r'^signup/$', views.test, name='signup'),
    url(r'^question/(?P<id>\d+)/$', views.test, name='question'),
    url(r'^ask/$', views.test, name='ask'),
    url(r'^popular/$', views.test, name='popular'),
    url(r'^new/$', views.test, name='new'),
)
