from django.conf.urls import patterns, include, url

import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.new, name='main'),
    url(r'^login/$', views.test, name='login'),
    url(r'^signup/$', views.test, name='signup'),
    url(r'^question/(?P<q_id>\d+)/$', views.question, name='question'),
    url(r'^ask/$', views.test, name='ask'),
    url(r'^popular/$', views.popular, name='popular'),
    url(r'^new/$', views.new, name='new'),
)
