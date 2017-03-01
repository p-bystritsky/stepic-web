from django.conf.urls import url, include

from django.contrib import admin

admin.autodiscover()

import qa.urls

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(qa.urls, namespace='qa'))
]
