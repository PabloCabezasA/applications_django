from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'myapp.views.index', name='index'),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^myweb/', include('myweb.urls', namespace="myweb")),
)