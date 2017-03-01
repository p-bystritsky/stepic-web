from django.conf.urls import url, include

import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.new, name='main'),
    url(r'^login/$', views.test, name='login'),
    url(r'^signup/$', views.test, name='signup'),
    url(r'^question/(?P<q_id>\d+)/$', views.view_question, name='question'),
    url(r'^ask/$', views.ask, name='ask'),
    url(r'^popular/$', views.popular, name='popular'),
    url(r'^new/$', views.new, name='new'),
]
